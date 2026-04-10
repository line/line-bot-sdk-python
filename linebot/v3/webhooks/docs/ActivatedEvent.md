# ActivatedEvent

This event indicates that the module channel has been switched to Active Channel by calling the Acquire Control API. Sent to the webhook URL server of the module channel.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat_control** | [**ChatControl**](ChatControl.md) |  | 

## Example

```python
from linebot.v3.webhooks.models.activated_event import ActivatedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ActivatedEvent from a JSON string
activated_event_instance = ActivatedEvent.from_json(json)
# print the JSON string representation of the object
print ActivatedEvent.to_json()

# convert the object into a dict
activated_event_dict = activated_event_instance.to_dict()
# create an instance of ActivatedEvent from a dict
activated_event_form_dict = activated_event.from_dict(activated_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


