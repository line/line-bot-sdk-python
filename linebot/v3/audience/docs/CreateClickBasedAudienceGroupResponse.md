# CreateClickBasedAudienceGroupResponse

Create audience for click-based retargeting

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audience_group_id** | **int** | The audience ID. | [optional] 
**type** | [**AudienceGroupType**](AudienceGroupType.md) |  | [optional] 
**description** | **str** | The audience&#39;s name. | [optional] 
**created** | **int** | When the audience was created (in UNIX time). | [optional] 
**request_id** | **str** | The request ID that was specified when the audience was created. | [optional] 
**click_url** | **str** | The URL that was specified when the audience was created. | [optional] 
**create_route** | **str** | How the audience was created. &#x60;MESSAGING_API&#x60;: An audience created with Messaging API.  | [optional] 
**permission** | **str** | Audience&#39;s update permission. Audiences linked to the same channel will be READ_WRITE.  - &#x60;READ&#x60;: Can use only. - &#x60;READ_WRITE&#x60;: Can use and update.  | [optional] 
**expire_timestamp** | **int** | Time of audience expiration. Only returned for specific audiences. | [optional] 
**is_ifa_audience** | **bool** | The value indicating the type of account to be sent, as specified when creating the audience for uploading user IDs. One of:  true: Accounts are specified with IFAs. false (default): Accounts are specified with user IDs.  | [optional] [default to False]

## Example

```python
from linebot.v3.audience.models.create_click_based_audience_group_response import CreateClickBasedAudienceGroupResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateClickBasedAudienceGroupResponse from a JSON string
create_click_based_audience_group_response_instance = CreateClickBasedAudienceGroupResponse.from_json(json)
# print the JSON string representation of the object
print CreateClickBasedAudienceGroupResponse.to_json()

# convert the object into a dict
create_click_based_audience_group_response_dict = create_click_based_audience_group_response_instance.to_dict()
# create an instance of CreateClickBasedAudienceGroupResponse from a dict
create_click_based_audience_group_response_form_dict = create_click_based_audience_group_response.from_dict(create_click_based_audience_group_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


