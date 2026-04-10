# TestWebhookEndpointResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Result of the communication from the LINE platform to the webhook URL. | [optional] 
**timestamp** | **datetime** | Time of the event in milliseconds. Even in the case of a redelivered webhook, it represents the time the event occurred, not the time it was redelivered.  | 
**status_code** | **int** | The HTTP status code. If the webhook response isn&#39;t received, the status code is set to zero or a negative number. | 
**reason** | **str** | Reason for the response. | 
**detail** | **str** | Details of the response. | 

## Example

```python
from linebot.v3.messaging.models.test_webhook_endpoint_response import TestWebhookEndpointResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TestWebhookEndpointResponse from a JSON string
test_webhook_endpoint_response_instance = TestWebhookEndpointResponse.from_json(json)
# print the JSON string representation of the object
print TestWebhookEndpointResponse.to_json()

# convert the object into a dict
test_webhook_endpoint_response_dict = test_webhook_endpoint_response_instance.to_dict()
# create an instance of TestWebhookEndpointResponse from a dict
test_webhook_endpoint_response_form_dict = test_webhook_endpoint_response.from_dict(test_webhook_endpoint_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


