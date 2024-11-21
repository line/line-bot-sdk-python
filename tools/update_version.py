import sys
import re
import subprocess

def update_and_verify_version(new_version):
    file_path = 'linebot/__about__.py'

    # Update version
    with open(file_path, 'r') as file:
        content = file.read()

    new_content = re.sub(
        r"__version__ = '.*?'",
        f"__version__ = '{new_version}'",
        content
    )

    with open(file_path, 'w') as file:
        file.write(new_content)

    print(f"Updated version to {new_version} in {file_path}")

    # verify version
    match = re.search(r"__version__ = '(.*?)'", new_content)
    if not match:
        raise ValueError("Version string not found in the file.")

    actual_version = match.group(1)
    if actual_version != new_version:
        raise ValueError(f"Version mismatch: expected {new_version}, found {actual_version}")

    print(f"Version verified: {actual_version}")

    # diff check just in case
    try:
        result = subprocess.run(['git', 'diff', '--numstat', file_path], capture_output=True, text=True, check=True)
        changed_lines = result.stdout.strip().split('\n')
        added_lines = 0
        deleted_lines = 0

        for line in changed_lines:
            added, deleted = map(int, line.split('\t')[:2])
            added_lines += added
            deleted_lines += deleted

        if added_lines != 1 or deleted_lines != 1:
            raise ValueError(f"Unexpected number of changed lines: expected 1 added and 1 deleted, found {added_lines} added and {deleted_lines} deleted")

        print('Git diff verification passed: 1 line added and 1 line deleted.')

    except subprocess.CalledProcessError as e:
        print(f"Error during git diff verification: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python update_and_verify_version.py <new_version>")
        sys.exit(1)

    new_version = sys.argv[1]

    try:
        update_and_verify_version(new_version)
    except ValueError as e:
        print(e)
        sys.exit(1)
