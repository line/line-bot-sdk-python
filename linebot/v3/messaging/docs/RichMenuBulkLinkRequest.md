# RichMenuBulkLinkRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rich_menu_id** | **str** | ID of a rich menu | 
**user_ids** | **List[str]** | Array of user IDs. Found in the &#x60;source&#x60; object of webhook event objects. Do not use the LINE ID used in LINE. | 

## Example

```python
from linebot.v3.messaging.models.rich_menu_bulk_link_request import RichMenuBulkLinkRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RichMenuBulkLinkRequest from a JSON string
rich_menu_bulk_link_request_instance = RichMenuBulkLinkRequest.from_json(json)
# print the JSON string representation of the object
print RichMenuBulkLinkRequest.to_json()

# convert the object into a dict
rich_menu_bulk_link_request_dict = rich_menu_bulk_link_request_instance.to_dict()
# create an instance of RichMenuBulkLinkRequest from a dict
rich_menu_bulk_link_request_form_dict = rich_menu_bulk_link_request.from_dict(rich_menu_bulk_link_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


