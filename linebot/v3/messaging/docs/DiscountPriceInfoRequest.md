# DiscountPriceInfoRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 

## Example

```python
from linebot.v3.messaging.models.discount_price_info_request import DiscountPriceInfoRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DiscountPriceInfoRequest from a JSON string
discount_price_info_request_instance = DiscountPriceInfoRequest.from_json(json)
# print the JSON string representation of the object
print DiscountPriceInfoRequest.to_json()

# convert the object into a dict
discount_price_info_request_dict = discount_price_info_request_instance.to_dict()
# create an instance of DiscountPriceInfoRequest from a dict
discount_price_info_request_form_dict = discount_price_info_request.from_dict(discount_price_info_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


