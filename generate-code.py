import os
import subprocess

def run_command(command):
    output = subprocess.check_output(command, shell=True)
    return output.decode('utf-8').strip()

import fileinput

def replace_text_in_files(dir_path: str, text_to_search: str, text_to_replace: str):
    for foldername, subfolders, filenames in os.walk(dir_path):
        for filename in filenames:
            file_path = os.path.join(foldername, filename)
            with fileinput.FileInput(file_path, inplace=True) as file:
                for line in file:
                    print(line.replace(text_to_search, text_to_replace), end='')


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

    ##
    ## TODO(v4): Delete this workaround in v4 and use operation-id in line-openapi.
    ## This workaround is to avoid breaking change in v3.

    ## POST   /liff/v1/apps          <- addLIFFApp
    ## GET    /liff/v1/apps          <- getAllLIFFApps
    ## PUT    /liff/v1/apps/{liffId} <- updateLIFFApp
    ## DELETE /liff/v1/apps/{liffId} <- deleteLIFFApp

    replace_text_in_files('./linebot/v3/liff/api', 'get_all_liff_apps(', 'liff_v1_apps_get(')
    replace_text_in_files('./linebot/v3/liff/api', 'get_all_liff_apps  ', 'liff_v1_apps_get  ')
    replace_text_in_files('./linebot/v3/liff/api', 'method get_all_liff_apps', 'method liff_v1_apps_get')
    replace_text_in_files('./linebot/v3/liff/api', 'get_all_liff_apps_with_http_info(', 'liff_v1_apps_get_with_http_info(')
    replace_text_in_files('./linebot/v3/liff/api', 'get_all_liff_apps_with_http_info method', 'liff_v1_apps_get_with_http_info method')
    replace_text_in_files('./linebot/v3/liff/docs', 'get_all_liff_apps(', 'liff_v1_apps_get(')
    replace_text_in_files('./linebot/v3/liff/docs', 'get_all_liff_apps**', 'liff_v1_apps_get**')
    replace_text_in_files('./linebot/v3/liff/docs', 'get_all_liff_apps:', 'liff_v1_apps_get:')
    replace_text_in_files('./linebot/v3/liff/docs', 'get_all_liff_apps)', 'liff_v1_apps_get)')

    replace_text_in_files('./linebot/v3/liff/api', 'add_liff_app(', 'liff_v1_apps_post(')
    replace_text_in_files('./linebot/v3/liff/api', 'add_liff_app  ', 'liff_v1_apps_post  ')
    replace_text_in_files('./linebot/v3/liff/api', 'method add_liff_app', 'method liff_v1_apps_post')
    replace_text_in_files('./linebot/v3/liff/api', 'add_liff_app_with_http_info(', 'liff_v1_apps_post_with_http_info(')
    replace_text_in_files('./linebot/v3/liff/api', 'add_liff_app_with_http_info method', 'liff_v1_apps_post_with_http_info method')
    replace_text_in_files('./linebot/v3/liff/docs', 'add_liff_app(', 'liff_v1_apps_post(')
    replace_text_in_files('./linebot/v3/liff/docs', 'add_liff_app**', 'liff_v1_apps_post**')
    replace_text_in_files('./linebot/v3/liff/docs', 'add_liff_app:', 'liff_v1_apps_post:')
    replace_text_in_files('./linebot/v3/liff/docs', 'add_liff_app)', 'liff_v1_apps_post)')

    replace_text_in_files('./linebot/v3/liff/api', 'update_liff_app(', 'liff_v1_apps_liff_id_put(')
    replace_text_in_files('./linebot/v3/liff/api', 'update_liff_app  ', 'liff_v1_apps_liff_id_put  ')
    replace_text_in_files('./linebot/v3/liff/api', 'method update_liff_app', 'method liff_v1_apps_liff_id_put')
    replace_text_in_files('./linebot/v3/liff/api', 'update_liff_app_with_http_info(', 'liff_v1_apps_liff_id_put_with_http_info(')
    replace_text_in_files('./linebot/v3/liff/api', 'update_liff_app_with_http_info method', 'liff_v1_apps_liff_id_put_with_http_info method')
    replace_text_in_files('./linebot/v3/liff/docs', 'update_liff_app(', 'liff_v1_apps_liff_id_put(')
    replace_text_in_files('./linebot/v3/liff/docs', 'update_liff_app**', 'liff_v1_apps_liff_id_put**')
    replace_text_in_files('./linebot/v3/liff/docs', 'update_liff_app:', 'liff_v1_apps_liff_id_put:')
    replace_text_in_files('./linebot/v3/liff/docs', 'update_liff_app)', 'liff_v1_apps_liff_id_put)')

    replace_text_in_files('./linebot/v3/liff/api', 'delete_liff_app(', 'liff_v1_apps_liff_id_delete(')
    replace_text_in_files('./linebot/v3/liff/api', 'delete_liff_app  ', 'liff_v1_apps_liff_id_delete  ')
    replace_text_in_files('./linebot/v3/liff/api', 'method delete_liff_app', 'method liff_v1_apps_liff_id_delete')
    replace_text_in_files('./linebot/v3/liff/api', 'delete_liff_app_with_http_info(', 'liff_v1_apps_liff_id_delete_with_http_info(')
    replace_text_in_files('./linebot/v3/liff/api', 'delete_liff_app_with_http_info method', 'liff_v1_apps_liff_id_delete_with_http_info method')
    replace_text_in_files('./linebot/v3/liff/docs', 'delete_liff_app(', 'liff_v1_apps_liff_id_delete(')
    replace_text_in_files('./linebot/v3/liff/docs', 'delete_liff_app**', 'liff_v1_apps_liff_id_delete**')
    replace_text_in_files('./linebot/v3/liff/docs', 'delete_liff_app:', 'liff_v1_apps_liff_id_delete:')
    replace_text_in_files('./linebot/v3/liff/docs', 'delete_liff_app)', 'liff_v1_apps_liff_id_delete)')


if __name__ == "__main__":
    main()
