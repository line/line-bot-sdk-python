# GetMembershipSubscriptionResponse

A user's membership subscription status

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subscriptions** | [**List[Subscription]**](Subscription.md) | List of subscription information | 

## Example

```python
from linebot.v3.messaging.models.get_membership_subscription_response import GetMembershipSubscriptionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetMembershipSubscriptionResponse from a JSON string
get_membership_subscription_response_instance = GetMembershipSubscriptionResponse.from_json(json)
# print the JSON string representation of the object
print GetMembershipSubscriptionResponse.to_json()

# convert the object into a dict
get_membership_subscription_response_dict = get_membership_subscription_response_instance.to_dict()
# create an instance of GetMembershipSubscriptionResponse from a dict
get_membership_subscription_response_form_dict = get_membership_subscription_response.from_dict(get_membership_subscription_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


