# CouponCashBackRewardRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**price_info** | [**CashBackPriceInfoRequest**](CashBackPriceInfoRequest.md) |  | [optional] 

## Example

```python
from linebot.v3.messaging.models.coupon_cash_back_reward_request import CouponCashBackRewardRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CouponCashBackRewardRequest from a JSON string
coupon_cash_back_reward_request_instance = CouponCashBackRewardRequest.from_json(json)
# print the JSON string representation of the object
print CouponCashBackRewardRequest.to_json()

# convert the object into a dict
coupon_cash_back_reward_request_dict = coupon_cash_back_reward_request_instance.to_dict()
# create an instance of CouponCashBackRewardRequest from a dict
coupon_cash_back_reward_request_form_dict = coupon_cash_back_reward_request.from_dict(coupon_cash_back_reward_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


