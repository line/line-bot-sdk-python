# PnpDeliveryCompletionEvent

When a request is made to the LINE notification messages API and delivery of the LINE notification message to the user is completed, a dedicated webhook event (delivery completion event) is sent from the LINE Platform to the webhook URL of the bot server.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delivery** | [**PnpDelivery**](PnpDelivery.md) |  | 

## Example

```python
from linebot.v3.webhooks.models.pnp_delivery_completion_event import PnpDeliveryCompletionEvent

# TODO update the JSON string below
json = "{}"
# create an instance of PnpDeliveryCompletionEvent from a JSON string
pnp_delivery_completion_event_instance = PnpDeliveryCompletionEvent.from_json(json)
# print the JSON string representation of the object
print PnpDeliveryCompletionEvent.to_json()

# convert the object into a dict
pnp_delivery_completion_event_dict = pnp_delivery_completion_event_instance.to_dict()
# create an instance of PnpDeliveryCompletionEvent from a dict
pnp_delivery_completion_event_form_dict = pnp_delivery_completion_event.from_dict(pnp_delivery_completion_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


