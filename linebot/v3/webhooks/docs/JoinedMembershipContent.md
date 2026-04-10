# JoinedMembershipContent


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**membership_id** | **int** | The ID of the membership that the user joined. This is defined for each membership. | 

## Example

```python
from linebot.v3.webhooks.models.joined_membership_content import JoinedMembershipContent

# TODO update the JSON string below
json = "{}"
# create an instance of JoinedMembershipContent from a JSON string
joined_membership_content_instance = JoinedMembershipContent.from_json(json)
# print the JSON string representation of the object
print JoinedMembershipContent.to_json()

# convert the object into a dict
joined_membership_content_dict = joined_membership_content_instance.to_dict()
# create an instance of JoinedMembershipContent from a dict
joined_membership_content_form_dict = joined_membership_content.from_dict(joined_membership_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


