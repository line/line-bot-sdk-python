# GetFriendsDemographicsResponse

Get friend demographics

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available** | **bool** | true if friend demographic information is available. | [optional] 
**genders** | [**List[GenderTile]**](GenderTile.md) | Percentage per gender. | [optional] 
**ages** | [**List[AgeTile]**](AgeTile.md) | Percentage per age group. | [optional] 
**areas** | [**List[AreaTile]**](AreaTile.md) | Percentage per area. | [optional] 
**app_types** | [**List[AppTypeTile]**](AppTypeTile.md) | Percentage by OS. | [optional] 
**subscription_periods** | [**List[SubscriptionPeriodTile]**](SubscriptionPeriodTile.md) | Percentage per friendship duration. | [optional] 

## Example

```python
from linebot.v3.insight.models.get_friends_demographics_response import GetFriendsDemographicsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetFriendsDemographicsResponse from a JSON string
get_friends_demographics_response_instance = GetFriendsDemographicsResponse.from_json(json)
# print the JSON string representation of the object
print GetFriendsDemographicsResponse.to_json()

# convert the object into a dict
get_friends_demographics_response_dict = get_friends_demographics_response_instance.to_dict()
# create an instance of GetFriendsDemographicsResponse from a dict
get_friends_demographics_response_form_dict = get_friends_demographics_response.from_dict(get_friends_demographics_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


