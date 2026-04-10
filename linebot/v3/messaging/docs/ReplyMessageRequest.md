# ReplyMessageRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reply_token** | **str** | replyToken received via webhook. | 
**messages** | [**List[Message]**](Message.md) | List of messages. | 
**notification_disabled** | **bool** | &#x60;true&#x60;: The user doesn’t receive a push notification when a message is sent. &#x60;false&#x60;: The user receives a push notification when the message is sent (unless they have disabled push notifications in LINE and/or their device). The default value is false.  | [optional] [default to False]

## Example

```python
from linebot.v3.messaging.models.reply_message_request import ReplyMessageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReplyMessageRequest from a JSON string
reply_message_request_instance = ReplyMessageRequest.from_json(json)
# print the JSON string representation of the object
print ReplyMessageRequest.to_json()

# convert the object into a dict
reply_message_request_dict = reply_message_request_instance.to_dict()
# create an instance of ReplyMessageRequest from a dict
reply_message_request_form_dict = reply_message_request.from_dict(reply_message_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


