# LeftMembershipContent


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**membership_id** | **int** | The ID of the membership that the user left. This is defined for each membership. | 

## Example

```python
from linebot.v3.webhooks.models.left_membership_content import LeftMembershipContent

# TODO update the JSON string below
json = "{}"
# create an instance of LeftMembershipContent from a JSON string
left_membership_content_instance = LeftMembershipContent.from_json(json)
# print the JSON string representation of the object
print LeftMembershipContent.to_json()

# convert the object into a dict
left_membership_content_dict = left_membership_content_instance.to_dict()
# create an instance of LeftMembershipContent from a dict
left_membership_content_form_dict = left_membership_content.from_dict(left_membership_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


