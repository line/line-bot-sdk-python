# CashBackPercentagePriceInfoResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**percentage** | **int** |  | [optional] 

## Example

```python
from linebot.v3.messaging.models.cash_back_percentage_price_info_response import CashBackPercentagePriceInfoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CashBackPercentagePriceInfoResponse from a JSON string
cash_back_percentage_price_info_response_instance = CashBackPercentagePriceInfoResponse.from_json(json)
# print the JSON string representation of the object
print CashBackPercentagePriceInfoResponse.to_json()

# convert the object into a dict
cash_back_percentage_price_info_response_dict = cash_back_percentage_price_info_response_instance.to_dict()
# create an instance of CashBackPercentagePriceInfoResponse from a dict
cash_back_percentage_price_info_response_form_dict = cash_back_percentage_price_info_response.from_dict(cash_back_percentage_price_info_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


