# GroupUserProfileResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | User&#39;s display name | 
**user_id** | **str** | User ID | 
**picture_url** | **str** | Profile image URL. &#x60;https&#x60; image URL. Not included in the response if the user doesn&#39;t have a profile image. | [optional] 

## Example

```python
from linebot.v3.messaging.models.group_user_profile_response import GroupUserProfileResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GroupUserProfileResponse from a JSON string
group_user_profile_response_instance = GroupUserProfileResponse.from_json(json)
# print the JSON string representation of the object
print GroupUserProfileResponse.to_json()

# convert the object into a dict
group_user_profile_response_dict = group_user_profile_response_instance.to_dict()
# create an instance of GroupUserProfileResponse from a dict
group_user_profile_response_form_dict = group_user_profile_response.from_dict(group_user_profile_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


