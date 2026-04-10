# FollowEvent

Event object for when your LINE Official Account is added as a friend (or unblocked). You can reply to follow events.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reply_token** | **str** | Reply token used to send reply message to this event | 
**follow** | [**FollowDetail**](FollowDetail.md) |  | 

## Example

```python
from linebot.v3.webhooks.models.follow_event import FollowEvent

# TODO update the JSON string below
json = "{}"
# create an instance of FollowEvent from a JSON string
follow_event_instance = FollowEvent.from_json(json)
# print the JSON string representation of the object
print FollowEvent.to_json()

# convert the object into a dict
follow_event_dict = follow_event_instance.to_dict()
# create an instance of FollowEvent from a dict
follow_event_form_dict = follow_event.from_dict(follow_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


