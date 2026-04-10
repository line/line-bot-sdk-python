# DiscountPercentagePriceInfoResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**percentage** | **int** |  | [optional] 

## Example

```python
from linebot.v3.messaging.models.discount_percentage_price_info_response import DiscountPercentagePriceInfoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DiscountPercentagePriceInfoResponse from a JSON string
discount_percentage_price_info_response_instance = DiscountPercentagePriceInfoResponse.from_json(json)
# print the JSON string representation of the object
print DiscountPercentagePriceInfoResponse.to_json()

# convert the object into a dict
discount_percentage_price_info_response_dict = discount_percentage_price_info_response_instance.to_dict()
# create an instance of DiscountPercentagePriceInfoResponse from a dict
discount_percentage_price_info_response_form_dict = discount_percentage_price_info_response.from_dict(discount_percentage_price_info_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


