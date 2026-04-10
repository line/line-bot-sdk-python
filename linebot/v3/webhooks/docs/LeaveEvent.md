# LeaveEvent

Event object for when a user removes your LINE Official Account from a group chat or when your LINE Official Account leaves a group chat or multi-person chat.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from linebot.v3.webhooks.models.leave_event import LeaveEvent

# TODO update the JSON string below
json = "{}"
# create an instance of LeaveEvent from a JSON string
leave_event_instance = LeaveEvent.from_json(json)
# print the JSON string representation of the object
print LeaveEvent.to_json()

# convert the object into a dict
leave_event_dict = leave_event_instance.to_dict()
# create an instance of LeaveEvent from a dict
leave_event_form_dict = leave_event.from_dict(leave_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


