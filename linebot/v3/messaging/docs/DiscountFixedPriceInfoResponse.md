# DiscountFixedPriceInfoResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** | Currency code (e.g., JPY, THB, TWD). | [optional] 
**fixed_amount** | **int** |  | [optional] 

## Example

```python
from linebot.v3.messaging.models.discount_fixed_price_info_response import DiscountFixedPriceInfoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DiscountFixedPriceInfoResponse from a JSON string
discount_fixed_price_info_response_instance = DiscountFixedPriceInfoResponse.from_json(json)
# print the JSON string representation of the object
print DiscountFixedPriceInfoResponse.to_json()

# convert the object into a dict
discount_fixed_price_info_response_dict = discount_fixed_price_info_response_instance.to_dict()
# create an instance of DiscountFixedPriceInfoResponse from a dict
discount_fixed_price_info_response_form_dict = discount_fixed_price_info_response.from_dict(discount_fixed_price_info_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


