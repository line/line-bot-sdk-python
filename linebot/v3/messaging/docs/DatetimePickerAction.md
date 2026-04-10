# DatetimePickerAction


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **str** |  | [optional] 
**mode** | **str** |  | [optional] 
**initial** | **str** |  | [optional] 
**max** | **str** |  | [optional] 
**min** | **str** |  | [optional] 

## Example

```python
from linebot.v3.messaging.models.datetime_picker_action import DatetimePickerAction

# TODO update the JSON string below
json = "{}"
# create an instance of DatetimePickerAction from a JSON string
datetime_picker_action_instance = DatetimePickerAction.from_json(json)
# print the JSON string representation of the object
print DatetimePickerAction.to_json()

# convert the object into a dict
datetime_picker_action_dict = datetime_picker_action_instance.to_dict()
# create an instance of DatetimePickerAction from a dict
datetime_picker_action_form_dict = datetime_picker_action.from_dict(datetime_picker_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


