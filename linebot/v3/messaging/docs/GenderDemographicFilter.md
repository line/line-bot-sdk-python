# GenderDemographicFilter


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**one_of** | [**List[GenderDemographic]**](GenderDemographic.md) |  | [optional] 

## Example

```python
from linebot.v3.messaging.models.gender_demographic_filter import GenderDemographicFilter

# TODO update the JSON string below
json = "{}"
# create an instance of GenderDemographicFilter from a JSON string
gender_demographic_filter_instance = GenderDemographicFilter.from_json(json)
# print the JSON string representation of the object
print GenderDemographicFilter.to_json()

# convert the object into a dict
gender_demographic_filter_dict = gender_demographic_filter_instance.to_dict()
# create an instance of GenderDemographicFilter from a dict
gender_demographic_filter_form_dict = gender_demographic_filter.from_dict(gender_demographic_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


