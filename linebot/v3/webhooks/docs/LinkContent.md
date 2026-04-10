# LinkContent

Content of the account link event.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | **str** | One of the following values to indicate whether linking the account was successful or not | 
**nonce** | **str** | Specified nonce (number used once) when verifying the user ID. | 

## Example

```python
from linebot.v3.webhooks.models.link_content import LinkContent

# TODO update the JSON string below
json = "{}"
# create an instance of LinkContent from a JSON string
link_content_instance = LinkContent.from_json(json)
# print the JSON string representation of the object
print LinkContent.to_json()

# convert the object into a dict
link_content_dict = link_content_instance.to_dict()
# create an instance of LinkContent from a dict
link_content_form_dict = link_content.from_dict(link_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


