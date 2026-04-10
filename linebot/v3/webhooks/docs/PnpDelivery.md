# PnpDelivery

A delivery object containing a hashed phone number string or a string specified by `X-Line-Delivery-Tag` header

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **str** | A hashed phone number string or a string specified by &#x60;X-Line-Delivery-Tag&#x60; header | 

## Example

```python
from linebot.v3.webhooks.models.pnp_delivery import PnpDelivery

# TODO update the JSON string below
json = "{}"
# create an instance of PnpDelivery from a JSON string
pnp_delivery_instance = PnpDelivery.from_json(json)
# print the JSON string representation of the object
print PnpDelivery.to_json()

# convert the object into a dict
pnp_delivery_dict = pnp_delivery_instance.to_dict()
# create an instance of PnpDelivery from a dict
pnp_delivery_form_dict = pnp_delivery.from_dict(pnp_delivery_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


