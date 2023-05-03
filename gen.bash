pushd generator
mvn package -DskipTests=true

popd

rm -rf linebot/messaging

java -cp ./tools/openapi-generator-cli.jar:./generator/target/python-nextgen-custom-client-openapi-generator-1.0.0.jar org.openapitools.codegen.OpenAPIGenerator generate \
-g python-nextgen-custom-client \
-i ./line-openapi/messaging-api.yml \
-o . \
--package-name linebot.messaging \
--additional-properties=excludeText=true \
--additional-properties=generateSourceCodeOnly=true \
--global-property debugModels=true > log.txt
