# RichMenuResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rich_menu_id** | **str** | ID of a rich menu | 
**size** | [**RichMenuSize**](RichMenuSize.md) |  | 
**selected** | **bool** | &#x60;true&#x60; to display the rich menu by default. Otherwise, &#x60;false&#x60;. | 
**name** | **str** | Name of the rich menu. This value can be used to help manage your rich menus and is not displayed to users. | 
**chat_bar_text** | **str** | Text displayed in the chat bar | 
**areas** | [**List[RichMenuArea]**](RichMenuArea.md) | Array of area objects which define the coordinates and size of tappable areas | 

## Example

```python
from linebot.v3.messaging.models.rich_menu_response import RichMenuResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RichMenuResponse from a JSON string
rich_menu_response_instance = RichMenuResponse.from_json(json)
# print the JSON string representation of the object
print RichMenuResponse.to_json()

# convert the object into a dict
rich_menu_response_dict = rich_menu_response_instance.to_dict()
# create an instance of RichMenuResponse from a dict
rich_menu_response_form_dict = rich_menu_response.from_dict(rich_menu_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


