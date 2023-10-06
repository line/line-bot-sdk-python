import os
import subprocess
import sys

def run_command(command):
    proc = subprocess.run(command, shell=True, text=True, capture_output=True)

    if len(proc.stderr) != 0:
        print("\n\nSTDERR:\n\n")
        print(proc.stderr)
        print("\n\n")

    if proc.returncode != 0:
        print("\n\nSTDOUT:\n\n")
        print(proc.stdout)
        print(f"\n\nCommand '{command}' returned non-zero exit status {proc.returncode}.")
        sys.exit(1)

    return proc.stdout.strip()


def rewrite_liff_function_name_backward_compats():
    for fname in ['liff.py', 'async_liff.py']:
        with open(f'linebot/v3/liff/api/{fname}', 'a') as fp:
             fp.write("\n\n")
             for (orig, cur) in [('liff_v1_apps_get', 'get_all_liff_apps'),
                                 ('liff_v1_apps_get_with_http_info', 'get_all_liff_apps_with_http_info'),
                                 ('liff_v1_apps_post', 'add_liff_app'),
                                 ('liff_v1_apps_post_with_http_info', 'add_liff_app_with_http_info'),
                                 ('liff_v1_apps_liff_id_put', 'update_liff_app'),
                                 ('liff_v1_apps_liff_id_put_with_http_info', 'update_liff_app_with_http_info'),
                                 ('liff_v1_apps_liff_id_delete', 'delete_liff_app'),
                                 ('liff_v1_apps_liff_id_delete_with_http_info', 'delete_liff_app_with_http_info')]:
                 fp.write(f"\n")
                 fp.write(f"    def {orig}(self, *args, **kwargs):\n")
                 fp.write(f"        import warnings\n")
                 fp.write(f"        warnings.warn('{orig} was deprecated. use {cur} instead.', DeprecationWarning)\n")
                 fp.write(f"        return self.{cur}(*args, **kwargs)\n")

def main():

    os.chdir("generator")
    run_command('mvn package -DskipTests=true')
    os.chdir("..")

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
                    -i line-openapi/{sourceYaml}
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


    ## TODO(v4): Delete this workaround in v4. This workaround keeps backward compatibility.
    rewrite_liff_function_name_backward_compats()


if __name__ == "__main__":
    main()
