# CreateRichMenuAliasRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rich_menu_alias_id** | **str** | Rich menu alias ID, which can be any ID, unique for each channel. | 
**rich_menu_id** | **str** | The rich menu ID to be associated with the rich menu alias. | 

## Example

```python
from linebot.v3.messaging.models.create_rich_menu_alias_request import CreateRichMenuAliasRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateRichMenuAliasRequest from a JSON string
create_rich_menu_alias_request_instance = CreateRichMenuAliasRequest.from_json(json)
# print the JSON string representation of the object
print CreateRichMenuAliasRequest.to_json()

# convert the object into a dict
create_rich_menu_alias_request_dict = create_rich_menu_alias_request_instance.to_dict()
# create an instance of CreateRichMenuAliasRequest from a dict
create_rich_menu_alias_request_form_dict = create_rich_menu_alias_request.from_dict(create_rich_menu_alias_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


