# LiffApp


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**liff_id** | **str** | LIFF app ID | [optional] 
**view** | [**LiffView**](LiffView.md) |  | [optional] 
**description** | **str** | Name of the LIFF app | [optional] 
**features** | [**LiffFeatures**](LiffFeatures.md) |  | [optional] 
**permanent_link_pattern** | **str** | How additional information in LIFF URLs is handled. concat is returned.  | [optional] 
**scope** | [**List[LiffScope]**](LiffScope.md) |  | [optional] 
**bot_prompt** | [**LiffBotPrompt**](LiffBotPrompt.md) |  | [optional] 

## Example

```python
from linebot.v3.liff.models.liff_app import LiffApp

# TODO update the JSON string below
json = "{}"
# create an instance of LiffApp from a JSON string
liff_app_instance = LiffApp.from_json(json)
# print the JSON string representation of the object
print LiffApp.to_json()

# convert the object into a dict
liff_app_dict = liff_app_instance.to_dict()
# create an instance of LiffApp from a dict
liff_app_form_dict = liff_app.from_dict(liff_app_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


