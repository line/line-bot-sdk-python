# IssueLinkTokenResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link_token** | **str** | Link token. Link tokens are valid for 10 minutes and can only be used once.   | 

## Example

```python
from linebot.v3.messaging.models.issue_link_token_response import IssueLinkTokenResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IssueLinkTokenResponse from a JSON string
issue_link_token_response_instance = IssueLinkTokenResponse.from_json(json)
# print the JSON string representation of the object
print IssueLinkTokenResponse.to_json()

# convert the object into a dict
issue_link_token_response_dict = issue_link_token_response_instance.to_dict()
# create an instance of IssueLinkTokenResponse from a dict
issue_link_token_response_form_dict = issue_link_token_response.from_dict(issue_link_token_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


