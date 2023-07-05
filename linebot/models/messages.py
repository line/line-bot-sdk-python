# -*- coding: utf-8 -*-

#  Licensed under the Apache License, Version 2.0 (the "License"); you may
#  not use this file except in compliance with the License. You may obtain
#  a copy of the License at
#
#       https://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#  WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#  License for the specific language governing permissions and limitations
#  under the License.

"""linebot.models.messages module."""


from abc import ABCMeta

from future.utils import with_metaclass

from linebot.models.emojis import Emojis
from .mention import Mention
from .mentionee import Mentionee
from .base import Base

from deprecated import deprecated

from linebot.deprecations import (
    LineBotSdkDeprecatedIn30
)


@deprecated(reason="Use 'from linebot.v3.webhooks import MessageContent' instead. See https://github.com/line/line-bot-sdk-python/blob/master/README.rst for more details.", version='3.0.0', category=LineBotSdkDeprecatedIn30)  # noqa: E501
class Message(with_metaclass(ABCMeta, Base)):
    """Abstract Base Class of Message."""

    def __init__(self, id=None, use_raw_message=False, **kwargs):
        """__init__ method.

        :param str id: Message ID
        :param bool use_raw_message: Using original Message key as attribute
        :param kwargs:
        """
        super(Message, self).__init__(**kwargs)

        if use_raw_message:
            self.__dict__.update(kwargs)

        self.type = None
        self.id = id

    def __getitem__(self, key):
        """__getitem__ method.

        :param str key: Message key
        """
        return self.__dict__.get(key, None)


@deprecated(reason="Use 'from linebot.v3.webhooks import TextMessageContent' instead. See https://github.com/line/line-bot-sdk-python/blob/master/README.rst for more details.", version='3.0.0', category=LineBotSdkDeprecatedIn30)  # noqa: E501
class TextMessage(Message):
    """TextMessage.

    https://developers.line.biz/en/reference/messaging-api/#wh-text

    Message object which contains the text sent from the source.
    """

    def __init__(self, id=None, text=None, emojis=None, mention=None, **kwargs):
        """__init__ method.

        :param str id: Message ID
        :param str text: Message text
        :param List emojis: Array of LINE emoji objects
        :param object mention: LINE mention object
        :param kwargs:
        """
        super(TextMessage, self).__init__(id=id, **kwargs)

        self.type = 'text'
        self.text = text
        if emojis:
            new_emojis = []
            for emoji in emojis:
                emoji_object = self.get_or_new_from_json_dict(
                    emoji, Emojis
                )
                if emoji_object:
                    new_emojis.append(emoji_object)
            self.emojis = new_emojis
        else:
            self.emojis = emojis

        if mention:
            mention_object = self.get_or_new_from_json_dict(
                mention, Mention
            )
            mentionees = []
            for mentionee in mention_object.mentionees:
                mentionee_object = self.get_or_new_from_json_dict(
                    mentionee, Mentionee
                )
                if mentionee_object:
                    mentionees.append(mentionee_object)
            self.mention = Mention(mentionees)
        else:
            self.mention = mention


@deprecated(reason="Use 'from linebot.v3.webhooks import ImageMessageContent' instead. See https://github.com/line/line-bot-sdk-python/blob/master/README.rst for more details.", version='3.0.0', category=LineBotSdkDeprecatedIn30)  # noqa: E501
class ImageMessage(Message):
    """ImageMessage.

    https://developers.line.biz/en/reference/messaging-api/#wh-image

    Message object which contains the image content sent from the source.
    The binary image data can be retrieved with the Content API.
    """

    def __init__(self, id=None, content_provider=None, image_set=None, **kwargs):
        """__init__ method.

        :param str id: Message ID
        :param content_provider: ContentProvider object
        :type content_provider:
            :py:class:`linebot.models.messages.ContentProvider`
        :param image_set: ImageSet object
        :type image_set:
            :py:class:`linebot.models.messages.ImageSet`
        :param kwargs:
        """
        super(ImageMessage, self).__init__(id=id, **kwargs)

        self.type = 'image'
        self.content_provider = self.get_or_new_from_json_dict(
            content_provider, ContentProvider
        )
        self.image_set = self.get_or_new_from_json_dict(
            image_set, ImageSet
        )


@deprecated(reason="Use 'from linebot.v3.webhooks import VideoMessageContent' instead. See https://github.com/line/line-bot-sdk-python/blob/master/README.rst for more details.", version='3.0.0', category=LineBotSdkDeprecatedIn30)  # noqa: E501
class VideoMessage(Message):
    """VideoMessage.

    https://developers.line.biz/en/reference/messaging-api/#wh-video

    Message object which contains the video content sent from the source.
    The binary video data can be retrieved with the Content API.
    """

    def __init__(self, id=None, duration=None, content_provider=None, **kwargs):
        """__init__ method.

        :param str id: Message ID
        :param long duration: Length of video file (milliseconds)
        :param content_provider: ContentProvider object
        :type content_provider:
            :py:class:`linebot.models.messages.ContentProvider`
        :param kwargs:
        """
        super(VideoMessage, self).__init__(id=id, **kwargs)

        self.type = 'video'
        self.duration = duration
        self.content_provider = self.get_or_new_from_json_dict(
            content_provider, ContentProvider
        )


