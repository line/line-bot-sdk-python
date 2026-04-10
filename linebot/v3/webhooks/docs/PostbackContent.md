# PostbackContent


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **str** | Postback data | 
**params** | **Dict[str, str]** |  | [optional] 

## Example

```python
from linebot.v3.webhooks.models.postback_content import PostbackContent

# TODO update the JSON string below
json = "{}"
# create an instance of PostbackContent from a JSON string
postback_content_instance = PostbackContent.from_json(json)
# print the JSON string representation of the object
print PostbackContent.to_json()

# convert the object into a dict
postback_content_dict = postback_content_instance.to_dict()
# create an instance of PostbackContent from a dict
postback_content_form_dict = postback_content.from_dict(postback_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


