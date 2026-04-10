# RichMenuSize

Rich menu size

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**width** | **int** | width | [optional] 
**height** | **int** | height | [optional] 

## Example

```python
from linebot.v3.messaging.models.rich_menu_size import RichMenuSize

# TODO update the JSON string below
json = "{}"
# create an instance of RichMenuSize from a JSON string
rich_menu_size_instance = RichMenuSize.from_json(json)
# print the JSON string representation of the object
print RichMenuSize.to_json()

# convert the object into a dict
rich_menu_size_dict = rich_menu_size_instance.to_dict()
# create an instance of RichMenuSize from a dict
rich_menu_size_form_dict = rich_menu_size.from_dict(rich_menu_size_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


