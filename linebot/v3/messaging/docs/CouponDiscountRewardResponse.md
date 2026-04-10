# CouponDiscountRewardResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**price_info** | [**DiscountPriceInfoResponse**](DiscountPriceInfoResponse.md) |  | [optional] 

## Example

```python
from linebot.v3.messaging.models.coupon_discount_reward_response import CouponDiscountRewardResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CouponDiscountRewardResponse from a JSON string
coupon_discount_reward_response_instance = CouponDiscountRewardResponse.from_json(json)
# print the JSON string representation of the object
print CouponDiscountRewardResponse.to_json()

# convert the object into a dict
coupon_discount_reward_response_dict = coupon_discount_reward_response_instance.to_dict()
# create an instance of CouponDiscountRewardResponse from a dict
coupon_discount_reward_response_form_dict = coupon_discount_reward_response.from_dict(coupon_discount_reward_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


