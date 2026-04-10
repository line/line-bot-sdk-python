# AppTypeTile


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_type** | **str** | users&#39; OS | [optional] 
**percentage** | **float** | Percentage | [optional] 

## Example

```python
from linebot.v3.insight.models.app_type_tile import AppTypeTile

# TODO update the JSON string below
json = "{}"
# create an instance of AppTypeTile from a JSON string
app_type_tile_instance = AppTypeTile.from_json(json)
# print the JSON string representation of the object
print AppTypeTile.to_json()

# convert the object into a dict
app_type_tile_dict = app_type_tile_instance.to_dict()
# create an instance of AppTypeTile from a dict
app_type_tile_form_dict = app_type_tile.from_dict(app_type_tile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


