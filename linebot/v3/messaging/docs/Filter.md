# Filter

Filter for narrowcast

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**demographic** | [**DemographicFilter**](DemographicFilter.md) |  | [optional] 

## Example

```python
from linebot.v3.messaging.models.filter import Filter

# TODO update the JSON string below
json = "{}"
# create an instance of Filter from a JSON string
filter_instance = Filter.from_json(json)
# print the JSON string representation of the object
print Filter.to_json()

# convert the object into a dict
filter_dict = filter_instance.to_dict()
# create an instance of Filter from a dict
filter_form_dict = filter.from_dict(filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


