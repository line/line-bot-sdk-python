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

from linebot.models import TextMessage
from linebot.models.emojis import Emojis
from linebot.models.mentionee import Mentionee
from linebot.models.mention import Mention
from tests.models.serialize_test_case import SerializeTestCase


class TestTextMessage(SerializeTestCase):
    def test_emojis(self):
        arg = {
            "type": "text",
            "text": "$ LINE emoji $",
            'emojis': [
                Emojis(
                    index=0,
                    length=6,
                    product_id='5ac1bfd5040ab15980c9b435',
                    emoji_id='001'
                ),
                Emojis(
                    index=13,
                    length=6,
                    product_id='5ac1bfd5040ab15980c9b435',
                    emoji_id='002'
                ),
            ]
        }
        self.assertEqual(
            self.serialize_as_dict(arg, type=self.TEXT),
            TextMessage(**arg).as_json_dict()
        )

    def test_null_emojis(self):
        arg = {
            "type": "text",
            "text": "\uDBC0\uDC84 LINE original emoji"
        }
        self.assertEqual(
            self.serialize_as_dict(arg, type=self.TEXT),
            TextMessage(**arg).as_json_dict()
        )

    def test_mention(self):
        arg = {
            "type": "text",
            "text": "@example Hello, world! (love)",
            "mention": Mention(
                mentionees=[
                    Mentionee(
                        index=0,
                        length=8,
                        user_id="U850014438e..."
                    )
                ]
            ),
        }
        self.assertEqual(
            self.serialize_as_dict(arg, type=self.TEXT),
            TextMessage(**arg).as_json_dict(),
        )

    def test_null_mention(self):
        arg = {"type": "text", "text": "Hello, world!"}
        self.assertEqual(
            self.serialize_as_dict(arg, type=self.TEXT),
            TextMessage(**arg).as_json_dict(),
        )


if __name__ == '__main__':
    unittest.main()
