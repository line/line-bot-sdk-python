# MemberLeftEvent

Event object for when a user leaves a group chat or multi-person chat that the LINE Official Account is in.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**left** | [**LeftMembers**](LeftMembers.md) |  | 

## Example

```python
from linebot.v3.webhooks.models.member_left_event import MemberLeftEvent

# TODO update the JSON string below
json = "{}"
# create an instance of MemberLeftEvent from a JSON string
member_left_event_instance = MemberLeftEvent.from_json(json)
# print the JSON string representation of the object
print MemberLeftEvent.to_json()

# convert the object into a dict
member_left_event_dict = member_left_event_instance.to_dict()
# create an instance of MemberLeftEvent from a dict
member_left_event_form_dict = member_left_event.from_dict(member_left_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


