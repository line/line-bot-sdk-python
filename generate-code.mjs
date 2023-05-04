async function main() {

    cd("generator");
    await $`mvn package -DskipTests=true`;
    cd("..");


    for (const components of [
        { SRCYML: "channel-access-token.yml", modelPackage: "linebot.oauth" },
        { SRCYML: "insight.yml", modelPackage: "linebot.insight" },
        { SRCYML: "liff.yml", modelPackage: "linebot.liff" },
        { SRCYML: "manage-audience.yml", modelPackage: "linebot.audience" },
        { SRCYML: "messaging-api.yml", modelPackage: "linebot.messaging" },
        { SRCYML: "module-attach.yml", modelPackage: "linebot.moduleattach" },
        { SRCYML: "module.yml", modelPackage: "linebot.module" },
        { SRCYML: "shop.yml", modelPackage: "linebot.shop" },
    ]) {
        const { SRCYML, modelPackage } = components;

        await $`rm -rf ${modelPackage.replace(".", "/")}/`;

        await $`java \\
                -cp ./tools/openapi-generator-cli.jar:./generator/target/python-nextgen-custom-client-openapi-generator-1.0.0.jar \\
                org.openapitools.codegen.OpenAPIGenerator \\
                generate \\
                --group-id com.linecorp.bot.model \\
                --package-name com.linecorp.bot.model \\
                -g python-nextgen-custom-client \\
                -o . \\
                --global-property modelDocs=false \\
                --additional-properties=excludeText=true \\
                --additional-properties=generateSourceCodeOnly=true \\
                --package-name ${modelPackage} \\
                -i line-openapi/${SRCYML}
              `;
    }

    {
        // webhook only model
        // TODO: __init__.py is deleted if apis=false. Fix it.
        const SRCYML = "webhook.yml"
        const modelPackage = "linebot.webhooks"
        await $`rm -rf ${modelPackage.replace(".", "/")}/`;
        await $`java \\
                -cp ./tools/openapi-generator-cli.jar:./generator/target/python-nextgen-custom-client-openapi-generator-1.0.0.jar \\
                org.openapitools.codegen.OpenAPIGenerator \\
                generate \\
                --group-id com.linecorp.bot.model \\
                --package-name com.linecorp.bot.model \\
                -g python-nextgen-custom-client \\
                -o . \\
                --global-property modelDocs=false,apiDocs=false \\
                --additional-properties=excludeText=true \\
                --additional-properties=generateSourceCodeOnly=true \\
                --package-name ${modelPackage} \\
                -i line-openapi/${SRCYML}
              `;
    }
}

await main();
