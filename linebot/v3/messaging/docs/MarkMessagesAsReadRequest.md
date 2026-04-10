# MarkMessagesAsReadRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat** | [**ChatReference**](ChatReference.md) |  | 

## Example

```python
from linebot.v3.messaging.models.mark_messages_as_read_request import MarkMessagesAsReadRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MarkMessagesAsReadRequest from a JSON string
mark_messages_as_read_request_instance = MarkMessagesAsReadRequest.from_json(json)
# print the JSON string representation of the object
print MarkMessagesAsReadRequest.to_json()

# convert the object into a dict
mark_messages_as_read_request_dict = mark_messages_as_read_request_instance.to_dict()
# create an instance of MarkMessagesAsReadRequest from a dict
mark_messages_as_read_request_form_dict = mark_messages_as_read_request.from_dict(mark_messages_as_read_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


