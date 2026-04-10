# CashBackFixedPriceInfoResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** | Currency code (e.g., JPY, THB, TWD). | [optional] 
**fixed_amount** | **int** |  | [optional] 

## Example

```python
from linebot.v3.messaging.models.cash_back_fixed_price_info_response import CashBackFixedPriceInfoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CashBackFixedPriceInfoResponse from a JSON string
cash_back_fixed_price_info_response_instance = CashBackFixedPriceInfoResponse.from_json(json)
# print the JSON string representation of the object
print CashBackFixedPriceInfoResponse.to_json()

# convert the object into a dict
cash_back_fixed_price_info_response_dict = cash_back_fixed_price_info_response_instance.to_dict()
# create an instance of CashBackFixedPriceInfoResponse from a dict
cash_back_fixed_price_info_response_form_dict = cash_back_fixed_price_info_response.from_dict(cash_back_fixed_price_info_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


