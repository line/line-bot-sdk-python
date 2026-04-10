# ButtonsTemplate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**thumbnail_image_url** | **str** |  | [optional] 
**image_aspect_ratio** | **str** |  | [optional] 
**image_size** | **str** |  | [optional] 
**image_background_color** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**text** | **str** |  | 
**default_action** | [**Action**](Action.md) |  | [optional] 
**actions** | [**List[Action]**](Action.md) |  | 

## Example

```python
from linebot.v3.messaging.models.buttons_template import ButtonsTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of ButtonsTemplate from a JSON string
buttons_template_instance = ButtonsTemplate.from_json(json)
# print the JSON string representation of the object
print ButtonsTemplate.to_json()

# convert the object into a dict
buttons_template_dict = buttons_template_instance.to_dict()
# create an instance of ButtonsTemplate from a dict
buttons_template_form_dict = buttons_template.from_dict(buttons_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


