# ImageSet


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Image set ID. Only included when multiple images are sent simultaneously. | 
**index** | **int** | An index starting from 1, indicating the image number in a set of images sent simultaneously. Only included when multiple images are sent simultaneously. However, it won&#39;t be included if the sender is using LINE 11.15 or earlier for Android. | [optional] 
**total** | **int** | The total number of images sent simultaneously. | [optional] 

## Example

```python
from linebot.v3.webhooks.models.image_set import ImageSet

# TODO update the JSON string below
json = "{}"
# create an instance of ImageSet from a JSON string
image_set_instance = ImageSet.from_json(json)
# print the JSON string representation of the object
print ImageSet.to_json()

# convert the object into a dict
image_set_dict = image_set_instance.to_dict()
# create an instance of ImageSet from a dict
image_set_form_dict = image_set.from_dict(image_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


