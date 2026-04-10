# GetModulesResponse

List of bots to which the module is attached

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bots** | [**List[ModuleBot]**](ModuleBot.md) | Array of Bot list Item objects representing basic information about the bot. | 
**next** | **str** | Continuation token. Used to get the next array of basic bot information. This property is only returned if there are more unreturned results.  | [optional] 

## Example

```python
from linebot.v3.module.models.get_modules_response import GetModulesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetModulesResponse from a JSON string
get_modules_response_instance = GetModulesResponse.from_json(json)
# print the JSON string representation of the object
print GetModulesResponse.to_json()

# convert the object into a dict
get_modules_response_dict = get_modules_response_instance.to_dict()
# create an instance of GetModulesResponse from a dict
get_modules_response_form_dict = get_modules_response.from_dict(get_modules_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


