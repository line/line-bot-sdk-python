# CarouselColumn

Column object for carousel template.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**thumbnail_image_url** | **str** |  | [optional] 
**image_background_color** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**text** | **str** |  | 
**default_action** | [**Action**](Action.md) |  | [optional] 
**actions** | [**List[Action]**](Action.md) |  | 

## Example

```python
from linebot.v3.messaging.models.carousel_column import CarouselColumn

# TODO update the JSON string below
json = "{}"
# create an instance of CarouselColumn from a JSON string
carousel_column_instance = CarouselColumn.from_json(json)
# print the JSON string representation of the object
print CarouselColumn.to_json()

# convert the object into a dict
carousel_column_dict = carousel_column_instance.to_dict()
# create an instance of CarouselColumn from a dict
carousel_column_form_dict = carousel_column.from_dict(carousel_column_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


