# GetWebhookEndpointResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endpoint** | **str** | Webhook URL | 
**active** | **bool** | Webhook usage status. Send a webhook event from the LINE Platform to the webhook URL only if enabled.  &#x60;true&#x60;: Webhook usage is enabled. &#x60;false&#x60;: Webhook usage is disabled.  | 

## Example

```python
from linebot.v3.messaging.models.get_webhook_endpoint_response import GetWebhookEndpointResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetWebhookEndpointResponse from a JSON string
get_webhook_endpoint_response_instance = GetWebhookEndpointResponse.from_json(json)
# print the JSON string representation of the object
print GetWebhookEndpointResponse.to_json()

# convert the object into a dict
get_webhook_endpoint_response_dict = get_webhook_endpoint_response_instance.to_dict()
# create an instance of GetWebhookEndpointResponse from a dict
get_webhook_endpoint_response_form_dict = get_webhook_endpoint_response.from_dict(get_webhook_endpoint_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


