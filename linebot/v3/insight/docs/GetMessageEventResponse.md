# GetMessageEventResponse

Statistics about how users interact with narrowcast messages or broadcast messages sent from your LINE Official Account.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**overview** | [**GetMessageEventResponseOverview**](GetMessageEventResponseOverview.md) |  | [optional] 
**messages** | [**List[GetMessageEventResponseMessage]**](GetMessageEventResponseMessage.md) | Array of information about individual message bubbles. | [optional] 
**clicks** | [**List[GetMessageEventResponseClick]**](GetMessageEventResponseClick.md) | Array of information about opened URLs in the message. | [optional] 

## Example

```python
from linebot.v3.insight.models.get_message_event_response import GetMessageEventResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetMessageEventResponse from a JSON string
get_message_event_response_instance = GetMessageEventResponse.from_json(json)
# print the JSON string representation of the object
print GetMessageEventResponse.to_json()

# convert the object into a dict
get_message_event_response_dict = get_message_event_response_instance.to_dict()
# create an instance of GetMessageEventResponse from a dict
get_message_event_response_form_dict = get_message_event_response.from_dict(get_message_event_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


