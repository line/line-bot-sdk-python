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
    TemplateSendMessage,
    CarouselTemplate,
    CarouselColumn,
    ImageCarouselTemplate,
    ImageCarouselColumn,
    ConfirmTemplate,
    ButtonsTemplate,
    PostbackAction,
    URIAction,
    MessageAction,
)
from tests.models.serialize_test_case import SerializeTestCase


class TestTemplate(SerializeTestCase):
    def test_template(self):
        arg = {
            'type': 'template',
            'alt_text': 'This is a buttons template',
            'template':
                ButtonsTemplate(
                    thumbnail_image_url='https=//example.com/bot/images/image.jpg',
                    image_aspect_ratio='rectangle',
                    image_size='cover',
                    image_background_color='#FFFFFF',
                    title='Menu',
                    text='Please select',
                    default_action=URIAction(label='View detail',
                                             uri='http://example.com/page/123'),
                    actions=[
                        PostbackAction(label='Buy', data='action=buy&itemid=155'),
                        URIAction(label='View detail', uri='http://example.com/page/155'),
                    ]
                )
        }
        self.assertEqual(
            self.serialize_as_dict(arg, type=self.TEMPLATE),
            TemplateSendMessage(**arg).as_json_dict()
        )

    def test_button_template(self):
        arg = {
            'type': 'buttons',
            'thumbnail_image_url': 'https=//example.com/bot/images/image.jpg',
            'image_aspect_ratio': 'rectangle',
            'image_size': 'cover',
            'image_background_color': '#FFFFFF',
            'title': 'Menu',
            'text': 'Please select',
            'default_action': URIAction(label='View detail',
                                        uri='http://example.com/page/123'),
            'actions': [
                PostbackAction(label='Buy', data='action=buy&itemid=155'),
                URIAction(label='View detail', uri='http://example.com/page/155'),
            ]
        }
        self.assertEqual(
            self.serialize_as_dict(arg, type=self.BUTTONS),
            ButtonsTemplate(**arg).as_json_dict()
        )

    def test_confirm_template(self):
        arg = {
            'type': 'confirm',
            'text': 'Are you sure?',
            'actions': [
                MessageAction(label='Yes', text='yes...'),
                MessageAction(label='No', text='no...'),
            ]
        }
        self.assertEqual(
            self.serialize_as_dict(arg, type=self.CONFIRM),
            ConfirmTemplate(**arg).as_json_dict()
        )

    def test_carousel_template(self):
        arg = {
            'image_aspect_ratio': 'rectangle',
            'image_size': 'cover',
            'columns': [
                CarouselColumn(
                    thumbnail_image_url='https://example.com/bot/images/item1.jpg',
                    image_background_color='#FFFFFF',
                    title='this is menu',
                    text='description',
                    default_action=URIAction(label='View detail',
                                             uri='http://example.com/page/123'),
                    actions=[
                        PostbackAction(label='Buy', data='action=buy&itemid=155'),
                        URIAction(label='View detail', uri='http://example.com/page/155'),
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://example.com/bot/images/item2.jpg',
                    image_background_color='#000000',
                    title='this is menu',
                    text='description',
                    default_action=URIAction(label='View detail',
                                             uri='http://example.com/page/222'),
                    actions=[
                        PostbackAction(label='Buy', data='action=buy&itemid=555'),
                        URIAction(label='View detail', uri='http://example.com/page/555'),
                    ]
                )
            ]
        }
        self.assertEqual(
            self.serialize_as_dict(arg, type=self.CAROUSEL),
            CarouselTemplate(**arg).as_json_dict()
        )

    def test_carousel_column(self):
        arg = {
            'thumbnail_image_url': 'https://example.com/bot/images/item1.jpg',
            'image_background_color': '#FFFFFF',
            'title': 'this is menu',
            'text': 'description',
            'default_action': URIAction(label='View detail',
                                        uri='http://example.com/page/123'),
            'actions': [
                PostbackAction(label='Buy', data='action=buy&itemid=155'),
                URIAction(label='View detail', uri='http://example.com/page/155'),
            ]
        }
        self.assertEqual(
            self.serialize_as_dict(arg),
            CarouselColumn(**arg).as_json_dict()
        )

    def test_image_carousel_template(self):
        arg = {
            'columns': [
                ImageCarouselColumn(
                    image_url='https://example.com/bot/images/item1.jpg',
                    action=PostbackAction(label='Buy', data='action=buy&itemid=555')
                ),
                ImageCarouselColumn(
                    image_url='https://example.com/bot/images/item2.jpg',
                    action=MessageAction(label='Yes', text='yes')
                ),
            ]
        }
        self.assertEqual(
            self.serialize_as_dict(arg, type=self.IMAGE_CAROUSEL),
            ImageCarouselTemplate(**arg).as_json_dict()
        )

    def test_image_carousel_column(self):
        arg = {
            'image_url': 'https://example.com/bot/images/item1.jpg',
            'action': PostbackAction(label='Buy', data='action=buy&itemid=555')
        }
        self.assertEqual(
            self.serialize_as_dict(arg),
            ImageCarouselColumn(**arg).as_json_dict()
        )


if __name__ == '__main__':
    unittest.main()
