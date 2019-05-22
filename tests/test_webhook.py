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
    LeaveEvent, PostbackEvent, BeaconEvent, AccountLinkEvent,
    MemberJoinedEvent, MemberLeftEvent, ThingsEvent,
    TextMessage, ImageMessage, VideoMessage, AudioMessage,
    LocationMessage, StickerMessage, FileMessage,
    SourceUser, SourceRoom, SourceGroup
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
        self.assertEqual(events[1].source.room_id, 'Ra8dbf4673c4c812cd491258042226c99')
        self.assertEqual(events[1].source.user_id, None)
        self.assertEqual(events[1].source.sender_id, 'Ra8dbf4673c4c812cd491258042226c99')
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
        self.assertEqual(events[8].source.group_id, 'Ca56f94637cc4347f90a25382909b24b9')
        self.assertEqual(events[8].source.user_id, None)
        self.assertEqual(events[8].source.sender_id, 'Ca56f94637cc4347f90a25382909b24b9')

        # LeaveEvent, SourceGroup
        self.assertIsInstance(events[9], LeaveEvent)
        self.assertEqual(events[9].type, 'leave')
        self.assertEqual(events[9].timestamp, 1462629479859)
        self.assertIsInstance(events[9].source, SourceGroup)
        self.assertEqual(events[9].source.type, 'group')
        self.assertEqual(events[9].source.group_id, 'Ca56f94637cc4347f90a25382909b24b9')
        self.assertEqual(events[9].source.user_id, None)
        self.assertEqual(events[9].source.sender_id, 'Ca56f94637cc4347f90a25382909b24b9')

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
        self.assertEqual(events[10].postback.params, None)

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
        self.assertEqual(events[11].beacon.dm, None)
        self.assertEqual(events[11].beacon.device_message, None)

        # BeaconEvent, SourceUser (with device message)
        self.assertIsInstance(events[12], BeaconEvent)
        self.assertEqual(events[12].reply_token, 'nHuyWiB7yP5Zw52FIkcQobQuGDXCTA')
        self.assertEqual(events[12].type, 'beacon')
        self.assertEqual(events[12].timestamp, 1462629479859)
        self.assertIsInstance(events[12].source, SourceUser)
        self.assertEqual(events[12].source.type, 'user')
        self.assertEqual(events[12].source.user_id, 'U206d25c2ea6bd87c17655609a1c37cb8')
        self.assertEqual(events[12].source.sender_id, 'U206d25c2ea6bd87c17655609a1c37cb8')
        self.assertEqual(events[12].beacon.hwid, 'd41d8cd98f')
        self.assertEqual(events[12].beacon.type, 'enter')
        self.assertEqual(events[12].beacon.dm, '1234567890abcdef')
        self.assertEqual(events[12].beacon.device_message, bytearray(b'\x124Vx\x90\xab\xcd\xef'))

        # AccountEvent, SourceUser
        self.assertIsInstance(events[13], AccountLinkEvent)
        self.assertEqual(events[13].reply_token, 'nHuyWiB7yP5Zw52FIkcQobQuGDXCTA')
        self.assertEqual(events[13].type, 'accountLink')
        self.assertEqual(events[13].timestamp, 1462629479859)
        self.assertIsInstance(events[13].source, SourceUser)
        self.assertEqual(events[13].source.type, 'user')
        self.assertEqual(events[13].source.user_id, 'U206d25c2ea6bd87c17655609a1c37cb8')
        self.assertEqual(events[13].source.sender_id, 'U206d25c2ea6bd87c17655609a1c37cb8')
        self.assertEqual(events[13].link.result, 'ok')
        self.assertEqual(events[13].link.nonce, 'Vb771wDYtXuammLszK6h9A')

        # MessageEvent, SourceGroup with userId, TextMessage
        self.assertIsInstance(events[14], MessageEvent)
        self.assertEqual(events[14].reply_token, 'nHuyWiB7yP5Zw52FIkcQobQuGDXCTA')
        self.assertEqual(events[14].type, 'message')
        self.assertEqual(events[14].timestamp, 1462629479859)
        self.assertIsInstance(events[14].source, SourceGroup)
        self.assertEqual(events[14].source.type, 'group')
        self.assertEqual(events[14].source.group_id, 'Ca56f94637cc4347f90a25382909b24b9')
        self.assertEqual(events[14].source.user_id, 'U206d25c2ea6bd87c17655609a1c37cb8')
        self.assertEqual(events[14].source.sender_id, 'Ca56f94637cc4347f90a25382909b24b9')
        self.assertIsInstance(events[14].message, TextMessage)
        self.assertEqual(events[14].message.id, '325708')
        self.assertEqual(events[14].message.type, 'text')
        self.assertEqual(events[14].message.text, 'Hello, world')

        # MessageEvent, SourceRoom with userId, TextMessage
        self.assertIsInstance(events[15], MessageEvent)
        self.assertEqual(events[15].reply_token, 'nHuyWiB7yP5Zw52FIkcQobQuGDXCTA')
        self.assertEqual(events[15].type, 'message')
        self.assertEqual(events[15].timestamp, 1462629479859)
        self.assertIsInstance(events[15].source, SourceRoom)
        self.assertEqual(events[15].source.type, 'room')
        self.assertEqual(events[15].source.room_id, 'Ra8dbf4673c4c812cd491258042226c99')
        self.assertEqual(events[15].source.user_id, 'U206d25c2ea6bd87c17655609a1c37cb8')
        self.assertEqual(events[15].source.sender_id, 'Ra8dbf4673c4c812cd491258042226c99')
        self.assertIsInstance(events[15].message, TextMessage)
        self.assertEqual(events[15].message.id, '325708')
        self.assertEqual(events[15].message.type, 'text')
        self.assertEqual(events[15].message.text, 'Hello, world')

        # PostbackEvent, SourceUser, with date params
        self.assertIsInstance(events[16], PostbackEvent)
        self.assertEqual(events[16].reply_token, 'nHuyWiB7yP5Zw52FIkcQobQuGDXCTA')
        self.assertEqual(events[16].type, 'postback')
        self.assertEqual(events[16].timestamp, 1462629479859)
        self.assertIsInstance(events[16].source, SourceUser)
        self.assertEqual(events[16].source.type, 'user')
        self.assertEqual(events[16].source.user_id, 'U206d25c2ea6bd87c17655609a1c37cb8')
        self.assertEqual(events[16].source.sender_id, 'U206d25c2ea6bd87c17655609a1c37cb8')
        self.assertEqual(events[16].postback.data, 'action=buyItem&itemId=123123&color=red')
        self.assertEqual(events[16].postback.params['date'], '2013-04-01')

        # PostbackEvent, SourceUser, with date params
        self.assertIsInstance(events[17], PostbackEvent)
        self.assertEqual(events[17].reply_token, 'nHuyWiB7yP5Zw52FIkcQobQuGDXCTA')
        self.assertEqual(events[17].type, 'postback')
        self.assertEqual(events[17].timestamp, 1462629479859)
        self.assertIsInstance(events[17].source, SourceUser)
        self.assertEqual(events[17].source.type, 'user')
        self.assertEqual(events[17].source.user_id, 'U206d25c2ea6bd87c17655609a1c37cb8')
        self.assertEqual(events[17].source.sender_id, 'U206d25c2ea6bd87c17655609a1c37cb8')
        self.assertEqual(events[17].postback.data, 'action=buyItem&itemId=123123&color=red')
        self.assertEqual(events[17].postback.params['time'], '10:00')

        # PostbackEvent, SourceUser, with date params
        self.assertIsInstance(events[18], PostbackEvent)
        self.assertEqual(events[18].reply_token, 'nHuyWiB7yP5Zw52FIkcQobQuGDXCTA')
        self.assertEqual(events[18].type, 'postback')
        self.assertEqual(events[18].timestamp, 1462629479859)
        self.assertIsInstance(events[18].source, SourceUser)
        self.assertEqual(events[18].source.type, 'user')
        self.assertEqual(events[18].source.user_id, 'U206d25c2ea6bd87c17655609a1c37cb8')
        self.assertEqual(events[18].source.sender_id, 'U206d25c2ea6bd87c17655609a1c37cb8')
        self.assertEqual(events[18].postback.data, 'action=buyItem&itemId=123123&color=red')
        self.assertEqual(events[18].postback.params['datetime'], '2013-04-01T10:00')

        # ThingsEvent, SourceUser, link
        self.assertIsInstance(events[19], ThingsEvent)
        self.assertEqual(events[19].reply_token, 'nHuyWiB7yP5Zw52FIkcQobQuGDXCTA')
        self.assertEqual(events[19].type, 'things')
        self.assertEqual(events[19].timestamp, 1462629479859)
        self.assertIsInstance(events[19].source, SourceUser)
        self.assertEqual(events[19].source.type, 'user')
        self.assertEqual(events[19].source.user_id, 'U206d25c2ea6bd87c17655609a1c37cb8')
        self.assertEqual(events[19].things.device_id, 't2c449c9d1')
        self.assertEqual(events[19].things.type, 'link')

        # MemberJoinedEvent
        self.assertIsInstance(events[20], MemberJoinedEvent)
        self.assertEqual(events[20].reply_token, '0f3779fba3b349968c5d07db31eabf65')
        self.assertEqual(events[20].type, 'memberJoined')
        self.assertEqual(events[20].timestamp, 1462629479859)
        self.assertIsInstance(events[20].source, SourceGroup)
        self.assertEqual(events[20].source.type, 'group')
        self.assertEqual(events[20].source.group_id, 'C4af4980629...')
        self.assertEqual(len(events[20].joined.members), 2)
        self.assertIsInstance(events[20].joined.members[0], SourceUser)
        self.assertEqual(events[20].joined.members[0].user_id, 'U4af4980629...')
        self.assertEqual(events[20].joined.members[1].user_id, 'U91eeaf62d9...')

        # MemberLeftEvent
        self.assertIsInstance(events[21], MemberLeftEvent)
        self.assertEqual(events[21].type, 'memberLeft')
        self.assertEqual(events[21].timestamp, 1462629479960)
        self.assertIsInstance(events[21].source, SourceGroup)
        self.assertEqual(events[21].source.type, 'group')
        self.assertEqual(events[21].source.group_id, 'C4af4980629...')
        self.assertEqual(len(events[21].left.members), 2)
        self.assertIsInstance(events[21].left.members[0], SourceUser)
        self.assertEqual(events[21].left.members[0].user_id, 'U4af4980629...')
        self.assertEqual(events[21].left.members[1].user_id, 'U91eeaf62d9...')

        # ThingsEvent, SourceUser, unlink
        self.assertIsInstance(events[22], ThingsEvent)
        self.assertEqual(events[22].reply_token, 'nHuyWiB7yP5Zw52FIkcQobQuGDXCTA')
        self.assertEqual(events[22].type, 'things')
        self.assertEqual(events[22].timestamp, 1462629479859)
        self.assertIsInstance(events[22].source, SourceUser)
        self.assertEqual(events[22].source.type, 'user')
        self.assertEqual(events[22].source.user_id, 'U206d25c2ea6bd87c17655609a1c37cb8')
        self.assertEqual(events[22].things.device_id, 't2c449c9d1')
        self.assertEqual(events[22].things.type, 'unlink')

        # MessageEvent, SourceUser, FileMessage
        self.assertIsInstance(events[23], MessageEvent)
        self.assertEqual(events[23].reply_token, 'nHuyWiB7yP5Zw52FIkcQobQuGDXCTA')
        self.assertEqual(events[23].type, 'message')
        self.assertEqual(events[23].timestamp, 1462629479859)
        self.assertIsInstance(events[23].source, SourceUser)
        self.assertEqual(events[23].source.type, 'user')
        self.assertEqual(events[23].source.user_id, 'U206d25c2ea6bd87c17655609a1c37cb8')
        self.assertEqual(events[23].source.sender_id, 'U206d25c2ea6bd87c17655609a1c37cb8')
        self.assertIsInstance(events[23].message, FileMessage)
        self.assertEqual(events[23].message.id, '325708')
        self.assertEqual(events[23].message.type, 'file')
        self.assertEqual(events[23].message.file_name, "file.txt")
        self.assertEqual(events[23].message.file_size, 2138)


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

        @self.handler.add(AccountLinkEvent)
        def account_link(event):
            self.calls.append('8 ' + event.type)

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
        self.assertEqual(self.calls[12], '7 beacon')
        self.assertEqual(self.calls[13], '8 accountLink')
        self.assertEqual(self.calls[14], '1 message_text')
        self.assertEqual(self.calls[15], '1 message_text')
        self.assertEqual(self.calls[16], '6 postback')
        self.assertEqual(self.calls[17], '6 postback')
        self.assertEqual(self.calls[18], '6 postback')


if __name__ == '__main__':
    unittest.main()
