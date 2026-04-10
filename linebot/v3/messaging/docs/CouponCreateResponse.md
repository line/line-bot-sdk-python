# CouponCreateResponse

Response object returned after creating a coupon. Contains the coupon ID.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coupon_id** | **str** | Unique identifier of the coupon. | 

## Example

```python
from linebot.v3.messaging.models.coupon_create_response import CouponCreateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CouponCreateResponse from a JSON string
coupon_create_response_instance = CouponCreateResponse.from_json(json)
# print the JSON string representation of the object
print CouponCreateResponse.to_json()

# convert the object into a dict
coupon_create_response_dict = coupon_create_response_instance.to_dict()
# create an instance of CouponCreateResponse from a dict
coupon_create_response_form_dict = coupon_create_response.from_dict(coupon_create_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


