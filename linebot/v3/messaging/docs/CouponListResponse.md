# CouponListResponse

Summary information about a coupon, used in coupon lists.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coupon_id** | **str** | Unique identifier of the coupon. | 
**title** | **str** | Title of the coupon. Displayed in the coupon list. | 

## Example

```python
from linebot.v3.messaging.models.coupon_list_response import CouponListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CouponListResponse from a JSON string
coupon_list_response_instance = CouponListResponse.from_json(json)
# print the JSON string representation of the object
print CouponListResponse.to_json()

# convert the object into a dict
coupon_list_response_dict = coupon_list_response_instance.to_dict()
# create an instance of CouponListResponse from a dict
coupon_list_response_form_dict = coupon_list_response.from_dict(coupon_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


