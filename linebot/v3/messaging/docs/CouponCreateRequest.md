# CouponCreateRequest

Request object for creating a coupon. Contains all configurable coupon properties.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acquisition_condition** | [**AcquisitionConditionRequest**](AcquisitionConditionRequest.md) |  | 
**barcode_image_url** | **str** | URL of the barcode image associated with the coupon. Used for in-store redemption. | [optional] 
**coupon_code** | **str** | Unique code to be presented by the user to redeem the coupon. Optional. | [optional] 
**description** | **str** | Detailed description of the coupon. Displayed to users. | [optional] 
**end_timestamp** | **int** | Coupon expiration time (epoch seconds). Coupon cannot be used after this time. | 
**image_url** | **str** | URL of the main image representing the coupon. Displayed in the coupon list. | [optional] 
**max_use_count_per_ticket** | **int** | Maximum number of times a single coupon ticket can be used. Use -1 to indicate no limit. | 
**start_timestamp** | **int** | Coupon start time (epoch seconds). Coupon can be used from this time. | 
**title** | **str** | Title of the coupon. Displayed in the coupon list. | 
**usage_condition** | **str** | Conditions for using the coupon. Shown to users. | [optional] 
**reward** | [**CouponRewardRequest**](CouponRewardRequest.md) |  | [optional] 
**visibility** | **str** | Visibility of the coupon. Determines who can see or acquire the coupon. | 
**timezone** | **str** | Timezone for interpreting start and end timestamps. | 

## Example

```python
from linebot.v3.messaging.models.coupon_create_request import CouponCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CouponCreateRequest from a JSON string
coupon_create_request_instance = CouponCreateRequest.from_json(json)
# print the JSON string representation of the object
print CouponCreateRequest.to_json()

# convert the object into a dict
coupon_create_request_dict = coupon_create_request_instance.to_dict()
# create an instance of CouponCreateRequest from a dict
coupon_create_request_form_dict = coupon_create_request.from_dict(coupon_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


