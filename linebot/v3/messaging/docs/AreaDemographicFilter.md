# AreaDemographicFilter


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**one_of** | [**List[AreaDemographic]**](AreaDemographic.md) |  | [optional] 

## Example

```python
from linebot.v3.messaging.models.area_demographic_filter import AreaDemographicFilter

# TODO update the JSON string below
json = "{}"
# create an instance of AreaDemographicFilter from a JSON string
area_demographic_filter_instance = AreaDemographicFilter.from_json(json)
# print the JSON string representation of the object
print AreaDemographicFilter.to_json()

# convert the object into a dict
area_demographic_filter_dict = area_demographic_filter_instance.to_dict()
# create an instance of AreaDemographicFilter from a dict
area_demographic_filter_form_dict = area_demographic_filter.from_dict(area_demographic_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


