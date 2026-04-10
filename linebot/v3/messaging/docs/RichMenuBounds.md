# RichMenuBounds

Rich menu bounds

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**x** | **int** | Horizontal position relative to the top-left corner of the area. | [optional] 
**y** | **int** | Vertical position relative to the top-left corner of the area. | [optional] 
**width** | **int** | Width of the area. | [optional] 
**height** | **int** | Height of the area. | [optional] 

## Example

```python
from linebot.v3.messaging.models.rich_menu_bounds import RichMenuBounds

# TODO update the JSON string below
json = "{}"
# create an instance of RichMenuBounds from a JSON string
rich_menu_bounds_instance = RichMenuBounds.from_json(json)
# print the JSON string representation of the object
print RichMenuBounds.to_json()

# convert the object into a dict
rich_menu_bounds_dict = rich_menu_bounds_instance.to_dict()
# create an instance of RichMenuBounds from a dict
rich_menu_bounds_form_dict = rich_menu_bounds.from_dict(rich_menu_bounds_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


