# MessagingApiPagerCouponListResponse

Paginated response object containing a list of coupons.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[CouponListResponse]**](CouponListResponse.md) | List of coupon summary objects. | 
**next** | **str** | Token for fetching the next page of results. | [optional] 

## Example

```python
from linebot.v3.messaging.models.messaging_api_pager_coupon_list_response import MessagingApiPagerCouponListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MessagingApiPagerCouponListResponse from a JSON string
messaging_api_pager_coupon_list_response_instance = MessagingApiPagerCouponListResponse.from_json(json)
# print the JSON string representation of the object
print MessagingApiPagerCouponListResponse.to_json()

# convert the object into a dict
messaging_api_pager_coupon_list_response_dict = messaging_api_pager_coupon_list_response_instance.to_dict()
# create an instance of MessagingApiPagerCouponListResponse from a dict
messaging_api_pager_coupon_list_response_form_dict = messaging_api_pager_coupon_list_response.from_dict(messaging_api_pager_coupon_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


