# CreateClickBasedAudienceGroupRequest

Create audience for click-based retargeting

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | The audience&#39;s name. This is case-insensitive, meaning AUDIENCE and audience are considered identical. Max character limit: 120  | [optional] 
**request_id** | **str** | The request ID of a broadcast or narrowcast message sent in the past 60 days. Each Messaging API request has a request ID.  | [optional] 
**click_url** | **str** | The URL clicked by the user. If empty, users who clicked any URL in the message are added to the list of recipients. Max character limit: 2,000  | [optional] 

## Example

```python
from linebot.v3.audience.models.create_click_based_audience_group_request import CreateClickBasedAudienceGroupRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateClickBasedAudienceGroupRequest from a JSON string
create_click_based_audience_group_request_instance = CreateClickBasedAudienceGroupRequest.from_json(json)
# print the JSON string representation of the object
print CreateClickBasedAudienceGroupRequest.to_json()

# convert the object into a dict
create_click_based_audience_group_request_dict = create_click_based_audience_group_request_instance.to_dict()
# create an instance of CreateClickBasedAudienceGroupRequest from a dict
create_click_based_audience_group_request_form_dict = create_click_based_audience_group_request.from_dict(create_click_based_audience_group_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


