# SubscribedMembershipPlan

Object containing information about the membership plan.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**membership_id** | **int** | Membership plan ID. | 
**title** | **str** | Membership plan name. | 
**description** | **str** | Membership plan description. | 
**benefits** | **List[str]** | List of membership plan perks. | 
**price** | **float** | Monthly fee for membership plan. (e.g. 1500.00) | 
**currency** | **str** | The currency of membership.price. | 

## Example

```python
from linebot.v3.messaging.models.subscribed_membership_plan import SubscribedMembershipPlan

# TODO update the JSON string below
json = "{}"
# create an instance of SubscribedMembershipPlan from a JSON string
subscribed_membership_plan_instance = SubscribedMembershipPlan.from_json(json)
# print the JSON string representation of the object
print SubscribedMembershipPlan.to_json()

# convert the object into a dict
subscribed_membership_plan_dict = subscribed_membership_plan_instance.to_dict()
# create an instance of SubscribedMembershipPlan from a dict
subscribed_membership_plan_form_dict = subscribed_membership_plan.from_dict(subscribed_membership_plan_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


