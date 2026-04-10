# TextMessage


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** |  | 
**emojis** | [**List[Emoji]**](Emoji.md) |  | [optional] 
**quote_token** | **str** | Quote token of the message you want to quote. | [optional] 

## Example

```python
from linebot.v3.messaging.models.text_message import TextMessage

# TODO update the JSON string below
json = "{}"
# create an instance of TextMessage from a JSON string
text_message_instance = TextMessage.from_json(json)
# print the JSON string representation of the object
print TextMessage.to_json()

# convert the object into a dict
text_message_dict = text_message_instance.to_dict()
# create an instance of TextMessage from a dict
text_message_form_dict = text_message.from_dict(text_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


