# CashBackPriceInfoRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 

## Example

```python
from linebot.v3.messaging.models.cash_back_price_info_request import CashBackPriceInfoRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CashBackPriceInfoRequest from a JSON string
cash_back_price_info_request_instance = CashBackPriceInfoRequest.from_json(json)
# print the JSON string representation of the object
print CashBackPriceInfoRequest.to_json()

# convert the object into a dict
cash_back_price_info_request_dict = cash_back_price_info_request_instance.to_dict()
# create an instance of CashBackPriceInfoRequest from a dict
cash_back_price_info_request_form_dict = cash_back_price_info_request.from_dict(cash_back_price_info_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


