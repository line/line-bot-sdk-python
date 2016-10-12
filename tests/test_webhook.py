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

import os
import unittest

from builtins import open
from linebot import (
    SignatureValidator, WebhookParser, WebhookHandler
)
from linebot.models import (
    MessageEvent, FollowEvent, UnfollowEvent, JoinEvent,
    LeaveEvent, PostbackEvent, BeaconEvent,
    TextMessage, ImageMessage, VideoMessage, AudioMessage,
    LocationMessage, StickerMessage,
    SourceUser, SourceRoom, SourceGroup,
)


class TestSignatureValidator(unittest.TestCase):
    def test_validate(self):
        signature_validator = SignatureValidator('channel_secret')

        self.assertEqual(
            signature_validator.validate(
                'bodybodybodybody', '/gg9a+LvFevTH1sd7XCQycD7tsWclCsInj7MhBHxN7k='),
            True
        )
        self.assertEqual(
            signature_validator.validate(
                'bodybodybodybody', 'invalid_signature'),
            False
        )


class TestWebhookParser(unittest.TestCase):
    def test_parse(self):
        file_dir = os.path.dirname(__file__)
        webhook_sample_json_path = os.path.join(file_dir, 'text', 'webhook.json')
        with open(webhook_sample_json_path) as fp:
            body = fp.read()

        parser = WebhookParser('channel_secret')
        # mock
        parser.signature_validator.validate = lambda a, b: True

        events = parser.parse(body, 'channel_secret')

        # MessageEvent, SourceUser, TextMessage
        self.assertIsInstance(events[0], MessageEvent)
        self.assertEqual(events[0].reply_token, 'nHuyWiB7yP5Zw52FIkcQobQuGDXCTA')
        self.assertEqual(events[0].type, 'message')
        self.assertEqual(events[0].timestamp, 1462629479859)
        self.assertIsInstance(events[0].source, SourceUser)
        self.assertEqual(events[0].source.type, 'user')
        self.assertEqual(events[0].source.user_id, 'U206d25c2ea6bd87c17655609a1c37cb8')
        self.assertEqual(events[0].source.sender_id, 'U206d25c2ea6bd87c17655609a1c37cb8')
        self.assertIsInstance(events[0].message, TextMessage)
        self.assertEqual(events[0].message.id, '325708')
        self.assertEqual(events[0].message.type, 'text')
        self.assertEqual(events[0].message.text, 'Hello, world')

        # MessageEvent, SourceRoom, TextMessage
        self.assertIsInstance(events[1], MessageEvent)
        self.assertEqual(events[1].reply_token, 'nHuyWiB7yP5Zw52FIkcQobQuGDXCTA')
        self.assertEqual(events[1].type, 'message')
        self.assertEqual(events[1].timestamp, 1462629479859)
        self.assertIsInstance(events[1].source, SourceRoom)
        self.assertEqual(events[1].source.type, 'room')
        self.assertEqual(events[1].source.room_id, 'U206d25c2ea6bd87c17655609a1c37cb8')
        self.assertEqual(events[1].source.sender_id, 'U206d25c2ea6bd87c17655609a1c37cb8')
        self.assertIsInstance(events[1].message, ImageMessage)
        self.assertEqual(events[1].message.id, '325708')
        self.assertEqual(events[1].message.type, 'image')

        # MessageEvent, SourceUser, VideoMessage
        self.assertIsInstance(events[2], MessageEvent)
        self.assertEqual(events[2].reply_token, 'nHuyWiB7yP5Zw52FIkcQobQuGDXCTA')
        self.assertEqual(events[2].type, 'message')
        self.assertEqual(events[2].timestamp, 1462629479859)
        self.assertIsInstance(events[2].source, SourceUser)
        self.assertEqual(events[2].source.type, 'user')
        self.assertEqual(events[2].source.user_id, 'U206d25c2ea6bd87c17655609a1c37cb8')
        self.assertEqual(events[2].source.sender_id, 'U206d25c2ea6bd87c17655609a1c37cb8')
        self.assertIsInstance(events[2].message, VideoMessage)
        self.assertEqual(events[2].message.id, '325708')
        self.assertEqual(events[2].message.type, 'video')

        # MessageEvent, SourceUser, AudioMessage
        self.assertIsInstance(events[3], MessageEvent)
        self.assertEqual(events[3].reply_token, 'nHuyWiB7yP5Zw52FIkcQobQuGDXCTA')
        self.assertEqual(events[3].type, 'message')
        self.assertEqual(events[3].timestamp, 1462629479859)
        self.assertIsInstance(events[3].source, SourceUser)
        self.assertEqual(events[3].source.type, 'user')
        self.assertEqual(events[3].source.user_id, 'U206d25c2ea6bd87c17655609a1c37cb8')
        self.assertEqual(events[3].source.sender_id, 'U206d25c2ea6bd87c17655609a1c37cb8')
        self.assertIsInstance(events[3].message, AudioMessage)
        self.assertEqual(events[3].message.id, '325708')
        self.assertEqual(events[3].message.type, 'audio')

        # MessageEvent, SourceUser, LocationMessage
        self.assertIsInstance(events[4], MessageEvent)
        self.assertEqual(events[4].reply_token, 'nHuyWiB7yP5Zw52FIkcQobQuGDXCTA')
        self.assertEqual(events[4].type, 'message')
        self.assertEqual(events[4].timestamp, 1462629479859)
        self.assertIsInstance(events[4].source, SourceUser)
        self.assertEqual(events[4].source.type, 'user')
        self.assertEqual(events[4].source.user_id, 'U206d25c2ea6bd87c17655609a1c37cb8')
        self.assertEqual(events[4].source.sender_id, 'U206d25c2ea6bd87c17655609a1c37cb8')
        self.assertIsInstance(events[4].message, LocationMessage)
        self.assertEqual(events[4].message.id, '325708')
        self.assertEqual(events[4].message.type, 'location')
        self.assertEqual(events[4].message.title, 'my location')
        self.assertEqual(events[4].message.address, 'Tokyo')
        self.assertEqual(events[4].message.latitude, 35.65910807942215)
        self.assertEqual(events[4].message.longitude, 139.70372892916203)

        # MessageEvent, SourceUser, StickerMessage
        self.assertIsInstance(events[5], MessageEvent)
        self.assertEqual(events[5].reply_token, 'nHuyWiB7yP5Zw52FIkcQobQuGDXCTA')
        self.assertEqual(events[5].type, 'message')
        self.assertEqual(events[5].timestamp, 1462629479859)
        self.assertIsInstance(events[5].source, SourceUser)
        self.assertEqual(events[5].source.type, 'user')
        self.assertEqual(events[5].source.user_id, 'U206d25c2ea6bd87c17655609a1c37cb8')
        self.assertEqual(events[5].source.sender_id, 'U206d25c2ea6bd87c17655609a1c37cb8')
        self.assertIsInstance(events[5].message, StickerMessage)
        self.assertEqual(events[5].message.id, '325708')
        self.assertEqual(events[5].message.type, 'sticker')
        self.assertEqual(events[5].message.package_id, '1')
        self.assertEqual(events[5].message.sticker_id, '1')

        # FollowEvent, SourceUser
        self.assertIsInstance(events[6], FollowEvent)
        self.assertEqual(events[6].reply_token, 'nHuyWiB7yP5Zw52FIkcQobQuGDXCTA')
        self.assertEqual(events[6].type, 'follow')
        self.assertEqual(events[6].timestamp, 1462629479859)
        self.assertIsInstance(events[6].source, SourceUser)
        self.assertEqual(events[6].source.type, 'user')
        self.assertEqual(events[6].source.user_id, 'U206d25c2ea6bd87c17655609a1c37cb8')
        self.assertEqual(events[6].source.sender_id, 'U206d25c2ea6bd87c17655609a1c37cb8')

        # UnfollowEvent, SourceUser
        self.assertIsInstance(events[7], UnfollowEvent)
        self.assertEqual(events[7].type, 'unfollow')
        self.assertEqual(events[7].timestamp, 1462629479859)
        self.assertIsInstance(events[7].source, SourceUser)
        self.assertEqual(events[7].source.type, 'user')
        self.assertEqual(events[7].source.user_id, 'U206d25c2ea6bd87c17655609a1c37cb8')
        self.assertEqual(events[7].source.sender_id, 'U206d25c2ea6bd87c17655609a1c37cb8')

        # JoinEvent, SourceGroup
        self.assertIsInstance(events[8], JoinEvent)
        self.assertEqual(events[8].reply_token, 'nHuyWiB7yP5Zw52FIkcQobQuGDXCTA')
        self.assertEqual(events[8].type, 'join')
        self.assertEqual(events[8].timestamp, 1462629479859)
        self.assertIsInstance(events[8].source, SourceGroup)
        self.assertEqual(events[8].source.type, 'group')
        self.assertEqual(events[8].source.group_id, 'cxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
        self.assertEqual(events[8].source.sender_id, 'cxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')

        # LeaveEvent, SourceGroup
        self.assertIsInstance(events[9], LeaveEvent)
        self.assertEqual(events[9].type, 'leave')
        self.assertEqual(events[9].timestamp, 1462629479859)
        self.assertIsInstance(events[9].source, SourceGroup)
        self.assertEqual(events[9].source.type, 'group')
        self.assertEqual(events[9].source.group_id, 'cxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
        self.assertEqual(events[9].source.sender_id, 'cxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')

        # PostbackEvent, SourceUser
        self.assertIsInstance(events[10], PostbackEvent)
        self.assertEqual(events[10].reply_token, 'nHuyWiB7yP5Zw52FIkcQobQuGDXCTA')
        self.assertEqual(events[10].type, 'postback')
        self.assertEqual(events[10].timestamp, 1462629479859)
        self.assertIsInstance(events[10].source, SourceUser)
        self.assertEqual(events[10].source.type, 'user')
        self.assertEqual(events[10].source.user_id, 'U206d25c2ea6bd87c17655609a1c37cb8')
        self.assertEqual(events[10].source.sender_id, 'U206d25c2ea6bd87c17655609a1c37cb8')
        self.assertEqual(events[10].postback.data, 'action=buyItem&itemId=123123&color=red')

        # BeaconEvent, SourceUser
        self.assertIsInstance(events[11], BeaconEvent)
        self.assertEqual(events[11].reply_token, 'nHuyWiB7yP5Zw52FIkcQobQuGDXCTA')
        self.assertEqual(events[11].type, 'beacon')
        self.assertEqual(events[11].timestamp, 1462629479859)
        self.assertIsInstance(events[11].source, SourceUser)
        self.assertEqual(events[11].source.type, 'user')
        self.assertEqual(events[11].source.user_id, 'U206d25c2ea6bd87c17655609a1c37cb8')
        self.assertEqual(events[11].source.sender_id, 'U206d25c2ea6bd87c17655609a1c37cb8')
        self.assertEqual(events[11].beacon.hwid, 'd41d8cd98f')
        self.assertEqual(events[11].beacon.type, 'enter')


class TestWebhookHandler(unittest.TestCase):
    def setUp(self):
        self.handler = WebhookHandler('channel_secret')
        self.calls = []

        @self.handler.add(MessageEvent, message=TextMessage)
        def message_text(event):
            self.calls.append('1 ' + event.type + '_' + event.message.type)

        @self.handler.add(
            MessageEvent, message=(ImageMessage, VideoMessage, AudioMessage))
        def message_content(event):
            self.calls.append('2 ' + event.type + '_' + event.message.type)

        @self.handler.add(MessageEvent, message=StickerMessage)
        def message_sticker(event):
            self.calls.append('3 ' + event.type + '_' + event.message.type)

        @self.handler.add(MessageEvent)
        def message(event):
            self.calls.append(event.type + '_' + event.message.type)

        @self.handler.add(FollowEvent)
        def follow(event):
            self.calls.append('4 ' + event.type)

        @self.handler.add(JoinEvent)
        def join(event):
            self.calls.append('5 ' + event.type)

        @self.handler.add(PostbackEvent)
        def postback(event):
            self.calls.append('6 ' + event.type)

        @self.handler.add(BeaconEvent)
        def beacon(event):
            self.calls.append('7 ' + event.type)

        @self.handler.default()
        def default(event):
            self.calls.append('default ' + event.type)

    def test_handler(self):
        file_dir = os.path.dirname(__file__)
        webhook_sample_json_path = os.path.join(file_dir, 'text', 'webhook.json')
        with open(webhook_sample_json_path) as fp:
            body = fp.read()

        # mock
        self.handler.parser.signature_validator.validate = lambda a, b: True

        self.handler.handle(body, 'signature')

        self.assertEqual(self.calls[0], '1 message_text')
        self.assertEqual(self.calls[1], '2 message_image')
        self.assertEqual(self.calls[2], '2 message_video')
        self.assertEqual(self.calls[3], '2 message_audio')
        self.assertEqual(self.calls[4], 'message_location')
        self.assertEqual(self.calls[5], '3 message_sticker')
        self.assertEqual(self.calls[6], '4 follow')
        self.assertEqual(self.calls[7], 'default unfollow')
        self.assertEqual(self.calls[8], '5 join')
        self.assertEqual(self.calls[9], 'default leave')
        self.assertEqual(self.calls[10], '6 postback')
        self.assertEqual(self.calls[11], '7 beacon')


if __name__ == '__main__':
    unittest.main()
