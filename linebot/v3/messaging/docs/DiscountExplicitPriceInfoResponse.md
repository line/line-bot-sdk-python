# DiscountExplicitPriceInfoResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** | Currency code (e.g., JPY, THB, TWD). | [optional] 
**price_after_discount** | **int** |  | [optional] 
**original_price** | **int** |  | [optional] 

## Example

```python
from linebot.v3.messaging.models.discount_explicit_price_info_response import DiscountExplicitPriceInfoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DiscountExplicitPriceInfoResponse from a JSON string
discount_explicit_price_info_response_instance = DiscountExplicitPriceInfoResponse.from_json(json)
# print the JSON string representation of the object
print DiscountExplicitPriceInfoResponse.to_json()

# convert the object into a dict
discount_explicit_price_info_response_dict = discount_explicit_price_info_response_instance.to_dict()
# create an instance of DiscountExplicitPriceInfoResponse from a dict
discount_explicit_price_info_response_form_dict = discount_explicit_price_info_response.from_dict(discount_explicit_price_info_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


