# Subscription

An array of memberships.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**membership** | [**SubscribedMembershipPlan**](SubscribedMembershipPlan.md) |  | 
**user** | [**SubscribedMembershipUser**](SubscribedMembershipUser.md) |  | 

## Example

```python
from linebot.v3.messaging.models.subscription import Subscription

# TODO update the JSON string below
json = "{}"
# create an instance of Subscription from a JSON string
subscription_instance = Subscription.from_json(json)
# print the JSON string representation of the object
print Subscription.to_json()

# convert the object into a dict
subscription_dict = subscription_instance.to_dict()
# create an instance of Subscription from a dict
subscription_form_dict = subscription.from_dict(subscription_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


