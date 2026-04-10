# QuickReply

Quick reply

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[QuickReplyItem]**](QuickReplyItem.md) | Quick reply button objects. | [optional] 

## Example

```python
from linebot.v3.messaging.models.quick_reply import QuickReply

# TODO update the JSON string below
json = "{}"
# create an instance of QuickReply from a JSON string
quick_reply_instance = QuickReply.from_json(json)
# print the JSON string representation of the object
print QuickReply.to_json()

# convert the object into a dict
quick_reply_dict = quick_reply_instance.to_dict()
# create an instance of QuickReply from a dict
quick_reply_form_dict = quick_reply.from_dict(quick_reply_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


