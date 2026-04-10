# DiscountExplicitPriceInfoRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**price_after_discount** | **int** |  | [optional] 
**original_price** | **int** |  | [optional] 

## Example

```python
from linebot.v3.messaging.models.discount_explicit_price_info_request import DiscountExplicitPriceInfoRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DiscountExplicitPriceInfoRequest from a JSON string
discount_explicit_price_info_request_instance = DiscountExplicitPriceInfoRequest.from_json(json)
# print the JSON string representation of the object
print DiscountExplicitPriceInfoRequest.to_json()

# convert the object into a dict
discount_explicit_price_info_request_dict = discount_explicit_price_info_request_instance.to_dict()
# create an instance of DiscountExplicitPriceInfoRequest from a dict
discount_explicit_price_info_request_form_dict = discount_explicit_price_info_request.from_dict(discount_explicit_price_info_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


