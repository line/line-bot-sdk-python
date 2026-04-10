# MembershipContent

Content of the membership event.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of membership event. | 

## Example

```python
from linebot.v3.webhooks.models.membership_content import MembershipContent

# TODO update the JSON string below
json = "{}"
# create an instance of MembershipContent from a JSON string
membership_content_instance = MembershipContent.from_json(json)
# print the JSON string representation of the object
print MembershipContent.to_json()

# convert the object into a dict
membership_content_dict = membership_content_instance.to_dict()
# create an instance of MembershipContent from a dict
membership_content_form_dict = membership_content.from_dict(membership_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


