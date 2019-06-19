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
    FlexSendMessage, BubbleContainer, BubbleStyle, BlockStyle,
    CarouselContainer, BoxComponent, ButtonComponent,
    FillerComponent, IconComponent, ImageComponent,
    SeparatorComponent, SpacerComponent, TextComponent
)
from linebot.utils import to_camel_case


class TestFlexMessage(unittest.TestCase):
    def test_flex_message(self):
        flex_message_arg = {
            'type': 'flex',
            'alt_text': 'this is a flex message',
            'contents': {
                'type': 'bubble',
                'body': {
                    'type': 'box',
                    'layout': 'vertical',
                    'contents': [
                        {'type': 'text', 'text': 'hello'},
                        {'type': 'text', 'text': 'world'}
                    ]
                }
            }
        }
        BubbleContainer(
            body=BoxComponent(
                layout='vertical',
                contents=[TextComponent(text='hello'), TextComponent(text='world')]
            )
        )
        self.assertEqual(
            {to_camel_case(k): v for k, v in flex_message_arg.items()},
            FlexSendMessage(**flex_message_arg).as_json_dict()
        )

    def test_bubble_container(self):
        bubble_container_arg = {
            'type': 'bubble',
            'header': {
                'type': 'box',
                'layout': 'vertical',
                'contents': [
                    {'type': 'text', 'text': 'Header text'}
                ]
            },
            'hero': {
                'type': 'image',
                'url': 'https://example.com/flex/images/image.jpg'
            },
            'body': {
                'type': 'box',
                'layout': 'vertical',
                'contents': [
                    {'type': 'text', 'text': 'Body text'}
                ]
            },
            'footer': {
                'type': 'box',
                'layout': 'vertical',
                'contents': [
                    {'type': 'text', 'text': 'Footer text'}
                ]
            },
            'styles': {
                'header': {
                    'backgroundColor': '#00ffff'
                },
                'hero': {
                    'separator': True,
                    'separatorColor': '#000000'
                },
                'footer': {
                    'backgroundColor': '#00ffff',
                    'separator': True,
                    'separatorColor': '#000000'
                }
            }
        }
        self.assertEqual(
            bubble_container_arg,
            BubbleContainer(**bubble_container_arg).as_json_dict()
        )

    def test_bubble_style(self):
        bubble_style_arg = {
            'header': {
                'backgroundColor': '#00ffff'
            },
            'hero': {
                'separator': True,
                'separatorColor': '#000000'
            },
            'footer': {
                'backgroundColor': '#00ffff',
                'separator': True,
                'separatorColor': '#000000'
            }
        }
        self.assertEqual(
            bubble_style_arg,
            BubbleStyle(**bubble_style_arg).as_json_dict()
        )

    def test_block_style(self):
        block_style_arg = {
            'background_color': '#00ffff',
            'separator': True,
            'separator_color': '#000000'
        }
        self.assertEqual(
            {to_camel_case(k): v for k, v in block_style_arg.items()},
            BlockStyle(**block_style_arg).as_json_dict()
        )

    def test_carousel_container(self):
        carousel_container_arg = {
            'type': 'carousel',
            'contents': [
                {
                    'type': 'bubble',
                    'body': {
                        'type': 'box',
                        'layout': 'vertical',
                        'contents': [
                            {'type': 'text', 'text': 'First bubble'}
                        ]
                    }
                },
                {
                    'type': 'bubble',
                    'body': {
                        'type': 'box',
                        'layout': 'vertical',
                        'contents': [
                            {'type': 'text', 'text': 'Second bubble'}
                        ]
                    }
                }
            ]
        }
        self.assertEqual(
            carousel_container_arg,
            CarouselContainer(**carousel_container_arg).as_json_dict()
        )

    def test_box_component(self):
        box_component_arg = {
            'type': 'box',
            'layout': 'vertical',
            'contents': [
                {
                    'type': 'image',
                    'url': 'https://example.com/flex/images/image.jpg'
                },
                {'type': 'separator'},
                {'type': 'text', 'text': 'Text in the box'}
            ]
        }
        self.assertEqual(
            box_component_arg,
            BoxComponent(**box_component_arg).as_json_dict()
        )

    def test_button_component(self):
        button_component_arg = {
            'type': 'button',
            'action': {
                'type': 'uri',
                'label': 'Tap me',
                'uri': 'https://example.com'
            },
            'style': 'primary',
            'color': '#0000ff'
        }
        self.assertEqual(
            button_component_arg,
            ButtonComponent(**button_component_arg).as_json_dict()
        )

    def test_filler_component(self):
        filler_component_arg = {
            'type': 'filler'
        }
        self.assertEqual(
            filler_component_arg,
            FillerComponent(**filler_component_arg).as_json_dict()
        )

    def test_icon_component(self):
        icon_component_arg = {
            'type': 'icon',
            'url': 'https://example.com/icon/png/caution.png',
            'size': 'lg',
            'aspect_ratio': '1.91:1'
        }
        self.assertEqual(
            {to_camel_case(k): v for k, v in icon_component_arg.items()},
            IconComponent(**icon_component_arg).as_json_dict()
        )

    def test_image_component(self):
        image_component_arg = {
            'type': 'image',
            'url': 'https://example.com/flex/images/image.jpg',
            'size': 'full',
            'aspect_ratio': '1.91:1'
        }
        self.assertEqual(
            {to_camel_case(k): v for k, v in image_component_arg.items()},
            ImageComponent(**image_component_arg).as_json_dict()
        )

    def test_separator_component(self):
        separator_component_arg = {
            'type': 'separator',
            'color': '#000000'
        }
        self.assertEqual(
            separator_component_arg,
            SeparatorComponent(**separator_component_arg).as_json_dict()
        )

    def test_spacer_component(self):
        spacer_component_arg = {
            'type': 'spacer',
            'size': 'md'
        }
        self.assertEqual(
            spacer_component_arg,
            SpacerComponent(**spacer_component_arg).as_json_dict()
        )

    def test_text_component(self):
        text_component_arg = {
            'type': 'text',
            'text': 'Hello, World!',
            'size': 'xl',
            'weight': 'bold',
            'color': '#0000ff'
        }
        self.assertEqual(
            text_component_arg,
            TextComponent(**text_component_arg).as_json_dict()
        )


if __name__ == '__main__':
    unittest.main()
