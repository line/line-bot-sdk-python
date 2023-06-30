# -*- coding: utf-8 -*-

#  Licensed under the Apache License, Version 2.0 (the 'License'); you may
#  not use this file except in compliance with the License. You may obtain
#  a copy of the License at
#
#       https://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an 'AS IS' BASIS, WITHOUT
#  WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#  License for the specific language governing permissions and limitations
#  under the License.

from __future__ import unicode_literals, absolute_import

import unittest

from linebot.models import (
    TextSendMessage,
    StickerSendMessage,
    VideoSendMessage,
    AudioSendMessage,
    LocationSendMessage,
    ImageSendMessage,
    QuickReplyButton,
    QuickReply,
    CameraRollAction,
    CameraAction
)
from tests.models.serialize_test_case import SerializeTestCase


class TestSendMessages(SerializeTestCase):
    def test_text_message(self):
        arg = {
            'text': 'Hello, world'
        }
        self.assertEqual(
            self.serialize_as_dict(arg, type=self.TEXT),
            TextSendMessage(**arg).as_json_dict()
        )

    def test_sticker_message(self):
        arg = {
            'package_id': '1',
            'sticker_id': '1'
        }
        self.assertEqual(
            self.serialize_as_dict(arg, type=self.STICKER),
            StickerSendMessage(**arg).as_json_dict()
        )

    def test_image_message(self):
        arg = {
            'original_content_url': 'https://example.com/original.jpg',
            'preview_image_url': 'https://example.com/preview.jpg'
        }
        self.assertEqual(
            self.serialize_as_dict(arg, type=self.IMAGE),
            ImageSendMessage(**arg).as_json_dict()
        )

    def test_video_message(self):
        arg = {
            'type': 'video',
            'original_content_url': 'https://example.com/original.mp4',
            'preview_image_url': 'https://example.com/preview.jpg'
        }
        self.assertEqual(
            self.serialize_as_dict(arg, type=self.VIDEO),
            VideoSendMessage(**arg).as_json_dict()
        )

    def test_video_message_wtih_track(self):
        arg = {
            'type': 'video',
            'original_content_url': 'https://example.com/original.mp4',
            'preview_image_url': 'https://example.com/preview.jpg',
            "tracking_id": "track_id"
        }
        self.assertEqual(
            self.serialize_as_dict(arg, type=self.VIDEO),
            VideoSendMessage(**arg).as_json_dict()
        )

    def test_audio_message(self):
        arg = {
            'original_content_url': 'https://example.com/original.m4a',
            'duration': 60000
        }
        self.assertEqual(
            self.serialize_as_dict(arg, type=self.AUDIO),
            AudioSendMessage(**arg).as_json_dict()
        )

    def test_location_message(self):
        arg = {
            'title': 'my location',
            'address': '〒150-0002 東京都渋谷区渋谷２丁目２１−１',
            'latitude': 35.65910807942215,
            'longitude': 139.70372892916203
        }
        self.assertEqual(
            self.serialize_as_dict(arg, type=self.LOCATION),
            LocationSendMessage(**arg).as_json_dict()
        )

    def test_quick_reply_button(self):
        arg = {
            'action': CameraRollAction(label='Send photo')
        }
        self.assertEqual(
            self.serialize_as_dict(arg, type=self.ACTION),
            QuickReplyButton(**arg).as_json_dict()
        )

    def test_quick_reply(self):
        arg = {
            'items': [
                QuickReplyButton(action=CameraRollAction(label='Send photo')),
                QuickReplyButton(action=CameraAction(label='Open camera')),
            ]
        }
        self.assertEqual(
            self.serialize_as_dict(arg),
            QuickReply(**arg).as_json_dict()
        )


if __name__ == '__main__':
    unittest.main()
