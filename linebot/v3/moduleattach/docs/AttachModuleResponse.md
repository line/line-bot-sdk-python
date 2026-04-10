# AttachModuleResponse

Attach by operation of the module channel provider

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bot_id** | **str** | User ID of the bot on the LINE Official Account. | 
**scopes** | **List[str]** | Permissions (scope) granted by the LINE Official Account admin. | 

## Example

```python
from linebot.v3.moduleattach.models.attach_module_response import AttachModuleResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AttachModuleResponse from a JSON string
attach_module_response_instance = AttachModuleResponse.from_json(json)
# print the JSON string representation of the object
print AttachModuleResponse.to_json()

# convert the object into a dict
attach_module_response_dict = attach_module_response_instance.to_dict()
# create an instance of AttachModuleResponse from a dict
attach_module_response_form_dict = attach_module_response.from_dict(attach_module_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


