# NarrowcastProgressResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phase** | **str** | The current status. One of:  &#x60;waiting&#x60;: Messages are not yet ready to be sent. They are currently being filtered or processed in some way. &#x60;sending&#x60;: Messages are currently being sent. &#x60;succeeded&#x60;: Messages were sent successfully. This may not mean the messages were successfully received. &#x60;failed&#x60;: Messages failed to be sent. Use the failedDescription property to find the cause of the failure.  | 
**success_count** | **int** | The number of users who successfully received the message. | [optional] 
**failure_count** | **int** | The number of users who failed to send the message. | [optional] 
**target_count** | **int** | The number of intended recipients of the message. | [optional] 
**failed_description** | **str** | The reason the message failed to be sent. This is only included with a &#x60;phase&#x60; property value of &#x60;failed&#x60;. | [optional] 
**error_code** | **int** | Error summary. This is only included with a phase property value of failed. One of:  &#x60;1&#x60;: An internal error occurred. &#x60;2&#x60;: An error occurred because there weren&#39;t enough recipients. &#x60;3&#x60;: A conflict error of requests occurs because a request that has already been accepted is retried. &#x60;4&#x60;: An audience of less than 50 recipients is included as a condition of sending. &#x60;5&#x60;: Message delivery has been canceled to prevent messages from being delivered only to a subset of the target audience.  | [optional] 
**accepted_time** | **datetime** | Narrowcast message request accepted time in milliseconds.  Format: ISO 8601 (e.g. 2020-12-03T10:15:30.121Z) Timezone: UTC  | 
**completed_time** | **datetime** | Processing of narrowcast message request completion time in milliseconds. Returned when the phase property is succeeded or failed.  Format: ISO 8601 (e.g. 2020-12-03T10:15:30.121Z) Timezone: UTC  | [optional] 

## Example

```python
from linebot.v3.messaging.models.narrowcast_progress_response import NarrowcastProgressResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NarrowcastProgressResponse from a JSON string
narrowcast_progress_response_instance = NarrowcastProgressResponse.from_json(json)
# print the JSON string representation of the object
print NarrowcastProgressResponse.to_json()

# convert the object into a dict
narrowcast_progress_response_dict = narrowcast_progress_response_instance.to_dict()
# create an instance of NarrowcastProgressResponse from a dict
narrowcast_progress_response_form_dict = narrowcast_progress_response.from_dict(narrowcast_progress_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


