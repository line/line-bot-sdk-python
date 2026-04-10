# CashBackPercentagePriceInfoRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**percentage** | **int** | Specifies the cashback rate as a percentage. Must be an integer between 1 and 99. | [optional] 

## Example

```python
from linebot.v3.messaging.models.cash_back_percentage_price_info_request import CashBackPercentagePriceInfoRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CashBackPercentagePriceInfoRequest from a JSON string
cash_back_percentage_price_info_request_instance = CashBackPercentagePriceInfoRequest.from_json(json)
# print the JSON string representation of the object
print CashBackPercentagePriceInfoRequest.to_json()

# convert the object into a dict
cash_back_percentage_price_info_request_dict = cash_back_percentage_price_info_request_instance.to_dict()
# create an instance of CashBackPercentagePriceInfoRequest from a dict
cash_back_percentage_price_info_request_form_dict = cash_back_percentage_price_info_request.from_dict(cash_back_percentage_price_info_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


