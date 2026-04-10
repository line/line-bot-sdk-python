# TextMessageContent


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** | Message text. | 
**emojis** | [**List[Emoji]**](Emoji.md) | Array of one or more LINE emoji objects. Only included in the message event when the text property contains a LINE emoji. | [optional] 
**mention** | [**Mention**](Mention.md) |  | [optional] 
**quote_token** | **str** | Quote token to quote this message.  | 
**quoted_message_id** | **str** | Message ID of a quoted message. Only included when the received message quotes a past message. | [optional] 
**mark_as_read_token** | **str** | Token used to mark the message as read.  | [optional] 

## Example

```python
from linebot.v3.webhooks.models.text_message_content import TextMessageContent

# TODO update the JSON string below
json = "{}"
# create an instance of TextMessageContent from a JSON string
text_message_content_instance = TextMessageContent.from_json(json)
# print the JSON string representation of the object
print TextMessageContent.to_json()

# convert the object into a dict
text_message_content_dict = text_message_content_instance.to_dict()
# create an instance of TextMessageContent from a dict
text_message_content_form_dict = text_message_content.from_dict(text_message_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


