# MembershipEvent

This event indicates that a user has subscribed (joined), unsubscribed (left), or renewed the bot's membership.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reply_token** | **str** | Reply token used to send reply message to this event | 
**membership** | [**MembershipContent**](MembershipContent.md) |  | 

## Example

```python
from linebot.v3.webhooks.models.membership_event import MembershipEvent

# TODO update the JSON string below
json = "{}"
# create an instance of MembershipEvent from a JSON string
membership_event_instance = MembershipEvent.from_json(json)
# print the JSON string representation of the object
print MembershipEvent.to_json()

# convert the object into a dict
membership_event_dict = membership_event_instance.to_dict()
# create an instance of MembershipEvent from a dict
membership_event_form_dict = membership_event.from_dict(membership_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


