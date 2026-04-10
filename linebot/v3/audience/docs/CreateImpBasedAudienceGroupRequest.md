# CreateImpBasedAudienceGroupRequest

Create audience for impression-based retargeting

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | The audience&#39;s name. This is case-insensitive, meaning &#x60;AUDIENCE&#x60; and &#x60;audience&#x60; are considered identical. Max character limit: 120  | [optional] 
**request_id** | **str** | The request ID of a broadcast or narrowcast message sent in the past 60 days. Each Messaging API request has a request ID.  | [optional] 

## Example

```python
from linebot.v3.audience.models.create_imp_based_audience_group_request import CreateImpBasedAudienceGroupRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateImpBasedAudienceGroupRequest from a JSON string
create_imp_based_audience_group_request_instance = CreateImpBasedAudienceGroupRequest.from_json(json)
# print the JSON string representation of the object
print CreateImpBasedAudienceGroupRequest.to_json()

# convert the object into a dict
create_imp_based_audience_group_request_dict = create_imp_based_audience_group_request_instance.to_dict()
# create an instance of CreateImpBasedAudienceGroupRequest from a dict
create_imp_based_audience_group_request_form_dict = create_imp_based_audience_group_request.from_dict(create_imp_based_audience_group_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


