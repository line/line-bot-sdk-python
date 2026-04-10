# RichMenuAliasListResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aliases** | [**List[RichMenuAliasResponse]**](RichMenuAliasResponse.md) | Rich menu aliases. | 

## Example

```python
from linebot.v3.messaging.models.rich_menu_alias_list_response import RichMenuAliasListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RichMenuAliasListResponse from a JSON string
rich_menu_alias_list_response_instance = RichMenuAliasListResponse.from_json(json)
# print the JSON string representation of the object
print RichMenuAliasListResponse.to_json()

# convert the object into a dict
rich_menu_alias_list_response_dict = rich_menu_alias_list_response_instance.to_dict()
# create an instance of RichMenuAliasListResponse from a dict
rich_menu_alias_list_response_form_dict = rich_menu_alias_list_response.from_dict(rich_menu_alias_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


