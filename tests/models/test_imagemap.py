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
    ImagemapArea,
    ImagemapSendMessage,
    URIImagemapAction,
    MessageImagemapAction,
    Video, BaseSize, ExternalLink,
)
from tests.models.serialize_test_case import SerializeTestCase


class TestImageMap(SerializeTestCase):
    def test_image_map(self):
        arg = {
            'base_url': 'https://example.com/bot/images/rm001',
            'alt_text': 'This is an imagemap',
            'base_size': BaseSize(width=1040, height=1040),
            'video':
                Video(
                    original_content_url='https://example.com/video.mp4',
                    preview_image_url='https://example.com/video_preview.jpg',
                    area=ImagemapArea(x=0, y=0, width=1040, height=585),
                    external_link=ExternalLink(label='See more',
                                               link_uri='https://example.com/see_more.html')
                ),
            'actions': [
                URIImagemapAction(
                    link_uri='https://example.com/',
                    area=ImagemapArea(x=0, y=585, width=520, height=454)
                ),
                MessageImagemapAction(
                    text='Hey',
                    area=ImagemapArea(x=0, y=58, width=52, height=40)
                )
            ]
        }
        self.assertEqual(
            self.serialize_as_dict(arg, type=self.IMAGEMAP),
            ImagemapSendMessage(**arg).as_json_dict()
        )

    def test_video(self):
        arg = {
            'original_content_url': 'https://example.com/video.mp4',
            'preview_image_url': 'https://example.com/video_preview.jpg',
            'area': ImagemapArea(x=0, y=0, width=1040, height=585),
            'external_link': ExternalLink(label='See more',
                                          link_uri='https://example.com/see_more.html')
        }
        self.assertEqual(
            self.serialize_as_dict(arg),
            Video(**arg).as_json_dict()
        )

    def test_message_actions(self):
        arg = {
            'text': 'Hey',
            'area': ImagemapArea(x=0, y=58, width=52, height=40)
        }
        self.assertEqual(
            self.serialize_as_dict(arg, type=self.MESSAGE),
            MessageImagemapAction(**arg).as_json_dict()
        )

    def test_uri_actions(self):
        arg = {
            'link_uri': 'https://example.com/',
            'area': ImagemapArea(x=0, y=585, width=520, height=454)
        }
        self.assertEqual(
            self.serialize_as_dict(arg, self.URI),
            URIImagemapAction(**arg).as_json_dict()
        )

    def test_base_size(self):
        arg = {
            'width': 1040,
            'height': 1040
        }
        self.assertEqual(
            self.serialize_as_dict(arg),
            BaseSize(**arg).as_json_dict()
        )

    def test_external_link(self):
        arg = {
            'label': 'Hey link',
            'link_uri': 'https://example.com/see_more.html'
        }
        self.assertEqual(
            self.serialize_as_dict(arg),
            ExternalLink(**arg).as_json_dict()
        )

    def test_imagemap_area(self):
        arg = {
            'x': 111,
            'y': 33,
            'width': 1040,
            'height': 1040
        }
        self.assertEqual(
            self.serialize_as_dict(arg),
            ImagemapArea(**arg).as_json_dict()
        )


if __name__ == '__main__':
    unittest.main()
