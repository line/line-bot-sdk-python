# TestWebhookEndpointRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endpoint** | **str** | A webhook URL to be validated. | [optional] 

## Example

```python
from linebot.v3.messaging.models.test_webhook_endpoint_request import TestWebhookEndpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TestWebhookEndpointRequest from a JSON string
test_webhook_endpoint_request_instance = TestWebhookEndpointRequest.from_json(json)
# print the JSON string representation of the object
print TestWebhookEndpointRequest.to_json()

# convert the object into a dict
test_webhook_endpoint_request_dict = test_webhook_endpoint_request_instance.to_dict()
# create an instance of TestWebhookEndpointRequest from a dict
test_webhook_endpoint_request_form_dict = test_webhook_endpoint_request.from_dict(test_webhook_endpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


