# AgeDemographicFilter


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gte** | [**AgeDemographic**](AgeDemographic.md) |  | [optional] 
**lt** | [**AgeDemographic**](AgeDemographic.md) |  | [optional] 

## Example

```python
from linebot.v3.messaging.models.age_demographic_filter import AgeDemographicFilter

# TODO update the JSON string below
json = "{}"
# create an instance of AgeDemographicFilter from a JSON string
age_demographic_filter_instance = AgeDemographicFilter.from_json(json)
# print the JSON string representation of the object
print AgeDemographicFilter.to_json()

# convert the object into a dict
age_demographic_filter_dict = age_demographic_filter_instance.to_dict()
# create an instance of AgeDemographicFilter from a dict
age_demographic_filter_form_dict = age_demographic_filter.from_dict(age_demographic_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


