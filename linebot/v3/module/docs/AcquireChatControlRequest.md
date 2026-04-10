# AcquireChatControlRequest

Request entity of the Acquire Control API

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expired** | **bool** | &#x60;True&#x60;: After the time limit (ttl) has passed, the initiative (Chat Control) will return to the Primary Channel. (Default) &#x60;False&#x60;: There&#39;s no time limit and the initiative (Chat Control) doesn&#39;t change over time.  | [optional] 
**ttl** | **int** | The time it takes for initiative (Chat Control) to return to the Primary Channel (the time that the module channel stays on the Active Channel). The value is specified in seconds. The maximum value is one year (3600 * 24 * 365). The default value is 3600 (1 hour).  * Ignored if the value of expired is false.  | [optional] 

## Example

```python
from linebot.v3.module.models.acquire_chat_control_request import AcquireChatControlRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AcquireChatControlRequest from a JSON string
acquire_chat_control_request_instance = AcquireChatControlRequest.from_json(json)
# print the JSON string representation of the object
print AcquireChatControlRequest.to_json()

# convert the object into a dict
acquire_chat_control_request_dict = acquire_chat_control_request_instance.to_dict()
# create an instance of AcquireChatControlRequest from a dict
acquire_chat_control_request_form_dict = acquire_chat_control_request.from_dict(acquire_chat_control_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


