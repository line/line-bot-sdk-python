# DiscountFixedPriceInfoRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fixed_amount** | **int** |  | [optional] 

## Example

```python
from linebot.v3.messaging.models.discount_fixed_price_info_request import DiscountFixedPriceInfoRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DiscountFixedPriceInfoRequest from a JSON string
discount_fixed_price_info_request_instance = DiscountFixedPriceInfoRequest.from_json(json)
# print the JSON string representation of the object
print DiscountFixedPriceInfoRequest.to_json()

# convert the object into a dict
discount_fixed_price_info_request_dict = discount_fixed_price_info_request_instance.to_dict()
# create an instance of DiscountFixedPriceInfoRequest from a dict
discount_fixed_price_info_request_form_dict = discount_fixed_price_info_request.from_dict(discount_fixed_price_info_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


