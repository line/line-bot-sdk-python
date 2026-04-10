# PostbackEvent

Event object for when a user performs a postback action which initiates a postback. You can reply to postback events.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reply_token** | **str** | Reply token used to send reply message to this event | [optional] 
**postback** | [**PostbackContent**](PostbackContent.md) |  | 

## Example

```python
from linebot.v3.webhooks.models.postback_event import PostbackEvent

# TODO update the JSON string below
json = "{}"
# create an instance of PostbackEvent from a JSON string
postback_event_instance = PostbackEvent.from_json(json)
# print the JSON string representation of the object
print PostbackEvent.to_json()

# convert the object into a dict
postback_event_dict = postback_event_instance.to_dict()
# create an instance of PostbackEvent from a dict
postback_event_form_dict = postback_event.from_dict(postback_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


