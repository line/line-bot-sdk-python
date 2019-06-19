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
    ImageSendMessage,
    VideoSendMessage,
    AudioSendMessage,
    LocationSendMessage,
    StickerSendMessage,
    QuickReply
)
from linebot.utils import to_camel_case


class TestSendMessages(unittest.TestCase):
    def test_text_message(self):
        text_message_arg = {
            'type': 'text',
            'text': 'Hello, world'
        }
        self.assertEqual(
            {to_camel_case(k): v for k, v in text_message_arg.items()},
            TextSendMessage(**text_message_arg).as_json_dict()
        )

    def test_sticker_message(self):
        sticker_message_arg = {
            'type': 'sticker',
            'package_id': '1',
            'sticker_id': '1'
        }
        self.assertEqual(
            {to_camel_case(k): v for k, v in sticker_message_arg.items()},
            StickerSendMessage(**sticker_message_arg).as_json_dict()
        )

    def test_image_message(self):
        image_message_arg = {
            'type': 'image',
            'original_content_url': 'https://example.com/original.jpg',
            'preview_image_url': 'https://example.com/preview.jpg'
        }
        self.assertEqual(
            {to_camel_case(k): v for k, v in image_message_arg.items()},
            ImageSendMessage(**image_message_arg).as_json_dict()
        )

    def test_video_message(self):
        video_message_arg = {
            'type': 'video',
            'original_content_url': 'https://example.com/original.mp4',
            'preview_image_url': 'https://example.com/preview.jpg'
        }
        self.assertEqual(
            {to_camel_case(k): v for k, v in video_message_arg.items()},
            VideoSendMessage(**video_message_arg).as_json_dict()
        )

    def test_audio_message(self):
        audio_message_arg = {
            'type': 'audio',
            'original_content_url': 'https://example.com/original.m4a',
            'duration': 60000
        }
        self.assertEqual(
            {to_camel_case(k): v for k, v in audio_message_arg.items()},
            AudioSendMessage(**audio_message_arg).as_json_dict()
        )

    def test_location_message(self):
        location_message_arg = {
            'type': 'location',
            'title': 'my location',
            'address': '〒150-0002 東京都渋谷区渋谷２丁目２１−１',
            'latitude': 35.65910807942215,
            'longitude': 139.70372892916203
        }
        self.assertEqual(
            {to_camel_case(k): v for k, v in location_message_arg.items()},
            LocationSendMessage(**location_message_arg).as_json_dict()
        )

    def test_quick_reply(self):
        quick_reply_arg = {
            'items': [
                {
                    'type': 'action',
                    'action': {'type': 'cameraRoll', 'label': 'Send photo'}
                },
                {
                    'type': 'action',
                    'action': {'type': 'camera', 'label': 'Open camera'}
                }
            ]
        }
        self.assertEqual(
            {to_camel_case(k): v for k, v in quick_reply_arg.items()},
            QuickReply(**quick_reply_arg).as_json_dict()
        )


if __name__ == '__main__':
    unittest.main()
