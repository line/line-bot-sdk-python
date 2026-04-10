# AddLiffAppRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**view** | [**LiffView**](LiffView.md) |  | 
**description** | **str** | Name of the LIFF app.  The LIFF app name can&#39;t include \&quot;LINE\&quot; or similar strings, or inappropriate strings.  | [optional] 
**features** | [**LiffFeatures**](LiffFeatures.md) |  | [optional] 
**permanent_link_pattern** | **str** | How additional information in LIFF URLs is handled. Specify &#x60;concat&#x60;.  | [optional] 
**scope** | [**List[LiffScope]**](LiffScope.md) |  | [optional] 
**bot_prompt** | [**LiffBotPrompt**](LiffBotPrompt.md) |  | [optional] 

## Example

```python
from linebot.v3.liff.models.add_liff_app_request import AddLiffAppRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddLiffAppRequest from a JSON string
add_liff_app_request_instance = AddLiffAppRequest.from_json(json)
# print the JSON string representation of the object
print AddLiffAppRequest.to_json()

# convert the object into a dict
add_liff_app_request_dict = add_liff_app_request_instance.to_dict()
# create an instance of AddLiffAppRequest from a dict
add_liff_app_request_form_dict = add_liff_app_request.from_dict(add_liff_app_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


