# GetMessageContentTranscodingResponse

Transcoding response

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | The preparation status. One of:  &#x60;processing&#x60;: Preparing to get content. &#x60;succeeded&#x60;: Ready to get the content. You can get the content sent by users. &#x60;failed&#x60;: Failed to prepare to get the content.  | 

## Example

```python
from linebot.v3.messaging.models.get_message_content_transcoding_response import GetMessageContentTranscodingResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetMessageContentTranscodingResponse from a JSON string
get_message_content_transcoding_response_instance = GetMessageContentTranscodingResponse.from_json(json)
# print the JSON string representation of the object
print GetMessageContentTranscodingResponse.to_json()

# convert the object into a dict
get_message_content_transcoding_response_dict = get_message_content_transcoding_response_instance.to_dict()
# create an instance of GetMessageContentTranscodingResponse from a dict
get_message_content_transcoding_response_form_dict = get_message_content_transcoding_response.from_dict(get_message_content_transcoding_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


