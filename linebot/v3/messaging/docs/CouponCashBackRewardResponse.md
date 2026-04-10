# CouponCashBackRewardResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**price_info** | [**CashBackPriceInfoResponse**](CashBackPriceInfoResponse.md) |  | [optional] 

## Example

```python
from linebot.v3.messaging.models.coupon_cash_back_reward_response import CouponCashBackRewardResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CouponCashBackRewardResponse from a JSON string
coupon_cash_back_reward_response_instance = CouponCashBackRewardResponse.from_json(json)
# print the JSON string representation of the object
print CouponCashBackRewardResponse.to_json()

# convert the object into a dict
coupon_cash_back_reward_response_dict = coupon_cash_back_reward_response_instance.to_dict()
# create an instance of CouponCashBackRewardResponse from a dict
coupon_cash_back_reward_response_form_dict = coupon_cash_back_reward_response.from_dict(coupon_cash_back_reward_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


