import os
import subprocess
import fnmatch
from typing import List, Tuple

def run_command(command):
    output = subprocess.check_output(command, shell=True)
    return output.decode('utf-8').strip()

def replace_in_file(file_path: str, replacements: List[Tuple[str, str]]):
    with open(file_path, 'r') as file:
        filedata = file.read()
    for k, v in replacements:
        filedata = filedata.replace(k, v)
    with open(file_path, 'w') as file:
        file.write(filedata)

def replace_in_files(directory: str, replacements: List[Tuple[str, str]]):
    for path, dirs, files in os.walk(directory):
        for filename in fnmatch.filter(files, "*"):
            file_path = os.path.join(path, filename)
            replace_in_file(file_path, replacements)

def replace_in_files_by_keyword(directory: str, wrong_function_name: str, original_function_name: str, prefix: List[str], suffix: List[str]):
    replacements = []
    for x in prefix:
        replacements.append((x + wrong_function_name, x + original_function_name))
    for x in suffix:
        replacements.append((wrong_function_name + x, original_function_name + x))
    replace_in_files(directory, replacements)

def replace_liff_function_name(wrong_function_name: str, original_function_name: str):
    replace_in_files_by_keyword('./linebot/v3/liff/api', wrong_function_name, original_function_name, ['method '], ['(', '  ', '_with_http_info(', '_with_http_info method'])
    replace_in_files_by_keyword('./linebot/v3/liff/docs', wrong_function_name, original_function_name, [], ['(', '**', ':', ')'])


def main():

    os.chdir("generator")
    run_command('mvn package -DskipTests=true')
    os.chdir("..")

    package_version = run_command("grep '__version__ =' linebot/__about__.py | awk -F\"'\" '{print $2}'")

    components = [
        {"sourceYaml": "channel-access-token.yml", "modelPackage": "linebot.v3.oauth"},
        {"sourceYaml": "insight.yml", "modelPackage": "linebot.v3.insight"},
        {"sourceYaml": "liff.yml", "modelPackage": "linebot.v3.liff"},
        {"sourceYaml": "manage-audience.yml", "modelPackage": "linebot.v3.audience"},
        {"sourceYaml": "messaging-api.yml", "modelPackage": "linebot.v3.messaging"},
        {"sourceYaml": "module-attach.yml", "modelPackage": "linebot.v3.moduleattach"},
        {"sourceYaml": "module.yml", "modelPackage": "linebot.v3.module"},
        {"sourceYaml": "shop.yml", "modelPackage": "linebot.v3.shop"},
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
    modelPackage = "linebot.v3.webhooks"
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


    ## TODO(v4): Delete this workaround in v4 and use operation-id in line-openapi.
    ## This workaround is to avoid breaking change in v3.

    ## GET    /liff/v1/apps          <- getAllLIFFApps
    replace_liff_function_name('get_all_liff_apps', 'liff_v1_apps_get')
    ## POST   /liff/v1/apps          <- addLIFFApp
    replace_liff_function_name('add_liff_app', 'liff_v1_apps_post')
    ## PUT    /liff/v1/apps/{liffId} <- updateLIFFApp
    replace_liff_function_name('update_liff_app', 'liff_v1_apps_liff_id_put')
    ## DELETE /liff/v1/apps/{liffId} <- deleteLIFFApp
    replace_liff_function_name('delete_liff_app', 'liff_v1_apps_liff_id_delete')


if __name__ == "__main__":
    main()
