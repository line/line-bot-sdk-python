# ModuleBot

basic information about the bot.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | Bot&#39;s user ID | 
**basic_id** | **str** | Bot&#39;s basic ID | 
**premium_id** | **str** | Bot&#39;s premium ID. Not included in the response if the premium ID isn&#39;t set. | [optional] 
**display_name** | **str** | Bot&#39;s display name | 
**picture_url** | **str** | Profile image URL. Image URL starting with &#x60;https://&#x60;. Not included in the response if the bot doesn&#39;t have a profile image. | [optional] 

## Example

```python
from linebot.v3.module.models.module_bot import ModuleBot

# TODO update the JSON string below
json = "{}"
# create an instance of ModuleBot from a JSON string
module_bot_instance = ModuleBot.from_json(json)
# print the JSON string representation of the object
print ModuleBot.to_json()

# convert the object into a dict
module_bot_dict = module_bot_instance.to_dict()
# create an instance of ModuleBot from a dict
module_bot_form_dict = module_bot.from_dict(module_bot_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


