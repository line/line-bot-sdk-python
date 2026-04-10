# URIAction


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uri** | **str** |  | [optional] 
**alt_uri** | [**AltUri**](AltUri.md) |  | [optional] 

## Example

```python
from linebot.v3.messaging.models.uri_action import URIAction

# TODO update the JSON string below
json = "{}"
# create an instance of URIAction from a JSON string
uri_action_instance = URIAction.from_json(json)
# print the JSON string representation of the object
print URIAction.to_json()

# convert the object into a dict
uri_action_dict = uri_action_instance.to_dict()
# create an instance of URIAction from a dict
uri_action_form_dict = uri_action.from_dict(uri_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


