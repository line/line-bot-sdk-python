# Membership


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**membership_id** | **int** | Membership plan ID. | 
**title** | **str** | Membership plan name. | 
**description** | **str** | Membership plan description. | 
**benefits** | **List[str]** | List of membership plan perks. | 
**price** | **float** | Monthly fee for membership plan. (e.g. 1500.00) | 
**currency** | **str** | The currency of membership.price. | 
**member_count** | **int** | Number of members subscribed to the membership plan. | 
**member_limit** | **int** | The upper limit of members who can subscribe. If no upper limit is set, it will be null. | 
**is_in_app_purchase** | **bool** | Payment method for users who subscribe to a membership plan. | 
**is_published** | **bool** | Membership plan status. | 

## Example

```python
from linebot.v3.messaging.models.membership import Membership

# TODO update the JSON string below
json = "{}"
# create an instance of Membership from a JSON string
membership_instance = Membership.from_json(json)
# print the JSON string representation of the object
print Membership.to_json()

# convert the object into a dict
membership_dict = membership_instance.to_dict()
# create an instance of Membership from a dict
membership_form_dict = membership.from_dict(membership_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


