# UserSource


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | ID of the source user | [optional] 

## Example

```python
from linebot.v3.webhooks.models.user_source import UserSource

# TODO update the JSON string below
json = "{}"
# create an instance of UserSource from a JSON string
user_source_instance = UserSource.from_json(json)
# print the JSON string representation of the object
print UserSource.to_json()

# convert the object into a dict
user_source_dict = user_source_instance.to_dict()
# create an instance of UserSource from a dict
user_source_form_dict = user_source.from_dict(user_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


