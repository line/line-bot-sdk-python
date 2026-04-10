# QuickReplyItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image_url** | **str** | URL of the icon that is displayed at the beginning of the button | [optional] 
**action** | [**Action**](Action.md) |  | [optional] 
**type** | **str** | &#x60;action&#x60; | [optional] [default to 'action']

## Example

```python
from linebot.v3.messaging.models.quick_reply_item import QuickReplyItem

# TODO update the JSON string below
json = "{}"
# create an instance of QuickReplyItem from a JSON string
quick_reply_item_instance = QuickReplyItem.from_json(json)
# print the JSON string representation of the object
print QuickReplyItem.to_json()

# convert the object into a dict
quick_reply_item_dict = quick_reply_item_instance.to_dict()
# create an instance of QuickReplyItem from a dict
quick_reply_item_form_dict = quick_reply_item.from_dict(quick_reply_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


