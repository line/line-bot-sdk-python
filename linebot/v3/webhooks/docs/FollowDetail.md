# FollowDetail


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_unblocked** | **bool** | Whether a user has added your LINE Official Account as a friend or unblocked. | 

## Example

```python
from linebot.v3.webhooks.models.follow_detail import FollowDetail

# TODO update the JSON string below
json = "{}"
# create an instance of FollowDetail from a JSON string
follow_detail_instance = FollowDetail.from_json(json)
# print the JSON string representation of the object
print FollowDetail.to_json()

# convert the object into a dict
follow_detail_dict = follow_detail_instance.to_dict()
# create an instance of FollowDetail from a dict
follow_detail_form_dict = follow_detail.from_dict(follow_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


