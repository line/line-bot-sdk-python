# RichMenuAliasResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rich_menu_alias_id** | **str** | Rich menu alias ID. | 
**rich_menu_id** | **str** | The rich menu ID associated with the rich menu alias. | 

## Example

```python
from linebot.v3.messaging.models.rich_menu_alias_response import RichMenuAliasResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RichMenuAliasResponse from a JSON string
rich_menu_alias_response_instance = RichMenuAliasResponse.from_json(json)
# print the JSON string representation of the object
print RichMenuAliasResponse.to_json()

# convert the object into a dict
rich_menu_alias_response_dict = rich_menu_alias_response_instance.to_dict()
# create an instance of RichMenuAliasResponse from a dict
rich_menu_alias_response_form_dict = rich_menu_alias_response.from_dict(rich_menu_alias_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


