# DetachModuleRequest

Unlink (detach) the module channel by the operation of the module channel administrator

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bot_id** | **str** | User ID of the LINE Official Account bot attached to the module channel. | [optional] 

## Example

```python
from linebot.v3.module.models.detach_module_request import DetachModuleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DetachModuleRequest from a JSON string
detach_module_request_instance = DetachModuleRequest.from_json(json)
# print the JSON string representation of the object
print DetachModuleRequest.to_json()

# convert the object into a dict
detach_module_request_dict = detach_module_request_instance.to_dict()
# create an instance of DetachModuleRequest from a dict
detach_module_request_form_dict = detach_module_request.from_dict(detach_module_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


