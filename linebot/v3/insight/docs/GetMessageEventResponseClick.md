# GetMessageEventResponseClick


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**seq** | **int** | The URL&#39;s serial number. | [optional] 
**url** | **str** | URL. | [optional] 
**click** | **int** | Number of times the URL was opened. | [optional] 
**unique_click** | **int** | Number of users that opened the URL. | [optional] 
**unique_click_of_request** | **int** | Number of users who opened this url through any link in the message. If a message contains two links to the same URL and a user opens both links, they&#39;re counted only once. | [optional] 

## Example

```python
from linebot.v3.insight.models.get_message_event_response_click import GetMessageEventResponseClick

# TODO update the JSON string below
json = "{}"
# create an instance of GetMessageEventResponseClick from a JSON string
get_message_event_response_click_instance = GetMessageEventResponseClick.from_json(json)
# print the JSON string representation of the object
print GetMessageEventResponseClick.to_json()

# convert the object into a dict
get_message_event_response_click_dict = get_message_event_response_click_instance.to_dict()
# create an instance of GetMessageEventResponseClick from a dict
get_message_event_response_click_form_dict = get_message_event_response_click.from_dict(get_message_event_response_click_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


