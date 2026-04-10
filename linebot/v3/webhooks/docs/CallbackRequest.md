# CallbackRequest

The request body contains a JSON object with the user ID of a bot that should receive webhook events and an array of webhook event objects. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination** | **str** | User ID of a bot that should receive webhook events. The user ID value is a string that matches the regular expression, &#x60;U[0-9a-f]{32}&#x60;.  | 
**events** | [**List[Event]**](Event.md) | Array of webhook event objects. The LINE Platform may send an empty array that doesn&#39;t include a webhook event object to confirm communication.  | 

## Example

```python
from linebot.v3.webhooks.models.callback_request import CallbackRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CallbackRequest from a JSON string
callback_request_instance = CallbackRequest.from_json(json)
# print the JSON string representation of the object
print CallbackRequest.to_json()

# convert the object into a dict
callback_request_dict = callback_request_instance.to_dict()
# create an instance of CallbackRequest from a dict
callback_request_form_dict = callback_request.from_dict(callback_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


