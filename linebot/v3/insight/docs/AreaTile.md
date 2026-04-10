# AreaTile


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**area** | **str** | users&#39; country and region | [optional] 
**percentage** | **float** | Percentage | [optional] 

## Example

```python
from linebot.v3.insight.models.area_tile import AreaTile

# TODO update the JSON string below
json = "{}"
# create an instance of AreaTile from a JSON string
area_tile_instance = AreaTile.from_json(json)
# print the JSON string representation of the object
print AreaTile.to_json()

# convert the object into a dict
area_tile_dict = area_tile_instance.to_dict()
# create an instance of AreaTile from a dict
area_tile_form_dict = area_tile.from_dict(area_tile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


