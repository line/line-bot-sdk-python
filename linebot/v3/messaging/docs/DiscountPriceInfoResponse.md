# DiscountPriceInfoResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 

## Example

```python
from linebot.v3.messaging.models.discount_price_info_response import DiscountPriceInfoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DiscountPriceInfoResponse from a JSON string
discount_price_info_response_instance = DiscountPriceInfoResponse.from_json(json)
# print the JSON string representation of the object
print DiscountPriceInfoResponse.to_json()

# convert the object into a dict
discount_price_info_response_dict = discount_price_info_response_instance.to_dict()
# create an instance of DiscountPriceInfoResponse from a dict
discount_price_info_response_form_dict = discount_price_info_response.from_dict(discount_price_info_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


