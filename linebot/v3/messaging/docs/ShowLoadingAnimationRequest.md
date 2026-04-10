# ShowLoadingAnimationRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat_id** | **str** | User ID of the target user for whom the loading animation is to be displayed. | 
**loading_seconds** | **int** | The number of seconds to display the loading indicator. It must be a multiple of 5. The maximum value is 60 seconds.  | [optional] 

## Example

```python
from linebot.v3.messaging.models.show_loading_animation_request import ShowLoadingAnimationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ShowLoadingAnimationRequest from a JSON string
show_loading_animation_request_instance = ShowLoadingAnimationRequest.from_json(json)
# print the JSON string representation of the object
print ShowLoadingAnimationRequest.to_json()

# convert the object into a dict
show_loading_animation_request_dict = show_loading_animation_request_instance.to_dict()
# create an instance of ShowLoadingAnimationRequest from a dict
show_loading_animation_request_form_dict = show_loading_animation_request.from_dict(show_loading_animation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


