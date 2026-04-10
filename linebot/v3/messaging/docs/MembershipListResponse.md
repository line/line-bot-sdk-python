# MembershipListResponse

List of memberships

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**memberships** | [**List[Membership]**](Membership.md) | List of membership information | 

## Example

```python
from linebot.v3.messaging.models.membership_list_response import MembershipListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MembershipListResponse from a JSON string
membership_list_response_instance = MembershipListResponse.from_json(json)
# print the JSON string representation of the object
print MembershipListResponse.to_json()

# convert the object into a dict
membership_list_response_dict = membership_list_response_instance.to_dict()
# create an instance of MembershipListResponse from a dict
membership_list_response_form_dict = membership_list_response.from_dict(membership_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


