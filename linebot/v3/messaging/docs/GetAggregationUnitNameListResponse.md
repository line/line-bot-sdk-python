# GetAggregationUnitNameListResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**custom_aggregation_units** | **List[str]** | An array of strings indicating the names of aggregation units used this month. | 
**next** | **str** | A continuation token to get the next array of unit names. Returned only when there are remaining aggregation units that weren&#39;t returned in customAggregationUnits in the original request.   | [optional] 

## Example

```python
from linebot.v3.messaging.models.get_aggregation_unit_name_list_response import GetAggregationUnitNameListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetAggregationUnitNameListResponse from a JSON string
get_aggregation_unit_name_list_response_instance = GetAggregationUnitNameListResponse.from_json(json)
# print the JSON string representation of the object
print GetAggregationUnitNameListResponse.to_json()

# convert the object into a dict
get_aggregation_unit_name_list_response_dict = get_aggregation_unit_name_list_response_instance.to_dict()
# create an instance of GetAggregationUnitNameListResponse from a dict
get_aggregation_unit_name_list_response_form_dict = get_aggregation_unit_name_list_response.from_dict(get_aggregation_unit_name_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


