# FlexImage


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | Image URL (Max character limit: 2000) Protocol: HTTPS (TLS 1.2 or later) Image format: JPEG or PNG Maximum image size: 1024×1024 pixels Maximum file size: 10 MB (300 KB when the animated property is true)  | 
**flex** | **int** | The ratio of the width or height of this component within the parent box. | [optional] 
**margin** | **str** | The minimum amount of space to include before this component in its parent container.  | [optional] 
**position** | **str** | Reference for offsetTop, offsetBottom, offsetStart, and offsetEnd. Specify one of the following values:  &#x60;relative&#x60;: Use the previous box as reference. &#x60;absolute&#x60;: Use the top left of parent element as reference. The default value is relative.  | [optional] 
**offset_top** | **str** | Offset. | [optional] 
**offset_bottom** | **str** | Offset. | [optional] 
**offset_start** | **str** | Offset. | [optional] 
**offset_end** | **str** | Offset. | [optional] 
**align** | **str** | Alignment style in horizontal direction.  | [optional] 
**gravity** | **str** | Alignment style in vertical direction. | [optional] 
**size** | **str** | The maximum image width. This is md by default.  | [optional] [default to 'md']
**aspect_ratio** | **str** | Aspect ratio of the image. &#x60;{width}:{height}&#x60; format. Specify the value of &#x60;{width}&#x60; and &#x60;{height}&#x60; in the range from &#x60;1&#x60; to &#x60;100000&#x60;. However, you cannot set &#x60;{height}&#x60; to a value that is more than three times the value of &#x60;{width}&#x60;. The default value is &#x60;1:1&#x60;.  | [optional] 
**aspect_mode** | **str** | The display style of the image if the aspect ratio of the image and that specified by the aspectRatio property do not match.  | [optional] 
**background_color** | **str** | Background color of the image. Use a hexadecimal color code. | [optional] 
**action** | [**Action**](Action.md) |  | [optional] 
**animated** | **bool** | When this is &#x60;true&#x60;, an animated image (APNG) plays. You can specify a value of true up to 10 images in a single message. You can&#39;t send messages that exceed this limit. This is &#x60;false&#x60; by default. Animated images larger than 300 KB aren&#39;t played back.  | [optional] [default to False]

## Example

```python
from linebot.v3.messaging.models.flex_image import FlexImage

# TODO update the JSON string below
json = "{}"
# create an instance of FlexImage from a JSON string
flex_image_instance = FlexImage.from_json(json)
# print the JSON string representation of the object
print FlexImage.to_json()

# convert the object into a dict
flex_image_dict = flex_image_instance.to_dict()
# create an instance of FlexImage from a dict
flex_image_form_dict = flex_image.from_dict(flex_image_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


