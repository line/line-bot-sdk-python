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

from __future__ import unicode_literals, absolute_import

import unittest

from linebot.utils import to_camel_case
from linebot.models import (
    TemplateSendMessage,
    ButtonsTemplate,
    ConfirmTemplate,
    CarouselTemplate,
    ImageCarouselTemplate,
)


class TestTemplate(unittest.TestCase):
    def test_template(self):
        arg = {
            "type": "template",
            "alt_text": "This is a buttons template",
            "template": {
                "type": "buttons",
                "thumbnailImageUrl": "https://example.com/bot/images/image.jpg",
                "imageAspectRatio": "rectangle",
                "imageSize": "cover",
                "imageBackgroundColor": "#FFFFFF",
                "title": "Menu",
                "text": "Please select",
                "defaultAction": {
                    "type": "uri",
                    "label": "View detail",
                    "uri": "http://example.com/page/123"
                },
                "actions": [
                    {
                        "type": "postback",
                        "label": "Buy",
                        "data": "action=buy&itemid=123"
                    },
                    {
                        "type": "postback",
                        "label": "Add to cart",
                        "data": "action=add&itemid=123"
                    },
                    {
                        "type": "uri",
                        "label": "View detail",
                        "uri": "http://example.com/page/123"
                    }
                ]
            }
        }
        self.assertEqual(
            {to_camel_case(k): v for k, v in arg.items()},
            TemplateSendMessage(**arg).as_json_dict()
        )

    def test_confirm_template(self):
        arg = {
            "type": "confirm",
            "text": "Are you sure?",
            "actions": [
                {
                    "type": "message",
                    "label": "Yes",
                    "text": "yes"
                },
                {
                    "type": "message",
                    "label": "No",
                    "text": "no"
                }
            ]
        }

        self.assertEqual(
            {to_camel_case(k): v for k, v in arg.items()},
            ConfirmTemplate(**arg).as_json_dict()
        )

    def test_carousel_template(self):
        arg = {
            "type": "carousel",
            "columns": [
                {
                    "thumbnailImageUrl": "https://example.com/bot/images/item1.jpg",
                    "imageBackgroundColor": "#FFFFFF",
                    "title": "this is menu",
                    "text": "description",
                    "defaultAction": {
                        "type": "uri",
                        "label": "View detail",
                        "uri": "http://example.com/page/123"
                    },
                    "actions": [
                        {
                            "type": "postback",
                            "label": "Buy",
                            "data": "action=buy&itemid=111"
                        },
                        {
                            "type": "postback",
                            "label": "Add to cart",
                            "data": "action=add&itemid=111"
                        },
                        {
                            "type": "uri",
                            "label": "View detail",
                            "uri": "http://example.com/page/111"
                        }
                    ]
                },
                {
                    "thumbnailImageUrl": "https://example.com/bot/images/item2.jpg",
                    "imageBackgroundColor": "#000000",
                    "title": "this is menu",
                    "text": "description",
                    "defaultAction": {
                        "type": "uri",
                        "label": "View detail",
                        "uri": "http://example.com/page/222"
                    },
                    "actions": [
                        {
                            "type": "postback",
                            "label": "Buy",
                            "data": "action=buy&itemid=222"
                        },
                        {
                            "type": "postback",
                            "label": "Add to cart",
                            "data": "action=add&itemid=222"
                        },
                        {
                            "type": "uri",
                            "label": "View detail",
                            "uri": "http://example.com/page/222"
                        }
                    ]
                }
            ],
            "imageAspectRatio": "rectangle",
            "imageSize": "cover"
        }
        self.assertEqual(
            {to_camel_case(k): v for k, v in arg.items()},
            CarouselTemplate(**arg).as_json_dict()
        )

    # def test_xxx_template(self):
    #     arg =
    #     self.assertEqual(
    #         {to_camel_case(k): v for k, v in arg.items()},
    #         ButtonsTemplate(**arg).as_json_dict()
    #     )

    def test_xxx_template(self):
        arg = {
                "type": "image_carousel",
                "columns": [
                    {
                        "imageUrl": "https://example.com/bot/images/item1.jpg",
                        "action": {
                            "type": "postback",
                            "label": "Buy",
                            "data": "action=buy&itemid=111"
                        }
                    },
                    {
                        "imageUrl": "https://example.com/bot/images/item2.jpg",
                        "action": {
                            "type": "message",
                            "label": "Yes",
                            "text": "yes"
                        }
                    },
                    {
                        "imageUrl": "https://example.com/bot/images/item3.jpg",
                        "action": {
                            "type": "uri",
                            "label": "View detail",
                            "uri": "http://example.com/page/222"
                        }
                    }
                ]
            }


        self.assertEqual(
            {to_camel_case(k): v for k, v in arg.items()},
            ImageCarouselTemplate(**arg).as_json_dict()
        )



if __name__ == '__main__':
    unittest.main()
