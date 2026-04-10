# GetStatisticsPerUnitResponseMessage


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**seq** | **int** | Bubble&#39;s serial number. | 
**impression** | **int** | Number of times the bubble was displayed. | [optional] 
**media_played** | **int** | Number of times audio or video in the bubble started playing. | [optional] 
**media_played25_percent** | **int** | Number of times audio or video in the bubble started playing and was played 25% of the total time. | [optional] 
**media_played50_percent** | **int** | Number of times audio or video in the bubble started playing and was played 50% of the total time. | [optional] 
**media_played75_percent** | **int** | Number of times audio or video in the bubble started playing and was played 75% of the total time. | [optional] 
**media_played100_percent** | **int** | Number of times audio or video in the bubble started playing and was played 100% of the total time. | [optional] 
**unique_impression** | **int** | Number of users the bubble was displayed. | [optional] 
**unique_media_played** | **int** | Number of users that started playing audio or video in the bubble. | [optional] 
**unique_media_played25_percent** | **int** | Number of users that started playing audio or video in the bubble and played 25% of the total time. | [optional] 
**unique_media_played50_percent** | **int** | Number of users that started playing audio or video in the bubble and played 50% of the total time. | [optional] 
**unique_media_played75_percent** | **int** | Number of users that started playing audio or video in the bubble and played 75% of the total time. | [optional] 
**unique_media_played100_percent** | **int** | Number of users that started playing audio or video in the bubble and played 100% of the total time. | [optional] 

## Example

```python
from linebot.v3.insight.models.get_statistics_per_unit_response_message import GetStatisticsPerUnitResponseMessage

# TODO update the JSON string below
json = "{}"
# create an instance of GetStatisticsPerUnitResponseMessage from a JSON string
get_statistics_per_unit_response_message_instance = GetStatisticsPerUnitResponseMessage.from_json(json)
# print the JSON string representation of the object
print GetStatisticsPerUnitResponseMessage.to_json()

# convert the object into a dict
get_statistics_per_unit_response_message_dict = get_statistics_per_unit_response_message_instance.to_dict()
# create an instance of GetStatisticsPerUnitResponseMessage from a dict
get_statistics_per_unit_response_message_form_dict = get_statistics_per_unit_response_message.from_dict(get_statistics_per_unit_response_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


