# MessageEvent

Webhook event object which contains the sent message.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reply_token** | **str** |  | [optional] 
**message** | [**MessageContent**](MessageContent.md) |  | 

## Example

```python
from linebot.v3.webhooks.models.message_event import MessageEvent

# TODO update the JSON string below
json = "{}"
# create an instance of MessageEvent from a JSON string
message_event_instance = MessageEvent.from_json(json)
# print the JSON string representation of the object
print MessageEvent.to_json()

# convert the object into a dict
message_event_dict = message_event_instance.to_dict()
# create an instance of MessageEvent from a dict
message_event_form_dict = message_event.from_dict(message_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


