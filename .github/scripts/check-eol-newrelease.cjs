// @ts-check

/**
 * @typedef {object} ReleaseCycle
 * @property {string|number} cycle - Release cycle (e.g. "1.20", 8.1, etc.)
 * @property {string} [releaseDate] - YYYY-MM-DD string for the first release in this cycle
 * @property {string|boolean} [eol] - End of Life date (YYYY-MM-DD) or false if not EoL
 * @property {string} [latest] - Latest release in this cycle
 * @property {string|null} [link] - Link to changelog or similar, if available
 * @property {boolean|string} [lts] - Whether this cycle is non-LTS (false), or LTS starting on a given date
 * @property {string|boolean} [support] - Active support date (YYYY-MM-DD) or boolean
 * @property {string|boolean} [discontinued] - Discontinued date (YYYY-MM-DD) or boolean
 */

/**
 * @typedef {object} EolNewReleaseConfig
 * @property {string} languageName
 * @property {string} eolJsonUrl
 * @property {string} eolViewUrl
 * @property {number} eolLookbackDays
 * @property {number} newReleaseThresholdDays
 * @property {boolean} ltsOnly
 * @property {number} retryCount
 * @property {number} retryIntervalSec
 */

/**
 * This script checks EoL and new releases from endoflife.date JSON.
 * It creates Issues for:
 *   - EoL reached within eolLookbackDays
 *   - New releases within newReleaseThresholdDays
 * If fetching fails after multiple retries, an error Issue is created once per week.
 *
 * Note this script is used in a GitHub Action workflow, and some line/line-bot-sdk-* repositories.
 * If you modify this script, please consider syncing the changes to other repositories.
 *
 * @param {import('@actions/github-script').AsyncFunctionArguments} actionCtx
 * @param {EolNewReleaseConfig} config
 */
