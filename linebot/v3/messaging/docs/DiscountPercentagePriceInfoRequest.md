# DiscountPercentagePriceInfoRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**percentage** | **int** | Specifies the discount rate as a percentage. Must be an integer between 1 and 99. | [optional] 

## Example

```python
from linebot.v3.messaging.models.discount_percentage_price_info_request import DiscountPercentagePriceInfoRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DiscountPercentagePriceInfoRequest from a JSON string
discount_percentage_price_info_request_instance = DiscountPercentagePriceInfoRequest.from_json(json)
# print the JSON string representation of the object
print DiscountPercentagePriceInfoRequest.to_json()

# convert the object into a dict
discount_percentage_price_info_request_dict = discount_percentage_price_info_request_instance.to_dict()
# create an instance of DiscountPercentagePriceInfoRequest from a dict
discount_percentage_price_info_request_form_dict = discount_percentage_price_info_request.from_dict(discount_percentage_price_info_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


