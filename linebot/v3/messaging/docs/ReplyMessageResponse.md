# ReplyMessageResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sent_messages** | [**List[SentMessage]**](SentMessage.md) | Array of sent messages. | 

## Example

```python
from linebot.v3.messaging.models.reply_message_response import ReplyMessageResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReplyMessageResponse from a JSON string
reply_message_response_instance = ReplyMessageResponse.from_json(json)
# print the JSON string representation of the object
print ReplyMessageResponse.to_json()

# convert the object into a dict
reply_message_response_dict = reply_message_response_instance.to_dict()
# create an instance of ReplyMessageResponse from a dict
reply_message_response_form_dict = reply_message_response.from_dict(reply_message_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


