# AgeTile


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**age** | **str** | users&#39; age | [optional] 
**percentage** | **float** | Percentage | [optional] 

## Example

```python
from linebot.v3.insight.models.age_tile import AgeTile

# TODO update the JSON string below
json = "{}"
# create an instance of AgeTile from a JSON string
age_tile_instance = AgeTile.from_json(json)
# print the JSON string representation of the object
print AgeTile.to_json()

# convert the object into a dict
age_tile_dict = age_tile_instance.to_dict()
# create an instance of AgeTile from a dict
age_tile_form_dict = age_tile.from_dict(age_tile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


