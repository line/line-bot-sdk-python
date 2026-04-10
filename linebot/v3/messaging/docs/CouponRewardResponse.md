# CouponRewardResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of coupon. Determines the benefit provided. | 

## Example

```python
from linebot.v3.messaging.models.coupon_reward_response import CouponRewardResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CouponRewardResponse from a JSON string
coupon_reward_response_instance = CouponRewardResponse.from_json(json)
# print the JSON string representation of the object
print CouponRewardResponse.to_json()

# convert the object into a dict
coupon_reward_response_dict = coupon_reward_response_instance.to_dict()
# create an instance of CouponRewardResponse from a dict
coupon_reward_response_form_dict = coupon_reward_response.from_dict(coupon_reward_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


