# MarkMessagesAsReadByTokenRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mark_as_read_token** | **str** | Token used to mark messages as read. | 

## Example

```python
from linebot.v3.messaging.models.mark_messages_as_read_by_token_request import MarkMessagesAsReadByTokenRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MarkMessagesAsReadByTokenRequest from a JSON string
mark_messages_as_read_by_token_request_instance = MarkMessagesAsReadByTokenRequest.from_json(json)
# print the JSON string representation of the object
print MarkMessagesAsReadByTokenRequest.to_json()

# convert the object into a dict
mark_messages_as_read_by_token_request_dict = mark_messages_as_read_by_token_request_instance.to_dict()
# create an instance of MarkMessagesAsReadByTokenRequest from a dict
mark_messages_as_read_by_token_request_form_dict = mark_messages_as_read_by_token_request.from_dict(mark_messages_as_read_by_token_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


