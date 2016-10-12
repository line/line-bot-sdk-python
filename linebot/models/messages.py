# -*- coding: utf-8 -*-
#  Licensed under the Apache License, Version 2.0 (the "License"); you may
#  not use this file except in compliance with the License. You may obtain
#  a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#  WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#  License for the specific language governing permissions and limitations
#  under the License.

from __future__ import unicode_literals

from .base import Base


class Message(Base):
    def __init__(self, id=None, **kwargs):
        super(Message, self).__init__(**kwargs)

        self.type = None
        self.id = id


class TextMessage(Message):
    def __init__(self, id=None, text=None, **kwargs):
        """TextMessage

        https://devdocs.line.me/en/#text-message

        Message object which contains the text sent from the source.

        Args:
            id: Message ID
            text: Message text
            **kwargs:
        """
        super(TextMessage, self).__init__(id=id, **kwargs)

        self.type = 'text'
        self.text = text


class ImageMessage(Message):
    def __init__(self, id=None, **kwargs):
        """ImageMessage

        https://devdocs.line.me/en/#image-message

        Message object which contains the image content sent from the source.
        The binary image data can be retrieved with the Content API.

        Args:
            id: Message ID
            **kwargs:
        """
        super(ImageMessage, self).__init__(id=id, **kwargs)

        self.type = 'image'


class VideoMessage(Message):
    def __init__(self, id=None, **kwargs):
        """VideoMessage

        https://devdocs.line.me/en/#video-message

        Message object which contains the video content sent from the source.
        The binary video data can be retrieved with the Content API.

        Args:
            id: Message ID
            **kwargs:
        """
        super(VideoMessage, self).__init__(id=id, **kwargs)

        self.type = 'video'


class AudioMessage(Message):
    def __init__(self, id=None, **kwargs):
        """AudioMessage

        https://devdocs.line.me/en/#audio-message

        Message object which contains the audio content sent from the source.
        The binary audio data can be retrieved with the Content API.

        Args:
            id: Message ID
            **kwargs:
        """
        super(AudioMessage, self).__init__(id=id, **kwargs)

        self.type = 'audio'


class LocationMessage(Message):
    def __init__(
            self, id=None, title=None, address=None, latitude=None,
            longitude=None, **kwargs
    ):
        """LocationMessage

        https://devdocs.line.me/en/#location-message

        Args:
            id: Message ID
            title: Title
            address: Address
            latitude: Latitude
            longitude: Longitude
            **kwargs:
        """
        super(LocationMessage, self).__init__(id=id, **kwargs)

        self.type = 'location'
        self.title = title
        self.address = address
        self.latitude = latitude
        self.longitude = longitude


class StickerMessage(Message):
    def __init__(self, id=None, package_id=None, sticker_id=None, **kwargs):
        """StickerMessage

        https://devdocs.line.me/en/#sticker-message

        Message object which contains the sticker data sent from the source.
        For a list of basic LINE stickers and sticker IDs, see sticker list.

        Args:
            id: Message ID
            package_id: Package ID
            sticker_id: Sticker ID
            **kwargs:
        """
        super(StickerMessage, self).__init__(id=id, **kwargs)

        self.type = 'sticker'
        self.package_id = package_id
        self.sticker_id = sticker_id
