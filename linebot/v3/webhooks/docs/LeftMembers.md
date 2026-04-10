# LeftMembers


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**members** | [**List[UserSource]**](UserSource.md) | Users who left. Array of source user objects. | 

## Example

```python
from linebot.v3.webhooks.models.left_members import LeftMembers

# TODO update the JSON string below
json = "{}"
# create an instance of LeftMembers from a JSON string
left_members_instance = LeftMembers.from_json(json)
# print the JSON string representation of the object
print LeftMembers.to_json()

# convert the object into a dict
left_members_dict = left_members_instance.to_dict()
# create an instance of LeftMembers from a dict
left_members_form_dict = left_members.from_dict(left_members_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


