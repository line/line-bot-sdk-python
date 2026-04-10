# RenewedMembershipContent


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**membership_id** | **int** | The ID of the membership that the user renewed. This is defined for each membership. | 

## Example

```python
from linebot.v3.webhooks.models.renewed_membership_content import RenewedMembershipContent

# TODO update the JSON string below
json = "{}"
# create an instance of RenewedMembershipContent from a JSON string
renewed_membership_content_instance = RenewedMembershipContent.from_json(json)
# print the JSON string representation of the object
print RenewedMembershipContent.to_json()

# convert the object into a dict
renewed_membership_content_dict = renewed_membership_content_instance.to_dict()
# create an instance of RenewedMembershipContent from a dict
renewed_membership_content_form_dict = renewed_membership_content.from_dict(renewed_membership_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


