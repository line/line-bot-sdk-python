# UserProfileResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | User&#39;s display name | 
**user_id** | **str** | User ID | 
**picture_url** | **str** | Profile image URL. &#x60;https&#x60; image URL. Not included in the response if the user doesn&#39;t have a profile image. | [optional] 
**status_message** | **str** | User&#39;s status message. Not included in the response if the user doesn&#39;t have a status message. | [optional] 
**language** | **str** | User&#39;s language, as a BCP 47 language tag. Not included in the response if the user hasn&#39;t yet consented to the LINE Privacy Policy. | [optional] 

## Example

```python
from linebot.v3.messaging.models.user_profile_response import UserProfileResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserProfileResponse from a JSON string
user_profile_response_instance = UserProfileResponse.from_json(json)
# print the JSON string representation of the object
print UserProfileResponse.to_json()

# convert the object into a dict
user_profile_response_dict = user_profile_response_instance.to_dict()
# create an instance of UserProfileResponse from a dict
user_profile_response_form_dict = user_profile_response.from_dict(user_profile_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


