# DemographicFilter

Demographic filter

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of demographic filter | [optional] 

## Example

```python
from linebot.v3.messaging.models.demographic_filter import DemographicFilter

# TODO update the JSON string below
json = "{}"
# create an instance of DemographicFilter from a JSON string
demographic_filter_instance = DemographicFilter.from_json(json)
# print the JSON string representation of the object
print DemographicFilter.to_json()

# convert the object into a dict
demographic_filter_dict = demographic_filter_instance.to_dict()
# create an instance of DemographicFilter from a dict
demographic_filter_form_dict = demographic_filter.from_dict(demographic_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