@deprecated(reason="Use 'from linebot.v3.webhooks import AudioMessageContent' instead. See https://github.com/line/line-bot-sdk-python/blob/master/README.rst for more details.", version='3.0.0', category=LineBotSdkDeprecatedIn30)  # noqa: E501
class AudioMessage(Message):
    """AudioMessage.

    https://developers.line.biz/en/reference/messaging-api/#wh-audio

    Message object which contains the audio content sent from the source.
    The binary audio data can be retrieved with the Content API.
    """

    def __init__(self, id=None, duration=None, content_provider=None, **kwargs):
        """__init__ method.

        :param str id: Message ID
        :param long duration: Length of audio file (milliseconds)
        :param content_provider: ContentProvider object
        :type content_provider:
            :py:class:`linebot.models.messages.ContentProvider`
        :param kwargs:
        """
        super(AudioMessage, self).__init__(id=id, **kwargs)

        self.type = 'audio'
        self.duration = duration
        self.content_provider = self.get_or_new_from_json_dict(
            content_provider, ContentProvider
        )


@deprecated(reason="Use 'from linebot.v3.webhooks import LocationMessageContent' instead. See https://github.com/line/line-bot-sdk-python/blob/master/README.rst for more details.", version='3.0.0', category=LineBotSdkDeprecatedIn30)  # noqa: E501
class LocationMessage(Message):
    """LocationMessage.

    https://developers.line.biz/en/reference/messaging-api/#wh-location
    """

    def __init__(self, id=None, title=None, address=None, latitude=None, longitude=None,
                 **kwargs):
        """__init__ method.

        :param str id: Message ID
        :param str title: Title
        :param str address: Address
        :param float latitude: Latitude
        :param float longitude: Longitude
        :param kwargs:
        """
        super(LocationMessage, self).__init__(id=id, **kwargs)

        self.type = 'location'
        self.title = title
        self.address = address
        self.latitude = latitude
        self.longitude = longitude


@deprecated(reason="Use 'from linebot.v3.webhooks import StickerMessageContent' instead. See https://github.com/line/line-bot-sdk-python/blob/master/README.rst for more details.", version='3.0.0', category=LineBotSdkDeprecatedIn30)  # noqa: E501
class StickerMessage(Message):
    """StickerMessage.

    https://developers.line.biz/en/reference/messaging-api/#wh-sticker

    Message object which contains the sticker data sent from the source.
    For a list of basic LINE stickers and sticker IDs, see sticker list.
    """

    def __init__(self, id=None, package_id=None, sticker_id=None,
                 sticker_resource_type=None, keywords=None, text=None, **kwargs):
        """__init__ method.

        :param str id: Message ID
        :param str package_id: Package ID
        :param str sticker_id: Sticker ID
        :param str sticker_resource_type: Sticker resource type
        :param list[str] keywords: List of up to 15 keywords describing the sticker
        :param str text: Any text entered by the user
        :param kwargs:
        """
        super(StickerMessage, self).__init__(id=id, **kwargs)

        self.type = 'sticker'
        self.package_id = package_id
        self.sticker_id = sticker_id
        self.sticker_resource_type = sticker_resource_type
        self.keywords = keywords
        self.text = text


@deprecated(reason="Use 'from linebot.v3.webhooks import FileMessageContent' instead. See https://github.com/line/line-bot-sdk-python/blob/master/README.rst for more details.", version='3.0.0', category=LineBotSdkDeprecatedIn30)  # noqa: E501
class FileMessage(Message):
    """FileMessage.

    https://developers.line.biz/en/reference/messaging-api/#wh-file

    Message object which contains the file content sent from the source.
    The binary file data can be retrieved with the Content API.
    """

    def __init__(self, id=None, file_name=None, file_size=None, **kwargs):
        """__init__ method.

        :param str id: Message ID
        :param str file_name: File Name
        :param int file_size: File Size
        :param kwargs:
        """
        super(FileMessage, self).__init__(id=id, **kwargs)

        self.type = 'file'
        self.file_size = file_size
        self.file_name = file_name


@deprecated(reason="Use 'from linebot.v3.webhooks import ContentProvider' instead. See https://github.com/line/line-bot-sdk-python/blob/master/README.rst for more details.", version='3.0.0', category=LineBotSdkDeprecatedIn30)  # noqa: E501
class ContentProvider(Base):
    """Content provider."""

    def __init__(self, type=None, original_content_url=None, preview_image_url=None, **kwargs):
        """__init__ method.

        :param str type: Provider of the content. `line` or `external`.
        :param str original_content_url: URL of the content.
        :param str preview_image_url: URL of the preview image.
        :param kwargs:
        """
        super(ContentProvider, self).__init__(**kwargs)

        self.type = type
        self.original_content_url = original_content_url
        self.preview_image_url = preview_image_url


@deprecated(reason="Use 'from linebot.v3.webhooks import ImageSet' instead. See https://github.com/line/line-bot-sdk-python/blob/master/README.rst for more details.", version='3.0.0', category=LineBotSdkDeprecatedIn30)  # noqa: E501
class ImageSet(Base):
    """Image Set."""

    def __init__(self, id=None, index=None, total=0, **kwargs):
        """__init__ method.

        :param str id: Image set ID.
        :param int index: Image number in a set of images sent simultaneously.
        :param int total: Total number of images sent simultaneously.
        :param kwargs:
        """
        super(ImageSet, self).__init__(**kwargs)

        self.id = id
        self.index = index
        self.total = total
