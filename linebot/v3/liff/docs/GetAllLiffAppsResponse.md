# GetAllLiffAppsResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apps** | [**List[LiffApp]**](LiffApp.md) |  | [optional] 

## Example

```python
from linebot.v3.liff.models.get_all_liff_apps_response import GetAllLiffAppsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetAllLiffAppsResponse from a JSON string
get_all_liff_apps_response_instance = GetAllLiffAppsResponse.from_json(json)
# print the JSON string representation of the object
print GetAllLiffAppsResponse.to_json()

# convert the object into a dict
get_all_liff_apps_response_dict = get_all_liff_apps_response_instance.to_dict()
# create an instance of GetAllLiffAppsResponse from a dict
get_all_liff_apps_response_form_dict = get_all_liff_apps_response.from_dict(get_all_liff_apps_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


