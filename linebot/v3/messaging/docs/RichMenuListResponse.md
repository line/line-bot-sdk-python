# RichMenuListResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**richmenus** | [**List[RichMenuResponse]**](RichMenuResponse.md) | Rich menus | 

## Example

```python
from linebot.v3.messaging.models.rich_menu_list_response import RichMenuListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RichMenuListResponse from a JSON string
rich_menu_list_response_instance = RichMenuListResponse.from_json(json)
# print the JSON string representation of the object
print RichMenuListResponse.to_json()

# convert the object into a dict
rich_menu_list_response_dict = rich_menu_list_response_instance.to_dict()
# create an instance of RichMenuListResponse from a dict
rich_menu_list_response_form_dict = rich_menu_list_response.from_dict(rich_menu_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


