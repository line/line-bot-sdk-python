# ImageCarouselColumn


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image_url** | **str** |  | 
**action** | [**Action**](Action.md) |  | 

## Example

```python
from linebot.v3.messaging.models.image_carousel_column import ImageCarouselColumn

# TODO update the JSON string below
json = "{}"
# create an instance of ImageCarouselColumn from a JSON string
image_carousel_column_instance = ImageCarouselColumn.from_json(json)
# print the JSON string representation of the object
print ImageCarouselColumn.to_json()

# convert the object into a dict
image_carousel_column_dict = image_carousel_column_instance.to_dict()
# create an instance of ImageCarouselColumn from a dict
image_carousel_column_form_dict = image_carousel_column.from_dict(image_carousel_column_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


