import os
import subprocess

def run_command(command):
    output = subprocess.check_output(command, shell=True)
    return output.decode('utf-8').strip()

def main():

    os.chdir("generator")
    run_command('mvn package -DskipTests=true')
    os.chdir("..")

    package_version = run_command("grep '__version__ =' linebot/__about__.py | awk -F\"'\" '{print $2}'")

    components = [
        {"sourceYaml": "channel-access-token.yml", "modelPackage": "linebot.oauth"},
        {"sourceYaml": "insight.yml", "modelPackage": "linebot.insight"},
        {"sourceYaml": "liff.yml", "modelPackage": "linebot.liff"},
        {"sourceYaml": "manage-audience.yml", "modelPackage": "linebot.audience"},
        {"sourceYaml": "messaging-api.yml", "modelPackage": "linebot.messaging"},
        {"sourceYaml": "module-attach.yml", "modelPackage": "linebot.moduleattach"},
        {"sourceYaml": "module.yml", "modelPackage": "linebot.module"},
        {"sourceYaml": "shop.yml", "modelPackage": "linebot.shop"},
    ]

    for component in components:
        sourceYaml = component['sourceYaml']
        modelPackage = component['modelPackage']
        modelPackagePath = modelPackage.replace(".", "/")

        run_command(f'rm -rf {modelPackagePath}/')

        command = f'''java \\
                    -cp ./tools/openapi-generator-cli.jar:./generator/target/python-nextgen-custom-client-openapi-generator-1.0.0.jar \\
                    org.openapitools.codegen.OpenAPIGenerator \\
                    generate \\
                    -g python-nextgen-custom-client \\
                    -o . \\
                    --global-property modelDocs=false \\
                    --additional-properties=excludeText=true \\
                    --additional-properties=generateSourceCodeOnly=true \\
                    --package-name {modelPackage} \\
                    -i line-openapi/{sourceYaml} \\
                    --additional-properties=packageVersion={package_version}
                  '''
        run_command(command)

    ## webhook requires only models.
    ## TODO: We'd like to specify apis=false but __init__.py is deleted. Fix it.
    sourceYaml = "webhook.yml"
    modelPackage = "linebot.webhooks"
    modelPackagePath = modelPackage.replace(".", "/")

    run_command(f'rm -rf {modelPackagePath}/')

    command = f'''java \\
                -cp ./tools/openapi-generator-cli.jar:./generator/target/python-nextgen-custom-client-openapi-generator-1.0.0.jar \\
                org.openapitools.codegen.OpenAPIGenerator \\
                generate \\
                -g python-nextgen-custom-client \\
                -o . \\
                --global-property modelDocs=false,apiDocs=false \\
                --additional-properties=excludeText=true \\
                --additional-properties=generateSourceCodeOnly=true \\
                --package-name {modelPackage} \\
                -i line-openapi/{sourceYaml}
              '''
    run_command(command)

if __name__ == "__main__":
    main()
