# MemberJoinedEvent

Event object for when a user joins a group chat or multi-person chat that the LINE Official Account is in.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reply_token** | **str** | Reply token used to send reply message to this event | 
**joined** | [**JoinedMembers**](JoinedMembers.md) |  | 

## Example

```python
from linebot.v3.webhooks.models.member_joined_event import MemberJoinedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of MemberJoinedEvent from a JSON string
member_joined_event_instance = MemberJoinedEvent.from_json(json)
# print the JSON string representation of the object
print MemberJoinedEvent.to_json()

# convert the object into a dict
member_joined_event_dict = member_joined_event_instance.to_dict()
# create an instance of MemberJoinedEvent from a dict
member_joined_event_form_dict = member_joined_event.from_dict(member_joined_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


