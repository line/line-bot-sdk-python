# SetWebhookEndpointRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endpoint** | **str** | A valid webhook URL. | 

## Example

```python
from linebot.v3.messaging.models.set_webhook_endpoint_request import SetWebhookEndpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetWebhookEndpointRequest from a JSON string
set_webhook_endpoint_request_instance = SetWebhookEndpointRequest.from_json(json)
# print the JSON string representation of the object
print SetWebhookEndpointRequest.to_json()

# convert the object into a dict
set_webhook_endpoint_request_dict = set_webhook_endpoint_request_instance.to_dict()
# create an instance of SetWebhookEndpointRequest from a dict
set_webhook_endpoint_request_form_dict = set_webhook_endpoint_request.from_dict(set_webhook_endpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