module.exports = async function checkEolAndNewReleases(actionCtx, config) {
    const { github, context, core } = actionCtx;
    const {
        languageName,
        eolJsonUrl,
        eolViewUrl,
        eolLookbackDays,
        newReleaseThresholdDays,
        ltsOnly,
        retryCount,
        retryIntervalSec,
    } = config;

    /**
     * Returns a simple "year-week" string like "2025-W09".
     * This is a rough calculation (not strictly ISO-8601).
     * @param {Date} date
     * @returns {string}
     */
    const getYearWeek = (date) => {
        const startOfYear = new Date(date.getFullYear(), 0, 1);
        const dayOfYear = Math.floor((date - startOfYear) / 86400000) + 1;
        const weekNum = Math.ceil(dayOfYear / 7);
        return `${date.getFullYear()}-W${String(weekNum).padStart(2, '0')}`;
    };

    /**
     * Simple dedent function.
     * Removes common leading indentation based on the minimum indent across all lines.
     * Also trims empty lines at the start/end.
     * @param {string} str
     * @returns {string}
     */
    const dedent = (str) => {
        const lines = str.split('\n');
        while (lines.length && lines[0].trim() === '') lines.shift();
        while (lines.length && lines[lines.length - 1].trim() === '') lines.pop();

        /** @type {number[]} */
        const indents = lines
            .filter(line => line.trim() !== '')
            .map(line => (line.match(/^(\s+)/)?.[1].length) ?? 0);

        const minIndent = indents.length > 0 ? Math.min(...indents) : 0;
        return lines.map(line => line.slice(minIndent)).join('\n');
    };

    /**
     * Creates an Issue if an Issue with the same title does not exist (state=all).
     * @param {string} title
     * @param {string} body
     * @param {string[]} [labels]
     * @returns {Promise<boolean>} true if created, false if an Issue with same title already exists
     */
    const createIssueIfNotExists = async (title, body, labels = []) => {
        const issues = await github.rest.issues.listForRepo({
            owner: context.repo.owner,
            repo: context.repo.repo,
            state: 'all',
            per_page: 100,
        });
        const found = issues.data.find(i => i.title === title);
        if (found) {
            core.info(`Issue already exists: "${title}"`);
            return false;
        }
        await github.rest.issues.create({
            owner: context.repo.owner,
            repo: context.repo.repo,
            title,
            body,
            labels,
        });
        core.notice(`Created Issue: "${title}"`);
        return true;
    };

    /**
     * Fetch with retry, returning an array of ReleaseCycle objects.
     * @param {string} url
     * @returns {Promise<ReleaseCycle[]>}
     */
    const fetchWithRetry = async (url) => {
        let lastErr = null;
        for (let i = 1; i <= retryCount; i++) {
            try {
                const response = await fetch(url);
                if (!response.ok) {
                    throw new Error(`HTTP ${response.status} ${response.statusText}`);
                }
                /** @type {ReleaseCycle[]} */
                const jsonData = await response.json();
                return jsonData;
            } catch (err) {
                lastErr = err;
                core.warning(`Fetch failed (attempt ${i}/${retryCount}): ${err.message}`);
                if (i < retryCount) {
                    await new Promise(r => setTimeout(r, retryIntervalSec * 1000));
                }
            }
        }
        throw new Error(`Failed to fetch after ${retryCount} attempts: ${lastErr?.message}`);
    };

    /**
     * Check EoL for a single release.
     * @param {ReleaseCycle} release
     * @param {Date} now
     * @param {Date} eolLookbackDate
     */
    const checkEoL = async (release, now, eolLookbackDate) => {
        if (ltsOnly && release.lts === false) {
            core.info(`Skipping non-LTS release: ${release.cycle}`);
            return;
        }
        if (typeof release.eol === 'string') {
            const eolDate = new Date(release.eol);
            if (!isNaN(eolDate.getTime())) {
                // Check if it reached EoL within the last eolLookbackDays
                if (eolDate <= now && eolDate >= eolLookbackDate) {
                    if (!release.cycle) return;
                    const title = `Drop ${languageName} ${release.cycle} support`;
                    const body = dedent(`
                        This version(${languageName} ${release.cycle}) has reached End of Life.
                        Please drop its support as needed.
                        
                        **EoL date**: ${release.eol}
                        endoflife.date for ${languageName}: ${eolViewUrl}
                        `);
                    await createIssueIfNotExists(title, body, ['keep']);
                }
            }
        }
    };

    /**
     * Check new release for a single release.
     * @param {ReleaseCycle} release
     * @param {Date} now
     * @param {Date} newReleaseSince
     */
    const checkNewRelease = async (release, now, newReleaseSince) => {
        if (ltsOnly && release.lts === false) {
            core.info(`Skipping non-LTS release: ${release.cycle}`);
            return;
        }
        if (typeof release.releaseDate === 'string') {
            const rDate = new Date(release.releaseDate);
            if (!isNaN(rDate.getTime())) {
                // Check if releaseDate is within newReleaseThresholdDays
                if (rDate >= newReleaseSince && rDate <= now) {
                    if (!release.cycle) return;
                    const ltsTag = ltsOnly ? ' (LTS)' : '';
                    const title = `Support ${languageName} ${release.cycle}${ltsTag}`;
                    const body = dedent(`
                        A new version(${languageName} ${release.cycle}) has been released.
                        Please start to support it.
                        
                        **Release date**: ${release.releaseDate}
                        endoflife.date for ${languageName}: ${eolViewUrl}            
                        `);
                    await createIssueIfNotExists(title, body, ['keep']);
                }
            }
        }
    };

    core.info(`Starting EoL & NewRelease check for ${languageName} ...`);
    const now = new Date();
    const eolLookbackDate = new Date(now);
    eolLookbackDate.setDate(eolLookbackDate.getDate() - eolLookbackDays);

    const newReleaseSince = new Date(now);
    newReleaseSince.setDate(newReleaseSince.getDate() - newReleaseThresholdDays);

    try {
        const data = await fetchWithRetry(eolJsonUrl);
        for (const release of data) {
            core.info(`Checking release: ${JSON.stringify(release)}`);
            await checkEoL(release, now, eolLookbackDate);
            await checkNewRelease(release, now, newReleaseSince);
        }
    } catch (err) {
        core.error(`Error checking EoL/NewReleases for ${languageName}: ${err.message}`);
        const yw = getYearWeek(new Date());
        const errorTitle = `[CI ERROR] EoL/NewRelease check for ${languageName} in ${yw}`;
        const runUrl = `https://github.com/${context.repo.owner}/${context.repo.repo}/actions/runs/${context.runId}`;
        const body = dedent(`
            The automated check for EoL and new releases failed (retried ${retryCount} times).
            **Error**: ${err.message}
            **Action URL**: [View job log here](${runUrl})
            Please investigate (network issues, invalid JSON, etc.) and fix it to monitor EOL site automatically.
            `);
        await createIssueIfNotExists(errorTitle, body, ['keep']);
        core.setFailed(err.message);
    }
};
