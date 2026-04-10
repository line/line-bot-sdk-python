# OperatorDemographicFilter


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_and** | [**List[DemographicFilter]**](DemographicFilter.md) |  | [optional] 
**var_or** | [**List[DemographicFilter]**](DemographicFilter.md) |  | [optional] 
**var_not** | [**DemographicFilter**](DemographicFilter.md) |  | [optional] 

## Example

```python
from linebot.v3.messaging.models.operator_demographic_filter import OperatorDemographicFilter

# TODO update the JSON string below
json = "{}"
# create an instance of OperatorDemographicFilter from a JSON string
operator_demographic_filter_instance = OperatorDemographicFilter.from_json(json)
# print the JSON string representation of the object
print OperatorDemographicFilter.to_json()

# convert the object into a dict
operator_demographic_filter_dict = operator_demographic_filter_instance.to_dict()
# create an instance of OperatorDemographicFilter from a dict
operator_demographic_filter_form_dict = operator_demographic_filter.from_dict(operator_demographic_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


