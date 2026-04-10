# GetNumberOfFollowersResponse

Get number of followers

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Calculation status. | [optional] 
**followers** | **int** | The number of times, as of the specified date, that a user added this LINE Official Account as a friend for the first time. The number doesn&#39;t decrease even if a user later blocks the account or when they delete their LINE account.  | [optional] 
**targeted_reaches** | **int** | The number of users, as of the specified date, that the LINE Official Account can reach through targeted messages based on gender, age, and/or region. This number only includes users who are active on LINE or LINE services and whose demographics have a high level of certainty.  | [optional] 
**blocks** | **int** | The number of users blocking the account as of the specified date. The number decreases when a user unblocks the account.    | [optional] 

## Example

```python
from linebot.v3.insight.models.get_number_of_followers_response import GetNumberOfFollowersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetNumberOfFollowersResponse from a JSON string
get_number_of_followers_response_instance = GetNumberOfFollowersResponse.from_json(json)
# print the JSON string representation of the object
print GetNumberOfFollowersResponse.to_json()

# convert the object into a dict
get_number_of_followers_response_dict = get_number_of_followers_response_instance.to_dict()
# create an instance of GetNumberOfFollowersResponse from a dict
get_number_of_followers_response_form_dict = get_number_of_followers_response.from_dict(get_number_of_followers_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


