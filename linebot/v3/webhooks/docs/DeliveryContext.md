# DeliveryContext

webhook's delivery context information

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_redelivery** | **bool** | Whether the webhook event is a redelivered one or not. | 

## Example

```python
from linebot.v3.webhooks.models.delivery_context import DeliveryContext

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveryContext from a JSON string
delivery_context_instance = DeliveryContext.from_json(json)
# print the JSON string representation of the object
print DeliveryContext.to_json()

# convert the object into a dict
delivery_context_dict = delivery_context_instance.to_dict()
# create an instance of DeliveryContext from a dict
delivery_context_form_dict = delivery_context.from_dict(delivery_context_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


