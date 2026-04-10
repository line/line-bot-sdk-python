# SentMessage


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the sent message. | 
**quote_token** | **str** | Quote token of the message. Only included when a message object that can be specified as a quote target was sent as a push or reply message.  | [optional] 

## Example

```python
from linebot.v3.messaging.models.sent_message import SentMessage

# TODO update the JSON string below
json = "{}"
# create an instance of SentMessage from a JSON string
sent_message_instance = SentMessage.from_json(json)
# print the JSON string representation of the object
print SentMessage.to_json()

# convert the object into a dict
sent_message_dict = sent_message_instance.to_dict()
# create an instance of SentMessage from a dict
sent_message_form_dict = sent_message.from_dict(sent_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


