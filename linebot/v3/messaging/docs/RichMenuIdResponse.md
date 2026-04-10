# RichMenuIdResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rich_menu_id** | **str** | Rich menu ID | 

## Example

```python
from linebot.v3.messaging.models.rich_menu_id_response import RichMenuIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RichMenuIdResponse from a JSON string
rich_menu_id_response_instance = RichMenuIdResponse.from_json(json)
# print the JSON string representation of the object
print RichMenuIdResponse.to_json()

# convert the object into a dict
rich_menu_id_response_dict = rich_menu_id_response_instance.to_dict()
# create an instance of RichMenuIdResponse from a dict
rich_menu_id_response_form_dict = rich_menu_id_response.from_dict(rich_menu_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


