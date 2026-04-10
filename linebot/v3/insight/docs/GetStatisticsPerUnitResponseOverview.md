# GetStatisticsPerUnitResponseOverview

Statistics related to messages.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unique_impression** | **int** | Number of users who opened the message, meaning they displayed at least 1 bubble. | [optional] 
**unique_click** | **int** | Number of users who opened any URL in the message. | [optional] 
**unique_media_played** | **int** | Number of users who started playing any video or audio in the message. | [optional] 
**unique_media_played100_percent** | **int** | Number of users who played the entirety of any video or audio in the message. | [optional] 

## Example

```python
from linebot.v3.insight.models.get_statistics_per_unit_response_overview import GetStatisticsPerUnitResponseOverview

# TODO update the JSON string below
json = "{}"
# create an instance of GetStatisticsPerUnitResponseOverview from a JSON string
get_statistics_per_unit_response_overview_instance = GetStatisticsPerUnitResponseOverview.from_json(json)
# print the JSON string representation of the object
print GetStatisticsPerUnitResponseOverview.to_json()

# convert the object into a dict
get_statistics_per_unit_response_overview_dict = get_statistics_per_unit_response_overview_instance.to_dict()
# create an instance of GetStatisticsPerUnitResponseOverview from a dict
get_statistics_per_unit_response_overview_form_dict = get_statistics_per_unit_response_overview.from_dict(get_statistics_per_unit_response_overview_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


