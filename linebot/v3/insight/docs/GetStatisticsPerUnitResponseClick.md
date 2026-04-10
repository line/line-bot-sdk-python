# GetStatisticsPerUnitResponseClick


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**seq** | **int** | The URL&#39;s serial number. | 
**url** | **str** | URL. | 
**click** | **int** | Number of times the URL in the bubble was opened. | [optional] 
**unique_click** | **int** | Number of users that opened the URL in the bubble. | [optional] 
**unique_click_of_request** | **int** | Number of users who opened this url through any link in the message. If another message bubble contains the same URL and a user opens both links, it&#39;s counted only once.  | [optional] 

## Example

```python
from linebot.v3.insight.models.get_statistics_per_unit_response_click import GetStatisticsPerUnitResponseClick

# TODO update the JSON string below
json = "{}"
# create an instance of GetStatisticsPerUnitResponseClick from a JSON string
get_statistics_per_unit_response_click_instance = GetStatisticsPerUnitResponseClick.from_json(json)
# print the JSON string representation of the object
print GetStatisticsPerUnitResponseClick.to_json()

# convert the object into a dict
get_statistics_per_unit_response_click_dict = get_statistics_per_unit_response_click_instance.to_dict()
# create an instance of GetStatisticsPerUnitResponseClick from a dict
get_statistics_per_unit_response_click_form_dict = get_statistics_per_unit_response_click.from_dict(get_statistics_per_unit_response_click_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


