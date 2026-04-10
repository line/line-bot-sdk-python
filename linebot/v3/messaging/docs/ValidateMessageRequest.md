# ValidateMessageRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**messages** | [**List[Message]**](Message.md) | Array of message objects to validate | 

## Example

```python
from linebot.v3.messaging.models.validate_message_request import ValidateMessageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ValidateMessageRequest from a JSON string
validate_message_request_instance = ValidateMessageRequest.from_json(json)
# print the JSON string representation of the object
print ValidateMessageRequest.to_json()

# convert the object into a dict
validate_message_request_dict = validate_message_request_instance.to_dict()
# create an instance of ValidateMessageRequest from a dict
validate_message_request_form_dict = validate_message_request.from_dict(validate_message_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


