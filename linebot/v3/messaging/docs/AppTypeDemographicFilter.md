# AppTypeDemographicFilter


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**one_of** | [**List[AppTypeDemographic]**](AppTypeDemographic.md) |  | [optional] 

## Example

```python
from linebot.v3.messaging.models.app_type_demographic_filter import AppTypeDemographicFilter

# TODO update the JSON string below
json = "{}"
# create an instance of AppTypeDemographicFilter from a JSON string
app_type_demographic_filter_instance = AppTypeDemographicFilter.from_json(json)
# print the JSON string representation of the object
print AppTypeDemographicFilter.to_json()

# convert the object into a dict
app_type_demographic_filter_dict = app_type_demographic_filter_instance.to_dict()
# create an instance of AppTypeDemographicFilter from a dict
app_type_demographic_filter_form_dict = app_type_demographic_filter.from_dict(app_type_demographic_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


