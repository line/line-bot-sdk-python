# PushMessageResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sent_messages** | [**List[SentMessage]**](SentMessage.md) | Array of sent messages. | 

## Example

```python
from linebot.v3.messaging.models.push_message_response import PushMessageResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PushMessageResponse from a JSON string
push_message_response_instance = PushMessageResponse.from_json(json)
# print the JSON string representation of the object
print PushMessageResponse.to_json()

# convert the object into a dict
push_message_response_dict = push_message_response_instance.to_dict()
# create an instance of PushMessageResponse from a dict
push_message_response_form_dict = push_message_response.from_dict(push_message_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


