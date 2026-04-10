# AttachedModuleContent


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bot_id** | **str** | User ID of the bot on the attached LINE Official Account | 
**scopes** | **List[str]** | An array of strings indicating the scope permitted by the admin of the LINE Official Account. | 

## Example

```python
from linebot.v3.webhooks.models.attached_module_content import AttachedModuleContent

# TODO update the JSON string below
json = "{}"
# create an instance of AttachedModuleContent from a JSON string
attached_module_content_instance = AttachedModuleContent.from_json(json)
# print the JSON string representation of the object
print AttachedModuleContent.to_json()

# convert the object into a dict
attached_module_content_dict = attached_module_content_instance.to_dict()
# create an instance of AttachedModuleContent from a dict
attached_module_content_form_dict = attached_module_content.from_dict(attached_module_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


