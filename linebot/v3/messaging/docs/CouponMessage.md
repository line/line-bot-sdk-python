# CouponMessage


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coupon_id** | **str** | Unique identifier of the coupon. | 
**delivery_tag** | **str** | Delivery route tag information. It can be used for analysis in LINE OA Manager. | [optional] 

## Example

```python
from linebot.v3.messaging.models.coupon_message import CouponMessage

# TODO update the JSON string below
json = "{}"
# create an instance of CouponMessage from a JSON string
coupon_message_instance = CouponMessage.from_json(json)
# print the JSON string representation of the object
print CouponMessage.to_json()

# convert the object into a dict
coupon_message_dict = coupon_message_instance.to_dict()
# create an instance of CouponMessage from a dict
coupon_message_form_dict = coupon_message.from_dict(coupon_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


