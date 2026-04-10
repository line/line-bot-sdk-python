# CashBackPriceInfoResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 

## Example

```python
from linebot.v3.messaging.models.cash_back_price_info_response import CashBackPriceInfoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CashBackPriceInfoResponse from a JSON string
cash_back_price_info_response_instance = CashBackPriceInfoResponse.from_json(json)
# print the JSON string representation of the object
print CashBackPriceInfoResponse.to_json()

# convert the object into a dict
cash_back_price_info_response_dict = cash_back_price_info_response_instance.to_dict()
# create an instance of CashBackPriceInfoResponse from a dict
cash_back_price_info_response_form_dict = cash_back_price_info_response.from_dict(cash_back_price_info_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


