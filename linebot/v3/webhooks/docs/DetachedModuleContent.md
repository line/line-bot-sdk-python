# DetachedModuleContent


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bot_id** | **str** | Detached LINE Official Account bot user ID | 
**reason** | **str** | Reason for detaching | 

## Example

```python
from linebot.v3.webhooks.models.detached_module_content import DetachedModuleContent

# TODO update the JSON string below
json = "{}"
# create an instance of DetachedModuleContent from a JSON string
detached_module_content_instance = DetachedModuleContent.from_json(json)
# print the JSON string representation of the object
print DetachedModuleContent.to_json()

# convert the object into a dict
detached_module_content_dict = detached_module_content_instance.to_dict()
# create an instance of DetachedModuleContent from a dict
detached_module_content_form_dict = detached_module_content.from_dict(detached_module_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


