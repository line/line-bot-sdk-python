# RichMenuRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**size** | [**RichMenuSize**](RichMenuSize.md) |  | [optional] 
**selected** | **bool** | &#x60;true&#x60; to display the rich menu by default. Otherwise, &#x60;false&#x60;. | [optional] 
**name** | **str** | Name of the rich menu. This value can be used to help manage your rich menus and is not displayed to users. | [optional] 
**chat_bar_text** | **str** | Text displayed in the chat bar | [optional] 
**areas** | [**List[RichMenuArea]**](RichMenuArea.md) | Array of area objects which define the coordinates and size of tappable areas | [optional] 

## Example

```python
from linebot.v3.messaging.models.rich_menu_request import RichMenuRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RichMenuRequest from a JSON string
rich_menu_request_instance = RichMenuRequest.from_json(json)
# print the JSON string representation of the object
print RichMenuRequest.to_json()

# convert the object into a dict
rich_menu_request_dict = rich_menu_request_instance.to_dict()
# create an instance of RichMenuRequest from a dict
rich_menu_request_form_dict = rich_menu_request.from_dict(rich_menu_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


