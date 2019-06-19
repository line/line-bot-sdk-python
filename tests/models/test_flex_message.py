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
    FlexSendMessage,
    BlockStyle,
    BubbleStyle,
    BubbleContainer,
    CarouselContainer,
    BoxComponent,
    TextComponent,
    SeparatorComponent,
    ImageComponent,
    ButtonComponent,
    FillerComponent,
    IconComponent,
    SpacerComponent,
    URIAction,
)
from tests.models.serialize_test_case import SerializeTestCase


class TestFlexMessage(SerializeTestCase):
    def test_flex_message(self):
        arg = {
            'type': 'flex',
            'alt_text': 'this is a flex message',
            'contents':
                BubbleContainer(
                    body=BoxComponent(
                        layout='vertical',
                        contents=[
                            TextComponent(text='hello'),
                            TextComponent(text='world')
                        ]
                    )
                )
        }
        self.assertEqual(
            self.serialize_as_dict(arg),
            FlexSendMessage(**arg).as_json_dict()
        )

    def test_bubble_container(self):
        arg = {
            'type': 'bubble',
            'header':
                BoxComponent(layout='vertical',
                             contents=[TextComponent(text='Header text')]),
            'hero':
                ImageComponent(uri='https://example.com/flex/images/image.jpg'),
            'body':
                BoxComponent(layout='vertical',
                             contents=[TextComponent(text='Body text')]),
            'footer':
                BoxComponent(layout='vertical',
                             contents=[TextComponent(text='Footer text')]),
            'styles':
                BubbleStyle(
                    header=BlockStyle(background_color='#00ffff'),
                    hero=BlockStyle(background_color='#00ffff',
                                    separator=True),
                    footer=BlockStyle(background_color='#00ffff',
                                      separator=True,
                                      separator_color='#00ffff')
                )
        }
        self.assertEqual(
            self.serialize_as_dict(arg),
            BubbleContainer(**arg).as_json_dict()
        )

    def test_bubble_style(self):
        arg = {
            'header':
                BlockStyle(background_color='#00ffff'),
            'hero':
                BlockStyle(background_color='#00ffff',
                           separator=True),
            'footer':
                BlockStyle(background_color='#00ffff',
                           separator=True,
                           separator_color='#00ffff')
        }
        self.assertEqual(
            self.serialize_as_dict(arg),
            BubbleStyle(**arg).as_json_dict()
        )

    def test_block_style(self):
        arg = {
            'background_color': '#00ffff',
            'separator': True,
            'separator_color': '#000000'
        }
        self.assertEqual(
            self.serialize_as_dict(arg),
            BlockStyle(**arg).as_json_dict()
        )

    def test_carousel_container(self):
        arg = {
            'type': 'carousel',
            'contents': [
                BubbleContainer(
                    body=BoxComponent(
                        layout='vertical',
                        contents=[TextComponent(text='Hey')]
                    )
                ),
                BubbleContainer(
                    body=BoxComponent(
                        layout='vertical',
                        contents=[TextComponent(text='Foo')]
                    )
                ),
            ]
        }
        self.assertEqual(
            self.serialize_as_dict(arg),
            CarouselContainer(**arg).as_json_dict()
        )

    def test_box_component(self):
        arg = {
            'type': 'box',
            'layout': 'vertical',
            'contents': [
                ImageComponent(url='https://example.com/flex/images/image.jpg'),
                SeparatorComponent(),
                TextComponent(text='Text in the box'),
            ]
        }

        self.assertEqual(
            self.serialize_as_dict(arg),
            BoxComponent(**arg).as_json_dict()
        )

    def test_button_component(self):
        arg = {
            'type': 'button',
            'action':
                URIAction(label='Tap me',
                          uri='https://example.com'),
            'style': 'primary',
            'color': '#0000ff'
        }
        self.assertEqual(
            self.serialize_as_dict(arg),
            ButtonComponent(**arg).as_json_dict()
        )

    def test_filler_component(self):
        arg = {
            'type': 'filler'
        }
        self.assertEqual(
            arg,
            FillerComponent(**arg).as_json_dict()
        )

    def test_icon_component(self):
        arg = {
            'type': 'icon',
            'url': 'https://example.com/icon/png/caution.png',
            'size': 'lg',
            'aspect_ratio': '1.91:1'
        }
        self.assertEqual(
            self.serialize_as_dict(arg),
            IconComponent(**arg).as_json_dict()
        )

    def test_image_component(self):
        arg = {
            'type': 'image',
            'url': 'https://example.com/flex/images/image.jpg',
            'size': 'full',
            'aspect_ratio': '1.91:1'
        }
        self.assertEqual(
            self.serialize_as_dict(arg),
            ImageComponent(**arg).as_json_dict()
        )

    def test_separator_component(self):
        arg = {
            'type': 'separator',
            'color': '#000000'
        }
        self.assertEqual(
            arg,
            SeparatorComponent(**arg).as_json_dict()
        )

    def test_spacer_component(self):
        arg = {
            'type': 'spacer',
            'size': 'md'
        }
        self.assertEqual(
            arg,
            SpacerComponent(**arg).as_json_dict()
        )

    def test_text_component(self):
        arg = {
            'type': 'text',
            'text': 'Hello, World!',
            'size': 'xl',
            'weight': 'bold',
            'color': '#0000ff'
        }
        self.assertEqual(
            arg,
            TextComponent(**arg).as_json_dict()
        )


if __name__ == '__main__':
    unittest.main()
