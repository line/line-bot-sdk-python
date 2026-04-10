# GetStatisticsPerUnitResponse

Response object for `get statistics per unit`

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**overview** | [**GetStatisticsPerUnitResponseOverview**](GetStatisticsPerUnitResponseOverview.md) |  | 
**messages** | [**List[GetStatisticsPerUnitResponseMessage]**](GetStatisticsPerUnitResponseMessage.md) | Array of information about individual message bubbles. | 
**clicks** | [**List[GetStatisticsPerUnitResponseClick]**](GetStatisticsPerUnitResponseClick.md) | Array of information about opened URLs in the message. | 

## Example

```python
from linebot.v3.insight.models.get_statistics_per_unit_response import GetStatisticsPerUnitResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetStatisticsPerUnitResponse from a JSON string
get_statistics_per_unit_response_instance = GetStatisticsPerUnitResponse.from_json(json)
# print the JSON string representation of the object
print GetStatisticsPerUnitResponse.to_json()

# convert the object into a dict
get_statistics_per_unit_response_dict = get_statistics_per_unit_response_instance.to_dict()
# create an instance of GetStatisticsPerUnitResponse from a dict
get_statistics_per_unit_response_form_dict = get_statistics_per_unit_response.from_dict(get_statistics_per_unit_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


