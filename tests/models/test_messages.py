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
    TextMessage, ImageMessage, VideoMessage, AudioMessage,
    LocationMessage, StickerMessage, FileMessage,
)
from linebot.utils import to_snake_case


class TestMessages(unittest.TestCase):
    @staticmethod
    def rename_keys(d):
        return {to_snake_case(k): v for k, v in d.items()}

    def setUp(self):
        self.content_provider_dict = {'type': 'external',
                                      'originalContentUrl': 'https://aaa.com',
                                      'previewImageUrl': 'https://bbb.com'}

        self.content_provider_dict2 = {'type': 'external', 'originalContentUrl': 'https://aaa.com'}

        self.text_message_ev = {'type': 'text', 'id': 'message_id', 'text': 'message_text'}
        self.text_message = TextMessage(**self.rename_keys(self.text_message_ev))

        self.image_message_ev = {'id': 'message_id', 'type': 'image',
                                 'contentProvider': self.content_provider_dict}
        self.image_message = ImageMessage(**self.rename_keys(self.image_message_ev))

        self.video_message_ev = {'id': 'message_id', 'type': 'video', 'duration': 60000,
                                 'contentProvider': self.content_provider_dict}
        self.video_message = VideoMessage(**self.rename_keys(self.video_message_ev))

        self.audio_message_ev = {'id': 'message_id', 'type': 'audio', 'duration': 60000,
                                 'contentProvider': self.content_provider_dict2}
        self.audio_message = AudioMessage(**self.rename_keys(self.audio_message_ev))

        self.location_message_ev = {'type': 'location', 'id': 'message_id', 'title': 'title',
                                    'address': '〒150-0002 東京都渋谷区渋谷２丁目２１−１',
                                    'latitude': 35.65910807942215, 'longitude': 139.70372892916203}
        self.location_message = LocationMessage(**self.rename_keys(self.location_message_ev))

        self.sticker_message_ev = {'type': 'sticker', 'id': 'message_id',
                                   'packageId': '1', 'stickerId': '1'}
        self.sticker_message = StickerMessage(**self.rename_keys(self.sticker_message_ev))

        self.file_message_ev = {'type': 'file', 'id': 'message_id',
                                'fileName': 'file.txt', 'fileSize': 2138}
        self.file_message = FileMessage(**self.rename_keys(self.file_message_ev))

    def test_as_json_dict(self):
        self.assertEqual(self.text_message_ev, self.text_message.as_json_dict())
        self.assertEqual(self.image_message_ev, self.image_message.as_json_dict())
        self.assertEqual(self.video_message_ev, self.video_message.as_json_dict())
        self.assertEqual(self.audio_message_ev, self.audio_message.as_json_dict())
        self.assertEqual(self.location_message_ev, self.location_message.as_json_dict())
        self.assertEqual(self.sticker_message_ev, self.sticker_message.as_json_dict())
        self.assertEqual(self.file_message_ev, self.file_message.as_json_dict())


if __name__ == '__main__':
    unittest.main()
