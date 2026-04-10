# UpdateRichMenuAliasRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rich_menu_id** | **str** | The rich menu ID to be associated with the rich menu alias. | 

## Example

```python
from linebot.v3.messaging.models.update_rich_menu_alias_request import UpdateRichMenuAliasRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateRichMenuAliasRequest from a JSON string
update_rich_menu_alias_request_instance = UpdateRichMenuAliasRequest.from_json(json)
# print the JSON string representation of the object
print UpdateRichMenuAliasRequest.to_json()

# convert the object into a dict
update_rich_menu_alias_request_dict = update_rich_menu_alias_request_instance.to_dict()
# create an instance of UpdateRichMenuAliasRequest from a dict
update_rich_menu_alias_request_form_dict = update_rich_menu_alias_request.from_dict(update_rich_menu_alias_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


