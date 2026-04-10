# CashBackFixedPriceInfoRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fixed_amount** | **int** |  | [optional] 

## Example

```python
from linebot.v3.messaging.models.cash_back_fixed_price_info_request import CashBackFixedPriceInfoRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CashBackFixedPriceInfoRequest from a JSON string
cash_back_fixed_price_info_request_instance = CashBackFixedPriceInfoRequest.from_json(json)
# print the JSON string representation of the object
print CashBackFixedPriceInfoRequest.to_json()

# convert the object into a dict
cash_back_fixed_price_info_request_dict = cash_back_fixed_price_info_request_instance.to_dict()
# create an instance of CashBackFixedPriceInfoRequest from a dict
cash_back_fixed_price_info_request_form_dict = cash_back_fixed_price_info_request.from_dict(cash_back_fixed_price_info_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


