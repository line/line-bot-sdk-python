# GetAggregationUnitUsageResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**num_of_custom_aggregation_units** | **int** | Number of aggregation units used this month. | 

## Example

```python
from linebot.v3.messaging.models.get_aggregation_unit_usage_response import GetAggregationUnitUsageResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetAggregationUnitUsageResponse from a JSON string
get_aggregation_unit_usage_response_instance = GetAggregationUnitUsageResponse.from_json(json)
# print the JSON string representation of the object
print GetAggregationUnitUsageResponse.to_json()

# convert the object into a dict
get_aggregation_unit_usage_response_dict = get_aggregation_unit_usage_response_instance.to_dict()
# create an instance of GetAggregationUnitUsageResponse from a dict
get_aggregation_unit_usage_response_form_dict = get_aggregation_unit_usage_response.from_dict(get_aggregation_unit_usage_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


