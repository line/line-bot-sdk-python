# BroadcastRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**messages** | [**List[Message]**](Message.md) | List of Message objects. | 
**notification_disabled** | **bool** | &#x60;true&#x60;: The user doesn’t receive a push notification when a message is sent. &#x60;false&#x60;: The user receives a push notification when the message is sent (unless they have disabled push notifications in LINE and/or their device). The default value is false.  | [optional] [default to False]

## Example

```python
from linebot.v3.messaging.models.broadcast_request import BroadcastRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BroadcastRequest from a JSON string
broadcast_request_instance = BroadcastRequest.from_json(json)
# print the JSON string representation of the object
print BroadcastRequest.to_json()

# convert the object into a dict
broadcast_request_dict = broadcast_request_instance.to_dict()
# create an instance of BroadcastRequest from a dict
broadcast_request_form_dict = broadcast_request.from_dict(broadcast_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


