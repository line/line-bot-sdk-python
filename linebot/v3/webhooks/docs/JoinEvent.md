# JoinEvent

Event object for when your LINE Official Account joins a group chat or multi-person chat. You can reply to join events.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reply_token** | **str** | Reply token used to send reply message to this event | 

## Example

```python
from linebot.v3.webhooks.models.join_event import JoinEvent

# TODO update the JSON string below
json = "{}"
# create an instance of JoinEvent from a JSON string
join_event_instance = JoinEvent.from_json(json)
# print the JSON string representation of the object
print JoinEvent.to_json()

# convert the object into a dict
join_event_dict = join_event_instance.to_dict()
# create an instance of JoinEvent from a dict
join_event_form_dict = join_event.from_dict(join_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


