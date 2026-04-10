# GroupSource


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_id** | **str** | Group ID of the source group chat | 
**user_id** | **str** | ID of the source user. Only included in message events. Only users of LINE for iOS and LINE for Android are included in userId. | [optional] 

## Example

```python
from linebot.v3.webhooks.models.group_source import GroupSource

# TODO update the JSON string below
json = "{}"
# create an instance of GroupSource from a JSON string
group_source_instance = GroupSource.from_json(json)
# print the JSON string representation of the object
print GroupSource.to_json()

# convert the object into a dict
group_source_dict = group_source_instance.to_dict()
# create an instance of GroupSource from a dict
group_source_form_dict = group_source.from_dict(group_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


