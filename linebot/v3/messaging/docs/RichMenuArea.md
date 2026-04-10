# RichMenuArea

Rich menu area

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bounds** | [**RichMenuBounds**](RichMenuBounds.md) |  | [optional] 
**action** | [**Action**](Action.md) |  | [optional] 

## Example

```python
from linebot.v3.messaging.models.rich_menu_area import RichMenuArea

# TODO update the JSON string below
json = "{}"
# create an instance of RichMenuArea from a JSON string
rich_menu_area_instance = RichMenuArea.from_json(json)
# print the JSON string representation of the object
print RichMenuArea.to_json()

# convert the object into a dict
rich_menu_area_dict = rich_menu_area_instance.to_dict()
# create an instance of RichMenuArea from a dict
rich_menu_area_form_dict = rich_menu_area.from_dict(rich_menu_area_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


