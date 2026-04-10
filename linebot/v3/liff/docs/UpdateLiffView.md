# UpdateLiffView


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Size of the LIFF app view. Specify one of these values: - compact - tall - full  | [optional] 
**url** | **str** | Endpoint URL. This is the URL of the web app that implements the LIFF app (e.g. https://example.com). Used when the LIFF app is launched using the LIFF URL. The URL scheme must be https. URL fragments (#URL-fragment) can&#39;t be specified.  | [optional] 
**module_mode** | **bool** | &#x60;true&#x60; to use the LIFF app in modular mode. When in modular mode, the action button in the header is not displayed.  | [optional] 

## Example

```python
from linebot.v3.liff.models.update_liff_view import UpdateLiffView

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateLiffView from a JSON string
update_liff_view_instance = UpdateLiffView.from_json(json)
# print the JSON string representation of the object
print UpdateLiffView.to_json()

# convert the object into a dict
update_liff_view_dict = update_liff_view_instance.to_dict()
# create an instance of UpdateLiffView from a dict
update_liff_view_form_dict = update_liff_view.from_dict(update_liff_view_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


