/*
 * Copyright 2018 OpenAPI-Generator Contributors (https://openapi-generator.tech)
 * Copyright 2018 SmartBear Software
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     https://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package line.bot.generator;

import org.apache.commons.lang3.StringUtils;
import org.openapitools.codegen.*;
import org.openapitools.codegen.languages.PythonPydanticV1ClientCodegen;
import org.openapitools.codegen.model.ModelMap;
import org.openapitools.codegen.model.ModelsMap;
import org.openapitools.codegen.model.OperationMap;
import org.openapitools.codegen.model.OperationsMap;
import org.openapitools.codegen.utils.ModelUtils;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.util.*;

import static org.openapitools.codegen.utils.StringUtils.camelize;
import static org.openapitools.codegen.utils.StringUtils.underscore;

public class PythonNextgenCustomClientGenerator extends PythonPydanticV1ClientCodegen implements CodegenConfig {
    private final Logger LOGGER = LoggerFactory.getLogger(PythonNextgenCustomClientGenerator.class);

    // Upstream codegenModelMap / circularImports are private, so we keep our own copies.
    private final HashMap<String, HashSet<String>> lineCircularImports = new HashMap<>();
    private final HashMap<String, CodegenModel> lineCodegenModelMap = new HashMap<>();

    public PythonNextgenCustomClientGenerator() {
        super();

        embeddedTemplateDir = templateDir = "python-nextgen-custom-client";

        // Replace upstream .mustache templates with .pebble; emit both sync and async APIs.
        apiTemplateFiles.clear();
        apiTemplateFiles.put("api.pebble", ".py");
        apiTemplateFiles.put("asyncio/async_api.pebble", ".py");

        modelTemplateFiles.clear();
        modelTemplateFiles.put("model.pebble", ".py");

        // Model docs are always disabled via --global-property modelDocs=false.
        modelDocTemplateFiles.clear();

        apiDocTemplateFiles.clear();
        apiDocTemplateFiles.put("api_doc.pebble", ".md");

        modelTestTemplateFiles.clear();
        apiTestTemplateFiles.clear();

        // Reserve pydantic keywords (schema/base64/json/date) on top of the Python reserved words.
        setReservedWordsLowerCase(
                Arrays.asList(
                        // pydantic keyword
                        "schema", "base64", "json",
                        "date",
                        // @property
                        "property",
                        // python reserved words
                        "and", "del", "from", "not", "while", "as", "elif", "global", "or", "with",
                        "assert", "else", "if", "pass", "yield", "break", "except", "import",
                        "print", "class", "exec", "in", "raise", "continue", "finally", "is",
                        "return", "def", "for", "lambda", "try", "self", "nonlocal", "None", "True",
                        "False", "async", "await"));
    }

    // Suppress AllOf.py models by disabling the upstream inline model resolver.
    @Override
    public boolean getUseInlineModelResolver() {
        return false;
    }

    @Override
    public void processOpts() {
        // Default excludeTests=true so the test __init__.py is not registered by super.
        if (!additionalProperties.containsKey(CodegenConstants.EXCLUDE_TESTS)) {
            additionalProperties.put(CodegenConstants.EXCLUDE_TESTS, "true");
        }

        super.processOpts();

        // Re-register only the supporting files we actually emit (generate-code.py
        // always runs with generateSourceCodeOnly=true, so setup.py / pyproject.toml /
        // tox.ini / requirements / .gitignore etc. are intentionally skipped).
        supportingFiles.clear();

        String modelPath = modelPackage.replace('.', java.io.File.separatorChar);
        String apiPath = apiPackage.replace('.', java.io.File.separatorChar);

        supportingFiles.add(new SupportingFile("README_onlypackage.pebble", "", packagePath() + "_README.md"));
        supportingFiles.add(new SupportingFile("configuration.pebble", packagePath(), "configuration.py"));
        supportingFiles.add(new SupportingFile("__init__package.pebble", packagePath(), "__init__.py"));
        supportingFiles.add(new SupportingFile("__init__model.pebble", modelPath, "__init__.py"));
        supportingFiles.add(new SupportingFile("__init__api.pebble", apiPath, "__init__.py"));

        // LINE OpenAPI has no HTTP signature scheme, so signing.py is not generated.

        // package name with dots gets directory structure
        String[] packageNameSplits = packageName.split("\\.");
        String currentPackagePath = "";
        for (int i = 0; i < packageNameSplits.length - 1; i++) {
            if (i > 0) {
                currentPackagePath = currentPackagePath + java.io.File.separatorChar;
            }
            currentPackagePath = currentPackagePath + packageNameSplits[i];
            supportingFiles.add(new SupportingFile("__init__.pebble", currentPackagePath, "__init__.py"));
        }

        supportingFiles.add(new SupportingFile("exceptions.pebble", packagePath(), "exceptions.py"));

        Boolean excludeTests = Boolean.valueOf(additionalProperties.get(CodegenConstants.EXCLUDE_TESTS).toString());
        if (Boolean.FALSE.equals(excludeTests)) {
            supportingFiles.add(new SupportingFile("__init__.pebble", "test", "__init__.py"));
        }

        // Emit sync and async api_client / REST in the same package.
        supportingFiles.add(new SupportingFile("api_client.pebble", packagePath(), "api_client.py"));
        supportingFiles.add(new SupportingFile("asyncio/api_client.pebble", packagePath(), "async_api_client.py"));

        supportingFiles.add(new SupportingFile("api_response.pebble", packagePath(), "api_response.py"));

        supportingFiles.add(new SupportingFile("rest.pebble", packagePath(), "rest.py"));
        supportingFiles.add(new SupportingFile("asyncio/rest.pebble", packagePath(), "async_rest.py"));
    }

    @Override
    public String getName() {
        return "python-nextgen-custom-client";
    }

    @Override
    public String getHelp() {
        return "Generates a Python client library.";
    }

    @Override
    public String generatorLanguageVersion() {
        return "3.10+";
    }

    // Keep existing class / file names by skipping the upstream "Api" suffix.
    @Override
    public String toApiName(String name) {
        return camelize(name);
    }

    // Files produced from asyncio templates get an "async_" prefix.
    @Override
    public String apiFilename(String templateName, String tag) {
        String result = super.apiFilename(templateName, tag);
        if (templateName.startsWith("async")) {
            int ix = result.lastIndexOf('/');
            result = result.substring(0, ix + 1) + "async_" + result.substring(ix + 1);
        }
        return result;
    }

    // Emit `from pydantic.v1 import ...` (instead of upstream's `from pydantic import ...`)
    // and omit the typing_extensions / postponed import machinery the upstream adds.
    @Override
    public OperationsMap postProcessOperationsWithModels(OperationsMap objs, List<ModelMap> allModels) {
        hasModelsToImport = false;
        TreeSet<String> typingImports = new TreeSet<>();
        TreeSet<String> pydanticImports = new TreeSet<>();
        TreeSet<String> datetimeImports = new TreeSet<>();
        TreeSet<String> modelImports = new TreeSet<>();

        OperationMap objectMap = objs.getOperations();
        List<CodegenOperation> operations = objectMap.getOperation();
        for (CodegenOperation operation : operations) {
            TreeSet<String> exampleImports = new TreeSet<>();
            List<CodegenParameter> params = operation.allParams;

            for (CodegenParameter param : params) {
                String typing = getPydanticType(param, typingImports, pydanticImports, datetimeImports, modelImports, exampleImports, null);
                List<String> fields = new ArrayList<>();
                String firstField = "";

                if (!param.required) {
                    firstField = "None";
                    typing = "Optional[" + typing + "]";
                    typingImports.add("Optional");
                } else {
                    firstField = "...";
                    if (param.isNullable) {
                        typing = "Optional[" + typing + "]";
                        typingImports.add("Optional");
                    }
                }

                if (!StringUtils.isEmpty(param.description)) {
                    fields.add(String.format(Locale.ROOT, "description=\"%s\"", param.description));
                }

                String fieldCustomization;
                if ("None".equals(firstField)) {
                    fieldCustomization = null;
                } else {
                    fieldCustomization = firstField;
                }

                if (!fields.isEmpty()) {
                    if (fieldCustomization != null) {
                        fields.add(0, fieldCustomization);
                    }
                    pydanticImports.add("Field");
                    fieldCustomization = String.format(Locale.ROOT, "Field(%s)", StringUtils.join(fields, ", "));
                } else {
                    fieldCustomization = "Field()";
                }

                if ("Field()".equals(fieldCustomization)) {
                    param.vendorExtensions.put("x-py-typing", typing);
                } else {
                    param.vendorExtensions.put("x-py-typing", String.format(Locale.ROOT, "Annotated[%s, %s]", typing, fieldCustomization));
                }
            }

            if (!StringUtils.isEmpty(operation.returnType)) {
                String typing = getPydanticType(operation.returnProperty, typingImports,
                        new TreeSet<>(), datetimeImports, modelImports, exampleImports, null);
            }

            if (!exampleImports.isEmpty()) {
                List<String> imports = new ArrayList<>();
                for (String exampleImport : exampleImports) {
                    imports.add("from " + packageName + ".models." + underscore(exampleImport) + " import " + exampleImport);
                }
                operation.vendorExtensions.put("x-py-example-import", imports);
            }
        }

        List<Map<String, String>> newImports = new ArrayList<>();

        if (!datetimeImports.isEmpty()) {
            Map<String, String> item = new HashMap<>();
            item.put("import", String.format(Locale.ROOT, "from datetime import %s\n", StringUtils.join(datetimeImports, ", ")));
            newImports.add(item);
        }

        if (!pydanticImports.isEmpty()) {
            Map<String, String> item = new HashMap<>();
            item.put("import", String.format(Locale.ROOT, "from pydantic.v1 import %s\n", StringUtils.join(pydanticImports, ", ")));
            newImports.add(item);
        }

        if (!typingImports.isEmpty()) {
            Map<String, String> item = new HashMap<>();
            item.put("import", String.format(Locale.ROOT, "from typing import %s\n", StringUtils.join(typingImports, ", ")));
            newImports.add(item);
        }

        if (!modelImports.isEmpty()) {
            for (String modelImport : modelImports) {
                Map<String, String> item = new HashMap<>();
                item.put("import", "from " + packageName + ".models." + underscore(modelImport) + " import " + modelImport);
                newImports.add(item);
            }
        }

        objs.setImports(newImports);
        return objs;
    }

    // Re-run our own postProcessModelsMap to emit pydantic.v1 imports and the
    // discriminator x-py-type-name extension (upstream's is private).
    @Override
    public Map<String, ModelsMap> postProcessAllModels(Map<String, ModelsMap> objs) {
        final Map<String, ModelsMap> processed = super.postProcessAllModels(objs);

        for (Map.Entry<String, ModelsMap> entry : objs.entrySet()) {
            CodegenModel cm = ModelUtils.getModelByName(entry.getKey(), objs);
            lineCodegenModelMap.put(cm.classname, ModelUtils.getModelByName(entry.getKey(), objs));
        }

        for (String m : lineCodegenModelMap.keySet()) {
            createLineImportMapOfSet(m, lineCodegenModelMap);
        }

        for (Map.Entry<String, ModelsMap> entry : processed.entrySet()) {
            entry.setValue(postProcessModelsMap(entry.getValue()));
        }

        return processed;
    }

    private void createLineImportMapOfSet(String modelName, Map<String, CodegenModel> codegenModelMap) {
        HashSet<String> imports = new HashSet<>();
        lineCircularImports.put(modelName, imports);

        CodegenModel cm = codegenModelMap.get(modelName);

        if (cm == null) {
            LOGGER.warn("Failed to lookup model in createLineImportMapOfSet: " + modelName);
            return;
        }

        List<CodegenProperty> codegenProperties;
        if (cm.oneOf != null && !cm.oneOf.isEmpty()) {
            codegenProperties = cm.getComposedSchemas().getOneOf();
        } else if (cm.anyOf != null && !cm.anyOf.isEmpty()) {
            codegenProperties = cm.getComposedSchemas().getAnyOf();
        } else {
            codegenProperties = cm.vars;
        }

        for (CodegenProperty cp : codegenProperties) {
            String modelNameFromDataType = getLineModelNameFromDataType(cp);
            if (modelNameFromDataType != null) {
                imports.add(modelNameFromDataType);
                updateLineImportsFromCodegenModel(modelNameFromDataType, codegenModelMap.get(modelNameFromDataType), imports);
            }
        }
    }

    private void updateLineImportsFromCodegenModel(String modelName, CodegenModel cm, Set<String> imports) {
        if (cm == null) {
            LOGGER.warn("Failed to lookup model in createLineImportMapOfSet " + modelName);
            return;
        }

        List<CodegenProperty> codegenProperties;
        if (cm.oneOf != null && !cm.oneOf.isEmpty()) {
            codegenProperties = cm.getComposedSchemas().getOneOf();
        } else if (cm.anyOf != null && !cm.anyOf.isEmpty()) {
            codegenProperties = cm.getComposedSchemas().getAnyOf();
        } else {
            codegenProperties = cm.vars;
        }

        for (CodegenProperty cp : codegenProperties) {
            String modelNameFromDataType = getLineModelNameFromDataType(cp);
            if (modelNameFromDataType != null) {
                if (modelName.equals(modelNameFromDataType)) {
                    continue;
                } else if (imports.contains(modelNameFromDataType)) {
                    continue;
                } else {
                    imports.add(modelNameFromDataType);
                    updateLineImportsFromCodegenModel(modelNameFromDataType, lineCodegenModelMap.get(modelNameFromDataType), imports);
                }
            }
        }
    }

    private String getLineModelNameFromDataType(CodegenProperty cp) {
        if (cp.isArray) {
            return getLineModelNameFromDataType(cp.items);
        } else if (cp.isMap) {
            return getLineModelNameFromDataType(cp.items);
        } else if (!cp.isPrimitiveType || cp.isModel) {
            return cp.dataType;
        } else {
            return null;
        }
    }

    private ModelsMap postProcessModelsMap(ModelsMap objs) {
        objs = postProcessModelsEnum(objs);

        TreeSet<String> typingImports = new TreeSet<>();
        TreeSet<String> pydanticImports = new TreeSet<>();
        TreeSet<String> datetimeImports = new TreeSet<>();
        TreeSet<String> modelImports = new TreeSet<>();

        for (ModelMap m : objs.getModels()) {
            TreeSet<String> exampleImports = new TreeSet<>();
            List<String> readOnlyFields = new ArrayList<>();
            hasModelsToImport = false;
            int property_count = 1;
            typingImports.clear();
            pydanticImports.clear();
            datetimeImports.clear();

            CodegenModel model = m.getModel();

            if (model.getComposedSchemas() != null && model.getComposedSchemas().getOneOf() != null
                    && !model.getComposedSchemas().getOneOf().isEmpty()) {
                int index = 0;
                List<CodegenProperty> oneOfs = model.getComposedSchemas().getOneOf();
                for (CodegenProperty oneOf : oneOfs) {
                    if ("none_type".equals(oneOf.dataType)) {
                        oneOfs.remove(index);
                        break;
                    }
                    index++;
                }
            }

            List<CodegenProperty> codegenProperties;
            if (!model.oneOf.isEmpty()) {
                codegenProperties = model.getComposedSchemas().getOneOf();
                typingImports.add("Any");
                typingImports.add("List");
                pydanticImports.add("Field");
                pydanticImports.add("StrictStr");
                pydanticImports.add("ValidationError");
                pydanticImports.add("validator");
            } else if (!model.anyOf.isEmpty()) {
                codegenProperties = model.getComposedSchemas().getAnyOf();
                pydanticImports.add("Field");
                pydanticImports.add("StrictStr");
                pydanticImports.add("ValidationError");
                pydanticImports.add("validator");
            } else {
                codegenProperties = model.vars;
                if (model.getDiscriminator() != null && model.getDiscriminator().getMappedModels() != null) {
                    typingImports.add("Union");
                }
            }

            for (CodegenProperty cp : codegenProperties) {
                String typing = getPydanticType(cp, typingImports, pydanticImports, datetimeImports, modelImports, exampleImports, model.classname);
                List<String> fields = new ArrayList<>();
                String firstField = "";

                if (cp.isReadOnly) {
                    readOnlyFields.add(cp.name);
                }

                if (!cp.required) {
                    firstField = "None";
                    typing = "Optional[" + typing + "]";
                    typingImports.add("Optional");
                } else {
                    firstField = "...";
                    if (cp.isNullable) {
                        typing = "Optional[" + typing + "]";
                        typingImports.add("Optional");
                    }
                }

                if (cp.baseName != null && !cp.baseName.equals(cp.name)) {
                    fields.add(String.format(Locale.ROOT, "alias=\"%s\"", cp.baseName));
                }

                if (!StringUtils.isEmpty(cp.description)) {
                    fields.add(String.format(Locale.ROOT, "description=\"%s\"", cp.description));
                }

                String fieldCustomization;
                if ("None".equals(firstField)) {
                    if (cp.defaultValue == null) {
                        fieldCustomization = "None";
                    } else {
                        if (cp.isArray || cp.isMap) {
                            fieldCustomization = "None";
                        } else {
                            fieldCustomization = cp.defaultValue;
                        }
                    }
                } else {
                    fieldCustomization = firstField;
                }

                if (!fields.isEmpty()) {
                    fields.add(0, fieldCustomization);
                    pydanticImports.add("Field");
                    fieldCustomization = String.format(Locale.ROOT, "Field(%s)", StringUtils.join(fields, ", "));
                }

                if ("...".equals(fieldCustomization)) {
                    pydanticImports.add("Field");
                    fieldCustomization = "Field(...)";
                }

                cp.vendorExtensions.put("x-py-typing", typing + " = " + fieldCustomization);

                if (!model.oneOf.isEmpty()) {
                    cp.vendorExtensions.put("x-py-name", String.format(Locale.ROOT, "oneof_schema_%d_validator", property_count++));
                } else if (!model.anyOf.isEmpty()) {
                    cp.vendorExtensions.put("x-py-name", String.format(Locale.ROOT, "anyof_schema_%d_validator", property_count++));
                }
            }

            if (!StringUtils.isEmpty(model.parent)) {
                modelImports.add(model.parent);
                // Extension for discriminator
                modelImports.addAll(model.imports);

                String mappedTypeName = mappingName(model.name, model.parentModel.getDiscriminator());
                model.vendorExtensions.put("x-py-type-name", mappedTypeName);
            } else if (!model.isEnum) {
                pydanticImports.add("BaseModel");
            }

            if (model.isEnum) {
                for (Map<String, Object> enumVars : (List<Map<String, Object>>) model.getAllowableValues().get("enumVars")) {
                    if ((Boolean) enumVars.get("isString")) {
                        model.vendorExtensions.put("x-py-enum-type", "str");
                        enumVars.put("name", toEnumVariableName((String) enumVars.get("value"), "str"));
                    } else {
                        model.vendorExtensions.put("x-py-enum-type", "int");
                        enumVars.put("name", toEnumVariableName((String) enumVars.get("value"), "int"));
                    }
                }
            }

            model.getVendorExtensions().put("x-py-typing-imports", typingImports);
            model.getVendorExtensions().put("x-py-pydantic-imports", pydanticImports);
            model.getVendorExtensions().put("x-py-datetime-imports", datetimeImports);
            model.getVendorExtensions().put("x-py-readonly", readOnlyFields);

            if (!modelImports.isEmpty()) {
                Set<String> modelsToImport = new TreeSet<>();
                for (String modelImport : modelImports) {
                    if (modelImport.equals(model.classname)) {
                        continue;
                    }
                    modelsToImport.add("from " + packageName + ".models." + underscore(modelImport) + " import " + modelImport);
                }

                model.getVendorExtensions().put("x-py-model-imports", modelsToImport);
            }
        }

        return objs;
    }

    private String mappingName(String modelName, CodegenDiscriminator discriminator) {
        String valueToSearch = "#/components/schemas/" + modelName;
        return discriminator.getMapping().entrySet().stream()
                .filter(entry -> valueToSearch.equals(entry.getValue()))
                .map(Map.Entry::getKey)
                .findFirst()
                .orElseThrow(() -> new NoSuchElementException("Key not found (" + modelName + ") mapping (" + discriminator.getMapping() + ")"));
    }

    // Pydantic type resolver (CodegenParameter). The upstream version adds
    // postponedModelImports / postponedExampleImports arguments and emits Annotated
    // imports; we keep the original signature to stay on pydantic.v1 without
    // postponed imports.
    private String getPydanticType(CodegenParameter cp,
                                   Set<String> typingImports,
                                   Set<String> pydanticImports,
                                   Set<String> datetimeImports,
                                   Set<String> modelImports,
                                   Set<String> exampleImports,
                                   String classname) {
        if (cp == null) {
            LOGGER.warn("Codegen property is null (e.g. map/dict of undefined type). Default to typing.Any.");
            typingImports.add("Any");
            return "Any";
        }

        if (cp.isArray) {
            String constraints = "";
            if (cp.maxItems != null) {
                constraints += String.format(Locale.ROOT, ", max_items=%d", cp.maxItems);
            }
            if (cp.minItems != null) {
                constraints += String.format(Locale.ROOT, ", min_items=%d", cp.minItems);
            }
            if (cp.getUniqueItems()) {
                constraints += ", unique_items=True";
            }
            pydanticImports.add("conlist");
            return String.format(Locale.ROOT, "conlist(%s%s)",
                    getPydanticType(cp.items, typingImports, pydanticImports, datetimeImports, modelImports, exampleImports, classname),
                    constraints);
        } else if (cp.isMap) {
            typingImports.add("Dict");
            return String.format(Locale.ROOT, "Dict[str, %s]",
                    getPydanticType(cp.items, typingImports, pydanticImports, datetimeImports, modelImports, exampleImports, classname));
        } else if (cp.isString) {
            if (cp.hasValidation) {
                List<String> fieldCustomization = new ArrayList<>();
                fieldCustomization.add("strict=True");
                if (cp.getMaxLength() != null) {
                    fieldCustomization.add("max_length=" + cp.getMaxLength());
                }
                if (cp.getMinLength() != null) {
                    fieldCustomization.add("min_length=" + cp.getMinLength());
                }
                if (cp.getPattern() != null) {
                    pydanticImports.add("validator");
                }
                pydanticImports.add("constr");
                return String.format(Locale.ROOT, "constr(%s)", StringUtils.join(fieldCustomization, ", "));
            } else {
                if ("password".equals(cp.getFormat())) {
                    pydanticImports.add("SecretStr");
                    return "SecretStr";
                } else {
                    pydanticImports.add("StrictStr");
                    return "StrictStr";
                }
            }
        } else if (cp.isNumber || cp.isFloat || cp.isDouble) {
            if (cp.hasValidation) {
                List<String> fieldCustomization = new ArrayList<>();
                List<String> intFieldCustomization = new ArrayList<>();

                if (cp.getMaximum() != null) {
                    if (cp.getExclusiveMaximum()) {
                        fieldCustomization.add("lt=" + cp.getMaximum());
                        intFieldCustomization.add("lt=" + Math.ceil(Double.valueOf(cp.getMaximum())));
                    } else {
                        fieldCustomization.add("le=" + cp.getMaximum());
                        intFieldCustomization.add("le=" + Math.floor(Double.valueOf(cp.getMaximum())));
                    }
                }
                if (cp.getMinimum() != null) {
                    if (cp.getExclusiveMinimum()) {
                        fieldCustomization.add("gt=" + cp.getMinimum());
                        intFieldCustomization.add("gt=" + Math.floor(Double.valueOf(cp.getMinimum())));
                    } else {
                        fieldCustomization.add("ge=" + cp.getMinimum());
                        intFieldCustomization.add("ge=" + Math.ceil(Double.valueOf(cp.getMinimum())));
                    }
                }
                if (cp.getMultipleOf() != null) {
                    fieldCustomization.add("multiple_of=" + cp.getMultipleOf());
                }

                if ("Union[StrictFloat, StrictInt]".equals(mapNumberTo)) {
                    fieldCustomization.add("strict=True");
                    intFieldCustomization.add("strict=True");
                    pydanticImports.add("confloat");
                    pydanticImports.add("conint");
                    typingImports.add("Union");
                    return String.format(Locale.ROOT, "Union[%s(%s), %s(%s)]", "confloat",
                            StringUtils.join(fieldCustomization, ", "),
                            "conint",
                            StringUtils.join(intFieldCustomization, ", ")
                    );
                } else if ("StrictFloat".equals(mapNumberTo)) {
                    fieldCustomization.add("strict=True");
                    pydanticImports.add("confloat");
                    return String.format(Locale.ROOT, "%s(%s)", "confloat",
                            StringUtils.join(fieldCustomization, ", "));
                } else {
                    pydanticImports.add("confloat");
                    return String.format(Locale.ROOT, "%s(%s)", "confloat",
                            StringUtils.join(fieldCustomization, ", "));
                }
            } else {
                if ("Union[StrictFloat, StrictInt]".equals(mapNumberTo)) {
                    typingImports.add("Union");
                    pydanticImports.add("StrictFloat");
                    pydanticImports.add("StrictInt");
                    return "Union[StrictFloat, StrictInt]";
                } else if ("StrictFloat".equals(mapNumberTo)) {
                    pydanticImports.add("StrictFloat");
                    return "StrictFloat";
                } else {
                    return "float";
                }
            }
        } else if (cp.isInteger || cp.isLong || cp.isShort || cp.isUnboundedInteger) {
            if (cp.hasValidation) {
                List<String> fieldCustomization = new ArrayList<>();
                fieldCustomization.add("strict=True");
                if (cp.getMaximum() != null) {
                    if (cp.getExclusiveMaximum()) {
                        fieldCustomization.add("lt=" + cp.getMaximum());
                    } else {
                        fieldCustomization.add("le=" + cp.getMaximum());
                    }
                }
                if (cp.getMinimum() != null) {
                    if (cp.getExclusiveMinimum()) {
                        fieldCustomization.add("gt=" + cp.getMinimum());
                    } else {
                        fieldCustomization.add("ge=" + cp.getMinimum());
                    }
                }
                if (cp.getMultipleOf() != null) {
                    fieldCustomization.add("multiple_of=" + cp.getMultipleOf());
                }

                pydanticImports.add("conint");
                return String.format(Locale.ROOT, "%s(%s)", "conint",
                        StringUtils.join(fieldCustomization, ", "));
            } else {
                pydanticImports.add("StrictInt");
                return "StrictInt";
            }
        } else if (cp.isBinary || cp.isByteArray) {
            if (cp.hasValidation) {
                List<String> fieldCustomization = new ArrayList<>();
                fieldCustomization.add("strict=True");
                if (cp.getMinLength() != null) {
                    fieldCustomization.add("min_length=" + cp.getMinLength());
                }
                if (cp.getMaxLength() != null) {
                    fieldCustomization.add("max_length=" + cp.getMaxLength());
                }
                if (cp.getPattern() != null) {
                    pydanticImports.add("validator");
                }

                pydanticImports.add("conbytes");
                pydanticImports.add("constr");
                typingImports.add("Union");
                return String.format(Locale.ROOT, "Union[conbytes(%s), constr(%<s)]", StringUtils.join(fieldCustomization, ", "));
            } else {
                pydanticImports.add("StrictBytes");
                pydanticImports.add("StrictStr");
                typingImports.add("Union");
                return "Union[StrictBytes, StrictStr]";
            }
        } else if (cp.isBoolean) {
            pydanticImports.add("StrictBool");
            return "StrictBool";
        } else if (cp.isDecimal) {
            if (cp.hasValidation) {
                List<String> fieldCustomization = new ArrayList<>();
                fieldCustomization.add("strict=True");
                if (cp.getMaximum() != null) {
                    if (cp.getExclusiveMaximum()) {
                        fieldCustomization.add("gt=" + cp.getMaximum());
                    } else {
                        fieldCustomization.add("ge=" + cp.getMaximum());
                    }
                }
                if (cp.getMinimum() != null) {
                    if (cp.getExclusiveMinimum()) {
                        fieldCustomization.add("lt=" + cp.getMinimum());
                    } else {
                        fieldCustomization.add("le=" + cp.getMinimum());
                    }
                }
                if (cp.getMultipleOf() != null) {
                    fieldCustomization.add("multiple_of=" + cp.getMultipleOf());
                }
                pydanticImports.add("condecimal");
                return String.format(Locale.ROOT, "%s(%s)", "condecimal", StringUtils.join(fieldCustomization, ", "));
            } else {
                pydanticImports.add("condecimal");
                return "condecimal()";
            }
        } else if (cp.getIsAnyType()) {
            typingImports.add("Any");
            return "Any";
        } else if (cp.isDate || cp.isDateTime) {
            if (cp.isDate) {
                datetimeImports.add("date");
            }
            if (cp.isDateTime) {
                datetimeImports.add("datetime");
            }
            return cp.dataType;
        } else if (cp.isUuid) {
            return cp.dataType;
        } else if (cp.isFreeFormObject) {
            typingImports.add("Dict");
            typingImports.add("Any");
            return "Dict[str, Any]";
        } else if (!cp.isPrimitiveType) {
            hasModelsToImport = true;
            modelImports.add(cp.dataType);
            exampleImports.add(cp.dataType);
            return cp.dataType;
        } else if (cp.getContent() != null) {
            LinkedHashMap<String, CodegenMediaType> contents = cp.getContent();
            for (String key : contents.keySet()) {
                CodegenMediaType cmt = contents.get(key);
                if (cmt != null)
                    return getPydanticType(cmt.getSchema(), typingImports, pydanticImports, datetimeImports, modelImports, exampleImports, classname);
            }
            throw new RuntimeException("Error! Failed to process getPydanticType when getting the content: " + cp);
        } else {
            throw new RuntimeException("Error! Codegen Parameter not yet supported in getPydanticType: " + cp);
        }
    }

    // Pydantic type resolver (CodegenProperty).
    private String getPydanticType(CodegenProperty cp,
                                   Set<String> typingImports,
                                   Set<String> pydanticImports,
                                   Set<String> datetimeImports,
                                   Set<String> modelImports,
                                   Set<String> exampleImports,
                                   String classname) {
        if (cp == null) {
            LOGGER.warn("Codegen property is null (e.g. map/dict of undefined type). Default to typing.Any.");
            typingImports.add("Any");
            return "Any";
        }

        if (cp.isEnum) {
            pydanticImports.add("validator");
        }

        if (cp.isArray) {
            String constraints = "";
            if (cp.maxItems != null) {
                constraints += String.format(Locale.ROOT, ", max_items=%d", cp.maxItems);
            }
            if (cp.minItems != null) {
                constraints += String.format(Locale.ROOT, ", min_items=%d", cp.minItems);
            }
            if (cp.getUniqueItems()) {
                constraints += ", unique_items=True";
            }
            pydanticImports.add("conlist");
            typingImports.add("List");
            return String.format(Locale.ROOT, "conlist(%s%s)",
                    getPydanticType(cp.items, typingImports, pydanticImports, datetimeImports, modelImports, exampleImports, classname),
                    constraints);
        } else if (cp.isMap) {
            typingImports.add("Dict");
            return String.format(Locale.ROOT, "Dict[str, %s]", getPydanticType(cp.items, typingImports, pydanticImports, datetimeImports, modelImports, exampleImports, classname));
        } else if (cp.isString) {
            if (cp.hasValidation) {
                List<String> fieldCustomization = new ArrayList<>();
                fieldCustomization.add("strict=True");
                if (cp.getMaxLength() != null) {
                    fieldCustomization.add("max_length=" + cp.getMaxLength());
                }
                if (cp.getMinLength() != null) {
                    fieldCustomization.add("min_length=" + cp.getMinLength());
                }
                if (cp.getPattern() != null) {
                    pydanticImports.add("validator");
                }
                pydanticImports.add("constr");
                return String.format(Locale.ROOT, "constr(%s)", StringUtils.join(fieldCustomization, ", "));
            } else {
                if ("password".equals(cp.getFormat())) {
                    pydanticImports.add("SecretStr");
                    return "SecretStr";
                } else {
                    pydanticImports.add("StrictStr");
                    return "StrictStr";
                }
            }
        } else if (cp.isNumber || cp.isFloat || cp.isDouble) {
            if (cp.hasValidation) {
                List<String> fieldCustomization = new ArrayList<>();
                List<String> intFieldCustomization = new ArrayList<>();

                if (cp.getMaximum() != null) {
                    if (cp.getExclusiveMaximum()) {
                        fieldCustomization.add("lt=" + cp.getMaximum());
                        intFieldCustomization.add("lt=" + (int) Math.ceil(Double.valueOf(cp.getMaximum())));
                    } else {
                        fieldCustomization.add("le=" + cp.getMaximum());
                        intFieldCustomization.add("le=" + (int) Math.floor(Double.valueOf(cp.getMaximum())));
                    }
                }
                if (cp.getMinimum() != null) {
                    if (cp.getExclusiveMinimum()) {
                        fieldCustomization.add("gt=" + cp.getMinimum());
                        intFieldCustomization.add("gt=" + (int) Math.floor(Double.valueOf(cp.getMinimum())));
                    } else {
                        fieldCustomization.add("ge=" + cp.getMinimum());
                        intFieldCustomization.add("ge=" + (int) Math.ceil(Double.valueOf(cp.getMinimum())));
                    }
                }
                if (cp.getMultipleOf() != null) {
                    fieldCustomization.add("multiple_of=" + cp.getMultipleOf());
                }

                if ("Union[StrictFloat, StrictInt]".equals(mapNumberTo)) {
                    fieldCustomization.add("strict=True");
                    intFieldCustomization.add("strict=True");
                    pydanticImports.add("confloat");
                    pydanticImports.add("conint");
                    typingImports.add("Union");
                    return String.format(Locale.ROOT, "Union[%s(%s), %s(%s)]", "confloat",
                            StringUtils.join(fieldCustomization, ", "),
                            "conint",
                            StringUtils.join(intFieldCustomization, ", ")
                    );
                } else if ("StrictFloat".equals(mapNumberTo)) {
                    fieldCustomization.add("strict=True");
                    pydanticImports.add("confloat");
                    return String.format(Locale.ROOT, "%s(%s)", "confloat",
                            StringUtils.join(fieldCustomization, ", "));
                } else {
                    pydanticImports.add("confloat");
                    return String.format(Locale.ROOT, "%s(%s)", "confloat",
                            StringUtils.join(fieldCustomization, ", "));
                }
            } else {
                if ("Union[StrictFloat, StrictInt]".equals(mapNumberTo)) {
                    typingImports.add("Union");
                    pydanticImports.add("StrictFloat");
                    pydanticImports.add("StrictInt");
                    return "Union[StrictFloat, StrictInt]";
                } else if ("StrictFloat".equals(mapNumberTo)) {
                    pydanticImports.add("StrictFloat");
                    return "StrictFloat";
                } else {
                    return "float";
                }
            }
        } else if (cp.isInteger || cp.isLong || cp.isShort || cp.isUnboundedInteger) {
            if (cp.hasValidation) {
                List<String> fieldCustomization = new ArrayList<>();
                fieldCustomization.add("strict=True");
                if (cp.getMaximum() != null) {
                    if (cp.getExclusiveMaximum()) {
                        fieldCustomization.add("lt=" + cp.getMaximum());
                    } else {
                        fieldCustomization.add("le=" + cp.getMaximum());
                    }
                }
                if (cp.getMinimum() != null) {
                    if (cp.getExclusiveMinimum()) {
                        fieldCustomization.add("gt=" + cp.getMinimum());
                    } else {
                        fieldCustomization.add("ge=" + cp.getMinimum());
                    }
                }
                if (cp.getMultipleOf() != null) {
                    fieldCustomization.add("multiple_of=" + cp.getMultipleOf());
                }

                pydanticImports.add("conint");
                return String.format(Locale.ROOT, "%s(%s)", "conint",
                        StringUtils.join(fieldCustomization, ", "));
            } else {
                pydanticImports.add("StrictInt");
                return "StrictInt";
            }
        } else if (cp.isBinary || cp.isByteArray) {
            if (cp.hasValidation) {
                List<String> fieldCustomization = new ArrayList<>();
                fieldCustomization.add("strict=True");
                if (cp.getMinLength() != null) {
                    fieldCustomization.add("min_length=" + cp.getMinLength());
                }
                if (cp.getMaxLength() != null) {
                    fieldCustomization.add("max_length=" + cp.getMaxLength());
                }
                if (cp.getPattern() != null) {
                    pydanticImports.add("validator");
                }

                pydanticImports.add("conbytes");
                pydanticImports.add("constr");
                typingImports.add("Union");
                return String.format(Locale.ROOT, "Union[conbytes(%s), constr(%<s)]", StringUtils.join(fieldCustomization, ", "));
            } else {
                pydanticImports.add("StrictBytes");
                pydanticImports.add("StrictStr");
                typingImports.add("Union");
                return "Union[StrictBytes, StrictStr]";
            }
        } else if (cp.isBoolean) {
            pydanticImports.add("StrictBool");
            return "StrictBool";
        } else if (cp.isDecimal) {
            if (cp.hasValidation) {
                List<String> fieldCustomization = new ArrayList<>();
                fieldCustomization.add("strict=True");
                if (cp.getMaximum() != null) {
                    if (cp.getExclusiveMaximum()) {
                        fieldCustomization.add("gt=" + cp.getMaximum());
                    } else {
                        fieldCustomization.add("ge=" + cp.getMaximum());
                    }
                }
                if (cp.getMinimum() != null) {
                    if (cp.getExclusiveMinimum()) {
                        fieldCustomization.add("lt=" + cp.getMinimum());
                    } else {
                        fieldCustomization.add("le=" + cp.getMinimum());
                    }
                }
                if (cp.getMultipleOf() != null) {
                    fieldCustomization.add("multiple_of=" + cp.getMultipleOf());
                }
                pydanticImports.add("condecimal");
                return String.format(Locale.ROOT, "%s(%s)", "condecimal", StringUtils.join(fieldCustomization, ", "));
            } else {
                pydanticImports.add("condecimal");
                return "condecimal()";
            }
        } else if (cp.getIsAnyType()) {
            typingImports.add("Any");
            return "Any";
        } else if (cp.isDate || cp.isDateTime) {
            if (cp.isDate) {
                datetimeImports.add("date");
            }
            if (cp.isDateTime) {
                datetimeImports.add("datetime");
            }
            return cp.dataType;
        } else if (cp.isUuid) {
            return cp.dataType;
        } else if (cp.isFreeFormObject) {
            typingImports.add("Dict");
            typingImports.add("Any");
            return "Dict[str, Any]";
        } else if (!cp.isPrimitiveType || cp.isModel) {
            if (classname == null) {
                hasModelsToImport = true;
                modelImports.add(cp.dataType);
                exampleImports.add(cp.dataType);
            } else {
                if (lineCircularImports.containsKey(cp.dataType)) {
                    if (lineCircularImports.get(cp.dataType).contains(classname)) {
                        LOGGER.debug("Skipped importing {} in {} due to circular import.", cp.dataType, classname);
                    } else {
                        hasModelsToImport = true;
                        modelImports.add(cp.dataType);
                        exampleImports.add(cp.dataType);
                    }
                } else {
                    LOGGER.error("Failed to look up {} from the imports (map of set) of models.", cp.dataType);
                }
            }
            return cp.dataType;
        } else {
            throw new RuntimeException("Error! Codegen Property not yet supported in getPydanticType: " + cp);
        }
    }
}
