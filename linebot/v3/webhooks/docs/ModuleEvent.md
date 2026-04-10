# ModuleEvent

This event indicates that the module channel has been attached to the LINE Official Account. Sent to the webhook URL server of the module channel.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**module** | [**ModuleContent**](ModuleContent.md) |  | 

## Example

```python
from linebot.v3.webhooks.models.module_event import ModuleEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ModuleEvent from a JSON string
module_event_instance = ModuleEvent.from_json(json)
# print the JSON string representation of the object
print ModuleEvent.to_json()

# convert the object into a dict
module_event_dict = module_event_instance.to_dict()
# create an instance of ModuleEvent from a dict
module_event_form_dict = module_event.from_dict(module_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


