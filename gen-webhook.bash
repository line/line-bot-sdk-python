pushd generator
mvn package -DskipTests=true

popd

rm -rf linebot/webhook

java -cp ./tools/openapi-generator-cli.jar:./generator/target/python-nextgen-custom-client-openapi-generator-1.0.0.jar org.openapitools.codegen.OpenAPIGenerator generate \
-g python-nextgen-custom-client \
-i ./line-openapi/webhook.yml \
-o . \
--package-name linebot.webhook \
--global-property models,modelDocs=false \
--global-property debugModels=true > log.txt
