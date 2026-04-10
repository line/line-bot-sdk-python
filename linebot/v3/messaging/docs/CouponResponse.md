# CouponResponse

Detailed information about a coupon, including all properties and current status.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acquisition_condition** | [**AcquisitionConditionResponse**](AcquisitionConditionResponse.md) |  | [optional] 
**barcode_image_url** | **str** | URL of the barcode image associated with the coupon. Used for in-store redemption. | [optional] 
**coupon_code** | **str** | Unique code to be presented by the user to redeem the coupon. | [optional] 
**description** | **str** | Detailed description of the coupon. Displayed to users. | [optional] 
**end_timestamp** | **int** | Coupon expiration time (epoch seconds). Coupon cannot be used after this time. | [optional] 
**image_url** | **str** | URL of the main image representing the coupon. Displayed in the coupon list. | [optional] 
**max_acquire_count** | **int** | Maximum number of coupons that can be issued in total. | [optional] 
**max_use_count_per_ticket** | **int** | Maximum number of times a single coupon ticket can be used. | [optional] 
**max_ticket_per_user** | **int** | Maximum number of coupon tickets a single user can acquire. | [optional] 
**start_timestamp** | **int** | Coupon start time (epoch seconds). Coupon can be used from this time. | [optional] 
**title** | **str** | Title of the coupon. Displayed in the coupon list. | [optional] 
**usage_condition** | **str** | Conditions for using the coupon. Shown to users. | [optional] 
**reward** | [**CouponRewardResponse**](CouponRewardResponse.md) |  | [optional] 
**visibility** | **str** | Visibility of the coupon. Determines who can see or acquire the coupon. | [optional] 
**timezone** | **str** | Timezone for interpreting start and end timestamps. | [optional] 
**coupon_id** | **str** | Unique identifier of the coupon. | [optional] 
**created_timestamp** | **int** | Created timestamp (seconds) of the coupon. | [optional] 
**status** | **str** | Current status of the coupon. | [optional] 

## Example

```python
from linebot.v3.messaging.models.coupon_response import CouponResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CouponResponse from a JSON string
coupon_response_instance = CouponResponse.from_json(json)
# print the JSON string representation of the object
print CouponResponse.to_json()

# convert the object into a dict
coupon_response_dict = coupon_response_instance.to_dict()
# create an instance of CouponResponse from a dict
coupon_response_form_dict = coupon_response.from_dict(coupon_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


