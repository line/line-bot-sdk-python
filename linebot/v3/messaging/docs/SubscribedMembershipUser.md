# SubscribedMembershipUser

Object containing user membership subscription information.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**membership_no** | **int** | The user&#39;s member number in the membership plan. | 
**joined_time** | **int** | UNIX timestamp at which the user subscribed to the membership. | 
**next_billing_date** | **str** | Next payment date for membership plan. - Format: yyyy-MM-dd (e.g. 2024-02-08) - Timezone: UTC+9  | 
**total_subscription_months** | **int** | The period of time in months that the user has been subscribed to a membership plan. If a user previously canceled and then re-subscribed to the same membership plan, only the period after the re-subscription will be counted. | 

## Example

```python
from linebot.v3.messaging.models.subscribed_membership_user import SubscribedMembershipUser

# TODO update the JSON string below
json = "{}"
# create an instance of SubscribedMembershipUser from a JSON string
subscribed_membership_user_instance = SubscribedMembershipUser.from_json(json)
# print the JSON string representation of the object
print SubscribedMembershipUser.to_json()

# convert the object into a dict
subscribed_membership_user_dict = subscribed_membership_user_instance.to_dict()
# create an instance of SubscribedMembershipUser from a dict
subscribed_membership_user_form_dict = subscribed_membership_user.from_dict(subscribed_membership_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


