# GenderTile


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gender** | **str** | users&#39; gender | [optional] 
**percentage** | **float** | Percentage | [optional] 

## Example

```python
from linebot.v3.insight.models.gender_tile import GenderTile

# TODO update the JSON string below
json = "{}"
# create an instance of GenderTile from a JSON string
gender_tile_instance = GenderTile.from_json(json)
# print the JSON string representation of the object
print GenderTile.to_json()

# convert the object into a dict
gender_tile_dict = gender_tile_instance.to_dict()
# create an instance of GenderTile from a dict
gender_tile_form_dict = gender_tile.from_dict(gender_tile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


