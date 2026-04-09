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


def add_stateless_channel_token_wrappers():
    for fname in ['channel_access_token.py', 'async_channel_access_token.py']:
        filepath = f'linebot/v3/oauth/api/{fname}'

        # Inject deprecation notes into original methods' docstrings
        with open(filepath, 'r') as fp:
            lines = fp.readlines()

        new_lines = []
        i = 0
        while i < len(lines):
            new_lines.append(lines[i])
            for base_method in ['issue_stateless_channel_token_with_http_info',
                                'issue_stateless_channel_token']:
                if f'def {base_method}(self' in lines[i] and i + 1 < len(lines) and '"""' in lines[i + 1]:
                    # Next line: docstring title
                    i += 1
                    new_lines.append(lines[i])
                    # Next line: blank line
                    i += 1
                    new_lines.append(lines[i])
                    # Insert deprecation note
                    new_lines.append(f'        .. deprecated::\n')
                    new_lines.append(f'            Use :func:`{base_method}_by_jwt_assertion` or\n')
                    new_lines.append(f'            :func:`{base_method}_by_client_secret` instead.\n')
                    new_lines.append('\n')
                    break
            i += 1

        with open(filepath, 'w') as fp:
            fp.writelines(new_lines)

        # Append wrapper methods with docstrings
        with open(filepath, 'a') as fp:
            for base_method in ['issue_stateless_channel_token',
                                'issue_stateless_channel_token_with_http_info']:
                if base_method == 'issue_stateless_channel_token':
                    rtype = 'IssueStatelessChannelAccessTokenResponse'
                else:
                    rtype = 'ApiResponse'

                fp.write("\n")
                fp.write(f"    def {base_method}_by_jwt_assertion(self, client_assertion, **kwargs):\n")
                fp.write(f'        """Issue a stateless channel access token using a JSON Web Token (JWT).\n')
                fp.write(f'\n')
                fp.write(f'        :param str client_assertion: A JSON Web Token the client needs to create and sign with the private key of the Assertion Signing Key.\n')
                fp.write(f'        :return: Returns the result object.\n')
                fp.write(f'        :rtype: {rtype}\n')
                fp.write(f'        """\n')
                fp.write(f"        return self.{base_method}(\n")
                fp.write("            grant_type='client_credentials',\n")
                fp.write("            client_assertion_type='urn:ietf:params:oauth:client-assertion-type:jwt-bearer',\n")
                fp.write("            client_assertion=client_assertion,\n")
                fp.write("            client_id='',\n")
                fp.write("            client_secret='',\n")
                fp.write("            **kwargs,\n")
                fp.write("        )\n")
                fp.write("\n")
                fp.write(f"    def {base_method}_by_client_secret(self, client_id, client_secret, **kwargs):\n")
                fp.write(f'        """Issue a stateless channel access token using client ID and client secret.\n')
                fp.write(f'\n')
                fp.write(f'        :param str client_id: Channel ID.\n')
                fp.write(f'        :param str client_secret: Channel secret.\n')
                fp.write(f'        :return: Returns the result object.\n')
                fp.write(f'        :rtype: {rtype}\n')
                fp.write(f'        """\n')
                fp.write(f"        return self.{base_method}(\n")
                fp.write("            grant_type='client_credentials',\n")
                fp.write("            client_assertion_type='',\n")
                fp.write("            client_assertion='',\n")
                fp.write("            client_id=client_id,\n")
                fp.write("            client_secret=client_secret,\n")
                fp.write("            **kwargs,\n")
                fp.write("        )\n")


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


    add_stateless_channel_token_wrappers()

    ## TODO(v4): Delete this workaround in v4. This workaround keeps backward compatibility.
    rewrite_liff_function_name_backward_compats()

    run_command('python3 tools/generate_unified_client.py')


if __name__ == "__main__":
    main()
