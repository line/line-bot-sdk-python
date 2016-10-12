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


class SendMessage(Base):
    def __init__(self, **kwargs):
        super(SendMessage, self).__init__(**kwargs)

        self.type = None


class TextSendMessage(SendMessage):
    def __init__(self, text=None, **kwargs):
        """TextSendMessage

        https://devdocs.line.me/en/#text

        Args:
            text: Message text
            **kwargs:
        """
        super(TextSendMessage, self).__init__(**kwargs)

        self.type = 'text'
        self.text = text


class ImageSendMessage(SendMessage):
    def __init__(
            self, original_content_url=None, preview_image_url=None, **kwargs
    ):
        """ImageSendMessage

        https://devdocs.line.me/en/#image

        Args:
            original_content_url: Image URL.
                HTTPS
                JPEG
                Max: 1024 x 1024
                Max: 1 MB
            preview_image_url: Preview image URL
                HTTPS
                JPEG
                Max: 240 x 240
                Max: 1 MB
            **kwargs:
        """
        super(ImageSendMessage, self).__init__(**kwargs)

        self.type = 'image'
        self.original_content_url = original_content_url
        self.preview_image_url = preview_image_url


class VideoSendMessage(SendMessage):
    def __init__(self, original_content_url=None, preview_image_url=None, **kwargs):
        """VideoSendMessage

        https://devdocs.line.me/en/#video

        Args:
            original_content_url: URL of video file.
                HTTPS
                mp4
                Less than 1 minute
                Max: 10 MB
            preview_image_url: URL of preview image
                HTTPS
                JPEG
                Max: 240 x 240
                Max: 1 MB
            **kwargs:
        """
        super(VideoSendMessage, self).__init__(**kwargs)

        self.type = 'video'
        self.original_content_url = original_content_url
        self.preview_image_url = preview_image_url


class AudioSendMessage(SendMessage):
    def __init__(self, original_content_url=None, duration=None, **kwargs):
        """AudioSendMessage

        https://devdocs.line.me/en/#audio

        Args:
            original_content_url: URL of audio file.
                HTTPS
                m4a
                Less than 1 minute
                Max 10 MB
            duration: Length of audio file (milliseconds).
            **kwargs:
        """
        super(AudioSendMessage, self).__init__(**kwargs)

        self.type = 'audio'
        self.original_content_url = original_content_url
        self.duration = duration


class LocationSendMessage(SendMessage):
    def __init__(
            self, title=None, address=None, latitude=None,
            longitude=None, **kwargs
    ):
        """LocationSendMessage

        https://devdocs.line.me/en/#location

        Args:
            title: Title.
            address: Address.
            latitude: Latitude.
            longitude: Longitude.
            **kwargs:
        """
        super(LocationSendMessage, self).__init__(**kwargs)

        self.type = 'location'
        self.title = title
        self.address = address
        self.latitude = latitude
        self.longitude = longitude


class StickerSendMessage(SendMessage):
    def __init__(self, package_id=None, sticker_id=None, **kwargs):
        """StickerSendMessage

        https://devdocs.line.me/en/#sticker

        Args:
            package_id: Package ID.
            sticker_id: Sticker ID.
            **kwargs:
        """
        super(StickerSendMessage, self).__init__(**kwargs)

        self.type = 'sticker'
        self.package_id = package_id
        self.sticker_id = sticker_id
