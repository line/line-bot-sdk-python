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
import inspect

from linebot import (
    SignatureValidator, WebhookParser, WebhookHandler
)
from linebot.models import (
    MessageEvent, FollowEvent, UnfollowEvent, JoinEvent,
    LeaveEvent, PostbackEvent, BeaconEvent, AccountLinkEvent,
    MemberJoinedEvent, MemberLeftEvent, ThingsEvent,
    TextMessage, ImageMessage, VideoMessage, AudioMessage,
    LocationMessage, StickerMessage, FileMessage,
    SourceUser, SourceRoom, SourceGroup,
    DeviceLink, DeviceUnlink, ScenarioResult, ActionResult)
from linebot.models.delivery_context import DeliveryContext
from linebot.models.events import UnsendEvent, VideoPlayCompleteEvent
from linebot.models.unsend import Unsend
from linebot.models.video_play_complete import VideoPlayComplete
from linebot.utils import PY3


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
    def setUp(self):
        parser = WebhookParser('channel_secret')
        # mock
        parser.signature_validator.validate = lambda a, b: True
        self.parser = parser

    def test_parse(self):
        file_dir = os.path.dirname(__file__)
        webhook_sample_json_path = os.path.join(file_dir, 'text', 'webhook.json')
        with open(webhook_sample_json_path) as fp:
            body = fp.read()

        events = self.parser.parse(body, 'channel_secret')

        # events count
        self.assertEqual(len(events), 29)

        # MessageEvent, SourceUser, TextMessage
        self.assertIsInstance(events[0], MessageEvent)
        self.assertEqual(events[0].reply_token, 'nHuyWiB7yP5Zw52FIkcQobQuGDXCTA')
        self.assertEqual(events[0].type, 'message')
        self.assertEqual(events[0].mode, 'active')
        self.assertEqual(events[0].timestamp, 1462629479859)
        self.assertIsInstance(events[0].source, SourceUser)
        self.assertEqual(events[0].source.type, 'user')
        self.assertEqual(events[0].source.user_id, 'U206d25c2ea6bd87c17655609a1c37cb8')
        self.assertEqual(events[0].webhook_event_id, 'testwebhookeventid')
        self.assertIsInstance(events[0].delivery_context, DeliveryContext)
        self.assertFalse(events[0].delivery_context.is_redelivery)
        self.assertIsInstance(events[0].message, TextMessage)
        self.assertEqual(events[0].message.id, '325708')
        self.assertEqual(events[0].message.type, 'text')
        self.assertEqual(events[0].message.text, 'Hello, world')

        # MessageEvent, SourceRoom, ImageMessage
        self.assertIsInstance(events[1], MessageEvent)
        self.assertEqual(events[1].reply_token, 'nHuyWiB7yP5Zw52FIkcQobQuGDXCTA')
        self.assertEqual(events[1].type, 'message')
        self.assertEqual(events[1].mode, 'active')
        self.assertEqual(events[1].timestamp, 1462629479859)
        self.assertIsInstance(events[1].source, SourceRoom)
        self.assertEqual(events[1].source.type, 'room')
        self.assertEqual(events[1].source.room_id, 'Ra8dbf4673c4c812cd491258042226c99')
        self.assertEqual(events[1].source.user_id, None)
        self.assertEqual(events[1].webhook_event_id, 'testwebhookeventid')
        self.assertIsInstance(events[1].delivery_context, DeliveryContext)
        self.assertFalse(events[1].delivery_context.is_redelivery)
        self.assertIsInstance(events[1].message, ImageMessage)
        self.assertEqual(events[1].message.id, '325708')
        self.assertEqual(events[1].message.type, 'image')
        self.assertEqual(events[1].message.content_provider.type, 'external')
        self.assertEqual(events[1].message.content_provider.original_content_url,
                         "https://example.com")
        self.assertEqual(events[1].message.content_provider.preview_image_url,
                         "https://example.com")

        # MessageEvent, SourceUser, VideoMessage
        self.assertIsInstance(events[2], MessageEvent)
        self.assertEqual(events[2].reply_token, 'nHuyWiB7yP5Zw52FIkcQobQuGDXCTA')
        self.assertEqual(events[2].type, 'message')
        self.assertEqual(events[2].mode, 'active')
        self.assertEqual(events[2].timestamp, 1462629479859)
        self.assertIsInstance(events[2].source, SourceUser)
        self.assertEqual(events[2].source.type, 'user')
        self.assertEqual(events[2].source.user_id, 'U206d25c2ea6bd87c17655609a1c37cb8')
        self.assertEqual(events[2].webhook_event_id, 'testwebhookeventid')
        self.assertIsInstance(events[2].delivery_context, DeliveryContext)
        self.assertFalse(events[2].delivery_context.is_redelivery)
        self.assertIsInstance(events[2].message, VideoMessage)
        self.assertEqual(events[2].message.id, '325708')
        self.assertEqual(events[2].message.type, 'video')
        self.assertEqual(events[2].message.duration, 60000)
        self.assertEqual(events[2].message.content_provider.type, 'external')
        self.assertEqual(events[2].message.content_provider.original_content_url,
                         "https://example.com")
        self.assertEqual(events[2].message.content_provider.preview_image_url,
                         "https://example.com")

        # MessageEvent, SourceUser, AudioMessage
        self.assertIsInstance(events[3], MessageEvent)
        self.assertEqual(events[3].reply_token, 'nHuyWiB7yP5Zw52FIkcQobQuGDXCTA')
        self.assertEqual(events[3].type, 'message')
        self.assertEqual(events[3].mode, 'active')
        self.assertEqual(events[3].timestamp, 1462629479859)
        self.assertIsInstance(events[3].source, SourceUser)
        self.assertEqual(events[3].source.type, 'user')
        self.assertEqual(events[3].source.user_id, 'U206d25c2ea6bd87c17655609a1c37cb8')
        self.assertEqual(events[3].webhook_event_id, 'testwebhookeventid')
        self.assertIsInstance(events[3].delivery_context, DeliveryContext)
        self.assertFalse(events[3].delivery_context.is_redelivery)
        self.assertIsInstance(events[3].message, AudioMessage)
        self.assertEqual(events[3].message.id, '325708')
        self.assertEqual(events[3].message.type, 'audio')
        self.assertEqual(events[3].message.duration, 60000)
        self.assertEqual(events[3].message.content_provider.type, 'external')
        self.assertEqual(events[3].message.content_provider.original_content_url,
                         "https://example.com")

        # MessageEvent, SourceUser, LocationMessage
        self.assertIsInstance(events[4], MessageEvent)
        self.assertEqual(events[4].reply_token, 'nHuyWiB7yP5Zw52FIkcQobQuGDXCTA')
        self.assertEqual(events[4].type, 'message')
        self.assertEqual(events[4].mode, 'active')
        self.assertEqual(events[4].timestamp, 1462629479859)
        self.assertIsInstance(events[4].source, SourceUser)
        self.assertEqual(events[4].source.type, 'user')
        self.assertEqual(events[4].source.user_id, 'U206d25c2ea6bd87c17655609a1c37cb8')
        self.assertEqual(events[4].webhook_event_id, 'testwebhookeventid')
        self.assertIsInstance(events[4].delivery_context, DeliveryContext)
        self.assertFalse(events[4].delivery_context.is_redelivery)
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
        self.assertEqual(events[5].mode, 'active')
        self.assertEqual(events[5].timestamp, 1462629479859)
        self.assertIsInstance(events[5].source, SourceUser)
        self.assertEqual(events[5].source.type, 'user')
        self.assertEqual(events[5].source.user_id, 'U206d25c2ea6bd87c17655609a1c37cb8')
        self.assertEqual(events[5].webhook_event_id, 'testwebhookeventid')
        self.assertIsInstance(events[5].delivery_context, DeliveryContext)
        self.assertFalse(events[5].delivery_context.is_redelivery)
        self.assertIsInstance(events[5].message, StickerMessage)
        self.assertEqual(events[5].message.id, '325708')
        self.assertEqual(events[5].message.type, 'sticker')
        self.assertEqual(events[5].message.package_id, '1')
        self.assertEqual(events[5].message.sticker_id, '1')
        self.assertEqual(events[5].message.sticker_resource_type, 'STATIC')
        self.assertEqual(events[5].message.keywords[0], 'Love You')
        self.assertEqual(events[5].message.keywords[1], 'Love')
        self.assertEqual(events[5].message.text, 'Just sticker')

        # FollowEvent, SourceUser
        self.assertIsInstance(events[6], FollowEvent)
        self.assertEqual(events[6].reply_token, 'nHuyWiB7yP5Zw52FIkcQobQuGDXCTA')
        self.assertEqual(events[6].type, 'follow')
        self.assertEqual(events[6].mode, 'active')
        self.assertEqual(events[6].timestamp, 1462629479859)
        self.assertIsInstance(events[6].source, SourceUser)
        self.assertEqual(events[6].source.type, 'user')
        self.assertEqual(events[6].source.user_id, 'U206d25c2ea6bd87c17655609a1c37cb8')
        self.assertEqual(events[6].webhook_event_id, 'testwebhookeventid')
        self.assertIsInstance(events[6].delivery_context, DeliveryContext)
        self.assertFalse(events[6].delivery_context.is_redelivery)

        # UnfollowEvent, SourceUser
        self.assertIsInstance(events[7], UnfollowEvent)
        self.assertEqual(events[7].type, 'unfollow')
        self.assertEqual(events[7].mode, 'active')
        self.assertEqual(events[7].timestamp, 1462629479859)
        self.assertIsInstance(events[7].source, SourceUser)
        self.assertEqual(events[7].source.type, 'user')
        self.assertEqual(events[7].source.user_id, 'U206d25c2ea6bd87c17655609a1c37cb8')
        self.assertEqual(events[7].webhook_event_id, 'testwebhookeventid')
        self.assertIsInstance(events[7].delivery_context, DeliveryContext)
        self.assertFalse(events[7].delivery_context.is_redelivery)

        # JoinEvent, SourceGroup
        self.assertIsInstance(events[8], JoinEvent)
        self.assertEqual(events[8].reply_token, 'nHuyWiB7yP5Zw52FIkcQobQuGDXCTA')
        self.assertEqual(events[8].type, 'join')
        self.assertEqual(events[8].mode, 'active')
        self.assertEqual(events[8].timestamp, 1462629479859)
        self.assertIsInstance(events[8].source, SourceGroup)
        self.assertEqual(events[8].source.type, 'group')
        self.assertEqual(events[8].source.group_id, 'Ca56f94637cc4347f90a25382909b24b9')
        self.assertEqual(events[8].source.user_id, None)
        self.assertEqual(events[8].webhook_event_id, 'testwebhookeventid')
        self.assertIsInstance(events[8].delivery_context, DeliveryContext)
        self.assertFalse(events[8].delivery_context.is_redelivery)

        # LeaveEvent, SourceGroup
        self.assertIsInstance(events[9], LeaveEvent)
        self.assertEqual(events[9].type, 'leave')
        self.assertEqual(events[9].mode, 'active')
        self.assertEqual(events[9].timestamp, 1462629479859)
        self.assertIsInstance(events[9].source, SourceGroup)
        self.assertEqual(events[9].source.type, 'group')
        self.assertEqual(events[9].source.group_id, 'Ca56f94637cc4347f90a25382909b24b9')
        self.assertEqual(events[9].source.user_id, None)
        self.assertEqual(events[9].webhook_event_id, 'testwebhookeventid')
        self.assertIsInstance(events[9].delivery_context, DeliveryContext)
        self.assertFalse(events[9].delivery_context.is_redelivery)

        # PostbackEvent, SourceUser
        self.assertIsInstance(events[10], PostbackEvent)
        self.assertEqual(events[10].reply_token, 'nHuyWiB7yP5Zw52FIkcQobQuGDXCTA')
        self.assertEqual(events[10].type, 'postback')
        self.assertEqual(events[10].mode, 'active')
        self.assertEqual(events[10].timestamp, 1462629479859)
        self.assertIsInstance(events[10].source, SourceUser)
        self.assertEqual(events[10].source.type, 'user')
        self.assertEqual(events[10].source.user_id, 'U206d25c2ea6bd87c17655609a1c37cb8')
        self.assertEqual(events[10].webhook_event_id, 'testwebhookeventid')
        self.assertIsInstance(events[10].delivery_context, DeliveryContext)
        self.assertFalse(events[10].delivery_context.is_redelivery)
        self.assertEqual(events[10].postback.data, 'action=buyItem&itemId=123123&color=red')
        self.assertEqual(events[10].postback.params, None)

        # BeaconEvent, SourceUser
        self.assertIsInstance(events[11], BeaconEvent)
        self.assertEqual(events[11].reply_token, 'nHuyWiB7yP5Zw52FIkcQobQuGDXCTA')
        self.assertEqual(events[11].type, 'beacon')
        self.assertEqual(events[11].mode, 'active')
        self.assertEqual(events[11].timestamp, 1462629479859)
        self.assertIsInstance(events[11].source, SourceUser)
        self.assertEqual(events[11].source.type, 'user')
        self.assertEqual(events[11].source.user_id, 'U206d25c2ea6bd87c17655609a1c37cb8')
        self.assertEqual(events[11].webhook_event_id, 'testwebhookeventid')
        self.assertIsInstance(events[11].delivery_context, DeliveryContext)
        self.assertFalse(events[11].delivery_context.is_redelivery)
        self.assertEqual(events[11].beacon.hwid, 'd41d8cd98f')
        self.assertEqual(events[11].beacon.type, 'enter')
        self.assertEqual(events[11].beacon.dm, None)
        self.assertEqual(events[11].beacon.device_message, None)

        # BeaconEvent, SourceUser (with device message)
        self.assertIsInstance(events[12], BeaconEvent)
        self.assertEqual(events[12].reply_token, 'nHuyWiB7yP5Zw52FIkcQobQuGDXCTA')
        self.assertEqual(events[12].type, 'beacon')
        self.assertEqual(events[12].mode, 'active')
        self.assertEqual(events[12].timestamp, 1462629479859)
        self.assertIsInstance(events[12].source, SourceUser)
        self.assertEqual(events[12].source.type, 'user')
        self.assertEqual(events[12].source.user_id, 'U206d25c2ea6bd87c17655609a1c37cb8')
        self.assertEqual(events[12].webhook_event_id, 'testwebhookeventid')
        self.assertIsInstance(events[12].delivery_context, DeliveryContext)
        self.assertFalse(events[12].delivery_context.is_redelivery)
        self.assertEqual(events[12].beacon.hwid, 'd41d8cd98f')
        self.assertEqual(events[12].beacon.type, 'enter')
        self.assertEqual(events[12].beacon.dm, '1234567890abcdef')
        self.assertEqual(events[12].beacon.device_message, bytearray(b'\x124Vx\x90\xab\xcd\xef'))

        # AccountEvent, SourceUser
        self.assertIsInstance(events[13], AccountLinkEvent)
        self.assertEqual(events[13].reply_token, 'nHuyWiB7yP5Zw52FIkcQobQuGDXCTA')
        self.assertEqual(events[13].type, 'accountLink')
        self.assertEqual(events[13].mode, 'active')
        self.assertEqual(events[13].timestamp, 1462629479859)
        self.assertIsInstance(events[13].source, SourceUser)
        self.assertEqual(events[13].source.type, 'user')
        self.assertEqual(events[13].source.user_id, 'U206d25c2ea6bd87c17655609a1c37cb8')
        self.assertEqual(events[13].webhook_event_id, 'testwebhookeventid')
        self.assertIsInstance(events[13].delivery_context, DeliveryContext)
        self.assertFalse(events[13].delivery_context.is_redelivery)
        self.assertEqual(events[13].link.result, 'ok')
        self.assertEqual(events[13].link.nonce, 'Vb771wDYtXuammLszK6h9A')

        # MessageEvent, SourceGroup with userId, TextMessage
        self.assertIsInstance(events[14], MessageEvent)
        self.assertEqual(events[14].reply_token, 'nHuyWiB7yP5Zw52FIkcQobQuGDXCTA')
        self.assertEqual(events[14].type, 'message')
        self.assertEqual(events[14].mode, 'active')
        self.assertEqual(events[14].timestamp, 1462629479859)
        self.assertIsInstance(events[14].source, SourceGroup)
        self.assertEqual(events[14].source.type, 'group')
        self.assertEqual(events[14].source.group_id, 'Ca56f94637cc4347f90a25382909b24b9')
        self.assertEqual(events[14].source.user_id, 'U206d25c2ea6bd87c17655609a1c37cb8')
        self.assertEqual(events[14].webhook_event_id, 'testwebhookeventid')
        self.assertIsInstance(events[14].delivery_context, DeliveryContext)
        self.assertFalse(events[14].delivery_context.is_redelivery)
        self.assertIsInstance(events[14].message, TextMessage)
        self.assertEqual(events[14].message.id, '325708')
        self.assertEqual(events[14].message.type, 'text')
        self.assertEqual(events[14].message.text, 'Hello, world')

        # MessageEvent, SourceRoom with userId, TextMessage
        self.assertIsInstance(events[15], MessageEvent)
        self.assertEqual(events[15].reply_token, 'nHuyWiB7yP5Zw52FIkcQobQuGDXCTA')
        self.assertEqual(events[15].type, 'message')
        self.assertEqual(events[15].mode, 'active')
        self.assertEqual(events[15].timestamp, 1462629479859)
        self.assertIsInstance(events[15].source, SourceRoom)
        self.assertEqual(events[15].source.type, 'room')
        self.assertEqual(events[15].source.room_id, 'Ra8dbf4673c4c812cd491258042226c99')
        self.assertEqual(events[15].source.user_id, 'U206d25c2ea6bd87c17655609a1c37cb8')
        self.assertEqual(events[15].webhook_event_id, 'testwebhookeventid')
        self.assertIsInstance(events[15].delivery_context, DeliveryContext)
        self.assertFalse(events[15].delivery_context.is_redelivery)
        self.assertIsInstance(events[15].message, TextMessage)
        self.assertEqual(events[15].message.id, '325708')
        self.assertEqual(events[15].message.type, 'text')
        self.assertEqual(events[15].message.text, 'Hello, world')

        # PostbackEvent, SourceUser, with date params
        self.assertIsInstance(events[16], PostbackEvent)
        self.assertEqual(events[16].reply_token, 'nHuyWiB7yP5Zw52FIkcQobQuGDXCTA')
        self.assertEqual(events[16].type, 'postback')
        self.assertEqual(events[16].mode, 'active')
        self.assertEqual(events[16].timestamp, 1462629479859)
        self.assertIsInstance(events[16].source, SourceUser)
        self.assertEqual(events[16].source.type, 'user')
        self.assertEqual(events[16].source.user_id, 'U206d25c2ea6bd87c17655609a1c37cb8')
        self.assertEqual(events[16].webhook_event_id, 'testwebhookeventid')
        self.assertIsInstance(events[16].delivery_context, DeliveryContext)
        self.assertFalse(events[16].delivery_context.is_redelivery)
        self.assertEqual(events[16].postback.data, 'action=buyItem&itemId=123123&color=red')
        self.assertEqual(events[16].postback.params['date'], '2013-04-01')

        # PostbackEvent, SourceUser, with date params
        self.assertIsInstance(events[17], PostbackEvent)
        self.assertEqual(events[17].reply_token, 'nHuyWiB7yP5Zw52FIkcQobQuGDXCTA')
        self.assertEqual(events[17].type, 'postback')
        self.assertEqual(events[17].mode, 'active')
        self.assertEqual(events[17].timestamp, 1462629479859)
        self.assertIsInstance(events[17].source, SourceUser)
        self.assertEqual(events[17].source.type, 'user')
        self.assertEqual(events[17].source.user_id, 'U206d25c2ea6bd87c17655609a1c37cb8')
        self.assertEqual(events[17].webhook_event_id, 'testwebhookeventid')
        self.assertIsInstance(events[17].delivery_context, DeliveryContext)
        self.assertFalse(events[17].delivery_context.is_redelivery)
        self.assertEqual(events[17].postback.data, 'action=buyItem&itemId=123123&color=red')
        self.assertEqual(events[17].postback.params['time'], '10:00')

        # PostbackEvent, SourceUser, with date params
        self.assertIsInstance(events[18], PostbackEvent)
        self.assertEqual(events[18].reply_token, 'nHuyWiB7yP5Zw52FIkcQobQuGDXCTA')
        self.assertEqual(events[18].type, 'postback')
        self.assertEqual(events[18].mode, 'active')
        self.assertEqual(events[18].timestamp, 1462629479859)
        self.assertIsInstance(events[18].source, SourceUser)
        self.assertEqual(events[18].source.type, 'user')
        self.assertEqual(events[18].source.user_id, 'U206d25c2ea6bd87c17655609a1c37cb8')
        self.assertEqual(events[18].webhook_event_id, 'testwebhookeventid')
        self.assertIsInstance(events[18].delivery_context, DeliveryContext)
        self.assertFalse(events[18].delivery_context.is_redelivery)
        self.assertEqual(events[18].postback.data, 'action=buyItem&itemId=123123&color=red')
        self.assertEqual(events[18].postback.params['datetime'], '2013-04-01T10:00')

        # ThingsEvent, SourceUser, link
        self.assertIsInstance(events[19], ThingsEvent)
        self.assertEqual(events[19].reply_token, 'nHuyWiB7yP5Zw52FIkcQobQuGDXCTA')
        self.assertEqual(events[19].type, 'things')
        self.assertEqual(events[19].mode, 'active')
        self.assertEqual(events[19].timestamp, 1462629479859)
        self.assertIsInstance(events[19].source, SourceUser)
        self.assertEqual(events[19].source.type, 'user')
        self.assertEqual(events[19].source.user_id, 'U206d25c2ea6bd87c17655609a1c37cb8')
        self.assertEqual(events[19].webhook_event_id, 'testwebhookeventid')
        self.assertIsInstance(events[19].delivery_context, DeliveryContext)
        self.assertFalse(events[19].delivery_context.is_redelivery)
        self.assertIsInstance(events[19].things, DeviceLink)
        self.assertEqual(events[19].things.type, 'link')
        self.assertEqual(events[19].things.device_id, 't2c449c9d1')

        # MemberJoinedEvent
        self.assertIsInstance(events[20], MemberJoinedEvent)
        self.assertEqual(events[20].reply_token, '0f3779fba3b349968c5d07db31eabf65')
        self.assertEqual(events[20].type, 'memberJoined')
        self.assertEqual(events[20].mode, 'active')
        self.assertEqual(events[20].timestamp, 1462629479859)
        self.assertIsInstance(events[20].source, SourceGroup)
        self.assertEqual(events[20].source.type, 'group')
        self.assertEqual(events[20].source.group_id, 'C4af4980629...')
        self.assertEqual(events[20].webhook_event_id, 'testwebhookeventid')
        self.assertIsInstance(events[20].delivery_context, DeliveryContext)
        self.assertFalse(events[20].delivery_context.is_redelivery)
        self.assertEqual(len(events[20].joined.members), 2)
        self.assertIsInstance(events[20].joined.members[0], SourceUser)
        self.assertEqual(events[20].joined.members[0].user_id, 'U4af4980629...')
        self.assertEqual(events[20].joined.members[1].user_id, 'U91eeaf62d9...')

        # MemberLeftEvent
        self.assertIsInstance(events[21], MemberLeftEvent)
        self.assertEqual(events[21].type, 'memberLeft')
        self.assertEqual(events[21].mode, 'active')
        self.assertEqual(events[21].timestamp, 1462629479960)
        self.assertIsInstance(events[21].source, SourceGroup)
        self.assertEqual(events[21].source.type, 'group')
        self.assertEqual(events[21].source.group_id, 'C4af4980629...')
        self.assertEqual(events[21].webhook_event_id, 'testwebhookeventid')
        self.assertIsInstance(events[21].delivery_context, DeliveryContext)
        self.assertFalse(events[21].delivery_context.is_redelivery)
        self.assertEqual(len(events[21].left.members), 2)
        self.assertIsInstance(events[21].left.members[0], SourceUser)
        self.assertEqual(events[21].left.members[0].user_id, 'U4af4980629...')
        self.assertEqual(events[21].left.members[1].user_id, 'U91eeaf62d9...')

        # ThingsEvent, SourceUser, unlink
        self.assertIsInstance(events[22], ThingsEvent)
        self.assertEqual(events[22].reply_token, 'nHuyWiB7yP5Zw52FIkcQobQuGDXCTA')
        self.assertEqual(events[22].type, 'things')
        self.assertEqual(events[22].mode, 'active')
        self.assertEqual(events[22].timestamp, 1462629479859)
        self.assertIsInstance(events[22].source, SourceUser)
        self.assertEqual(events[22].source.type, 'user')
        self.assertEqual(events[22].source.user_id, 'U206d25c2ea6bd87c17655609a1c37cb8')
        self.assertEqual(events[22].webhook_event_id, 'testwebhookeventid')
        self.assertIsInstance(events[22].delivery_context, DeliveryContext)
        self.assertFalse(events[22].delivery_context.is_redelivery)
        self.assertIsInstance(events[22].things, DeviceUnlink)
        self.assertEqual(events[22].things.type, 'unlink')
        self.assertEqual(events[22].things.device_id, 't2c449c9d1')

        # MessageEvent, SourceUser, FileMessage
        self.assertIsInstance(events[23], MessageEvent)
        self.assertEqual(events[23].reply_token, 'nHuyWiB7yP5Zw52FIkcQobQuGDXCTA')
        self.assertEqual(events[23].type, 'message')
        self.assertEqual(events[23].mode, 'active')
        self.assertEqual(events[23].timestamp, 1462629479859)
        self.assertIsInstance(events[23].source, SourceUser)
        self.assertEqual(events[23].source.type, 'user')
        self.assertEqual(events[23].source.user_id, 'U206d25c2ea6bd87c17655609a1c37cb8')
        self.assertEqual(events[23].webhook_event_id, 'testwebhookeventid')
        self.assertIsInstance(events[23].delivery_context, DeliveryContext)
        self.assertFalse(events[23].delivery_context.is_redelivery)
        self.assertIsInstance(events[23].message, FileMessage)
        self.assertEqual(events[23].message.id, '325708')
        self.assertEqual(events[23].message.type, 'file')
        self.assertEqual(events[23].message.file_name, "file.txt")
        self.assertEqual(events[23].message.file_size, 2138)

        # ThingsEvent, SourceUser, scenarioResult
        self.assertIsInstance(events[24], ThingsEvent)
        self.assertEqual(events[24].reply_token, 'nHuyWiB7yP5Zw52FIkcQobQuGDXCTA')
        self.assertEqual(events[24].type, 'things')
        self.assertEqual(events[24].mode, 'active')
        self.assertEqual(events[24].timestamp, 1547817848122)
        self.assertIsInstance(events[24].source, SourceUser)
        self.assertEqual(events[24].source.type, 'user')
        self.assertEqual(events[24].source.user_id, 'U206d25c2ea6bd87c17655609a1c37cb8')
        self.assertEqual(events[24].webhook_event_id, 'testwebhookeventid')
        self.assertIsInstance(events[24].delivery_context, DeliveryContext)
        self.assertFalse(events[24].delivery_context.is_redelivery)
        self.assertIsInstance(events[24].things, ScenarioResult)
        self.assertEqual(events[24].things.type, 'scenarioResult')
        self.assertEqual(events[24].things.device_id, 't2c449c9d1')
        self.assertEqual(events[24].things.result.scenario_id, 'XXX')
        self.assertEqual(events[24].things.result.revision, 2)
        self.assertEqual(events[24].things.result.start_time, 1547817845950)
        self.assertEqual(events[24].things.result.end_time, 1547817845952)
        self.assertEqual(events[24].things.result.result_code, 'success')
        self.assertEqual(events[24].things.result.ble_notification_payload, 'AQ==')
        self.assertIsInstance(events[24].things.result.action_results[0], ActionResult)
        self.assertEqual(events[24].things.result.action_results[0].type, 'binary')
        self.assertEqual(events[24].things.result.action_results[0].data, '/w==')
        self.assertIsInstance(events[24].things.result.action_results[1], ActionResult)
        self.assertEqual(events[24].things.result.action_results[1].type, 'void')

        # UnsendEvent
        self.assertIsInstance(events[25], UnsendEvent)
        self.assertEqual(events[25].type, 'unsend')
        self.assertEqual(events[25].mode, 'active')
        self.assertEqual(events[25].timestamp, 1547817848122)
        self.assertIsInstance(events[25].source, SourceGroup)
        self.assertEqual(events[25].source.type, 'group')
        self.assertEqual(events[25].source.user_id, 'U206d25c2ea6bd87c17655609a1c37cb8')
        self.assertEqual(events[25].webhook_event_id, 'testwebhookeventid')
        self.assertIsInstance(events[25].delivery_context, DeliveryContext)
        self.assertFalse(events[25].delivery_context.is_redelivery)
        self.assertIsInstance(events[25].unsend, Unsend)
        self.assertEqual(events[25].unsend.message_id, '325708')

        # VideoPlayCompleteEvent
        self.assertIsInstance(events[26], VideoPlayCompleteEvent)
        self.assertEqual(events[26].reply_token, 'nHuyWiB7yP5Zw52FIkcQobQuGDXCTA')
        self.assertEqual(events[26].type, 'videoPlayComplete')
        self.assertEqual(events[26].mode, 'active')
        self.assertEqual(events[26].timestamp, 1462629479859)
        self.assertIsInstance(events[26].source, SourceUser)
        self.assertEqual(events[26].source.type, 'user')
        self.assertEqual(events[26].source.user_id, 'U206d25c2ea6bd87c17655609a1c37cb8')
        self.assertEqual(events[26].webhook_event_id, 'testwebhookeventid')
        self.assertIsInstance(events[26].delivery_context, DeliveryContext)
        self.assertFalse(events[26].delivery_context.is_redelivery)
        self.assertIsInstance(events[26].video_play_complete, VideoPlayComplete)
        self.assertEqual(events[26].video_play_complete.tracking_id, 'track_id')

        # MessageEvent, SourceUser, ImageMessage with ImageSet
        self.assertIsInstance(events[1], MessageEvent)
        self.assertEqual(events[27].reply_token, 'fbf94e269485410da6b7e3a5e33283e8')
        self.assertEqual(events[27].type, 'message')
        self.assertEqual(events[27].mode, 'active')
        self.assertEqual(events[27].timestamp, 1627356924722)
        self.assertIsInstance(events[27].source, SourceUser)
        self.assertEqual(events[27].source.type, 'user')
        self.assertEqual(events[27].source.user_id, 'U206d25c2ea6bd87c17655609a1c37cb8')
        self.assertEqual(events[27].webhook_event_id, 'testwebhookeventid')
        self.assertIsInstance(events[27].delivery_context, DeliveryContext)
        self.assertFalse(events[27].delivery_context.is_redelivery)
        self.assertIsInstance(events[27].message, ImageMessage)
        self.assertEqual(events[27].message.id, '354718705033693861')
        self.assertEqual(events[27].message.type, 'image')
        self.assertEqual(events[27].message.content_provider.type, 'line')
        self.assertEqual(events[27].message.image_set.id, 'E005D41A7288F41B655')
        self.assertEqual(events[27].message.image_set.index, 2)
        self.assertEqual(events[27].message.image_set.total, 2)

        # MessageEvent, SourceUser, TextMessage (Redeliveried)
        self.assertIsInstance(events[28], MessageEvent)
        self.assertEqual(events[28].reply_token, 'nHuyWiB7yP5Zw52FIkcQobQuGDXCTA')
        self.assertEqual(events[28].type, 'message')
        self.assertEqual(events[28].mode, 'active')
        self.assertEqual(events[28].timestamp, 1462629479859)
        self.assertIsInstance(events[28].source, SourceUser)
        self.assertEqual(events[28].source.type, 'user')
        self.assertEqual(events[28].source.user_id, 'U206d25c2ea6bd87c17655609a1c37cb8')
        self.assertEqual(events[28].webhook_event_id, 'testwebhookeventid')
        self.assertIsInstance(events[28].delivery_context, DeliveryContext)
        self.assertTrue(events[28].delivery_context.is_redelivery)
        self.assertIsInstance(events[28].message, TextMessage)
        self.assertEqual(events[28].message.id, '325708')
        self.assertEqual(events[28].message.type, 'text')
        self.assertEqual(events[28].message.text, 'Hello, world')

    def test_parse_webhook_req_without_destination(self):
        body = """
        {
            "events": [
                {
                    "replyToken": "00000000000000000000000000000000",
                    "type": "message",
                    "timestamp": 1561099010135,
                    "source": {
                        "type": "user",
                        "userId": "Udeadbeefdeadbeefdeadbeefdeadbeef"
                    },
                    "message": {
                        "id": "100001",
                        "type": "text",
                        "text": "Hello, world"
                    }
                },
                {
                    "replyToken": "ffffffffffffffffffffffffffffffff",
                    "type": "message",
                    "timestamp": 1561099010135,
                    "source": {
                        "type": "user",
                        "userId": "Udeadbeefdeadbeefdeadbeefdeadbeef"
                    },
                    "message": {
                        "id": "100002",
                        "type": "sticker",
                        "packageId": "1",
                        "stickerId": "1"
                    }
                }
            ]
        }
        """
        payload = self.parser.parse(body=body, signature='channel_secret', as_payload=True)
        self.assertEqual(None, payload.destination)


class TestWebhookHandler(unittest.TestCase):
    def setUp(self):
        self.handler = WebhookHandler('channel_secret')

        @self.handler.add(MessageEvent, message=TextMessage)
        def message_text(event, destination):
            self.assertEqual('message', event.type)
            self.assertEqual('text', event.message.type)
            self.assertEqual('U123', destination)

        @self.handler.add(MessageEvent,
                          message=(ImageMessage, VideoMessage, AudioMessage))
        def message_content(event):
            self.assertEqual('message', event.type)
            self.assertIn(
                event.message.type,
                ['image', 'video', 'audio']
            )

        @self.handler.add(MessageEvent, message=StickerMessage)
        def message_sticker(event):
            self.assertEqual('message', event.type)
            self.assertEqual('sticker', event.message.type)

        @self.handler.add(MessageEvent)
        def message(event):
            self.assertEqual('message', event.type)
            self.assertNotIn(
                event.message.type,
                ['text', 'image', 'video', 'audio', 'sticker']
            )

        @self.handler.add(FollowEvent)
        def follow(event, destination):
            self.assertEqual('follow', event.type)
            self.assertEqual('U123', destination)

        @self.handler.add(JoinEvent)
        def join(event):
            self.assertEqual('join', event.type)

        @self.handler.add(PostbackEvent)
        def postback(event):
            self.assertEqual('postback', event.type)

        @self.handler.add(BeaconEvent)
        def beacon(event):
            self.assertEqual('beacon', event.type)

        @self.handler.add(AccountLinkEvent)
        def account_link(event):
            self.assertEqual('accountLink', event.type)

        @self.handler.default()
        def default(event):
            self.assertNotIn(
                event.type,
                ['message', 'follow', 'join', 'postback', 'beacon', 'accountLink']
            )

    def test_handler(self):
        file_dir = os.path.dirname(__file__)
        webhook_sample_json_path = os.path.join(file_dir, 'text', 'webhook.json')
        with open(webhook_sample_json_path) as fp:
            body = fp.read()

        # mock
        self.handler.parser.signature_validator.validate = lambda a, b: True

        self.handler.handle(body, 'signature')


class TestInvokeWebhookHandler(unittest.TestCase):
    def setUp(self):
        def wrap(func):
            def wrapper(*args):
                if PY3:
                    arg_spec = inspect.getfullargspec(func)
                else:
                    arg_spec = inspect.getargspec(func)
                return func(*args[0:len(arg_spec.args)])

            return wrapper

        def func_with_0_args():
            assert True

        def func_with_1_arg(arg):
            assert arg

        def func_with_2_args(arg1, arg2):
            assert arg1 and arg2

        def func_with_1_arg_with_default(arg=False):
            assert arg

        def func_with_2_args_with_default(arg1=False, arg2=False):
            assert arg1 and arg2

        def func_with_1_arg_and_1_arg_with_default(arg1, arg2=False):
            assert arg1 and arg2

        @wrap
        def wrapped_func_with_0_args():
            assert True

        @wrap
        def wrapped_func_with_1_arg(arg):
            assert arg

        @wrap
        def wrapped_func_with_2_args(arg1, arg2):
            assert arg1 and arg2

        @wrap
        def wrapped_func_with_1_arg_with_default(arg=False):
            assert arg

        @wrap
        def wrapped_func_with_2_args_with_default(arg1=False, arg2=False):
            assert arg1 and arg2

        @wrap
        def wrapped_func_with_1_arg_and_1_arg_with_default(
                arg1, arg2=False):
            assert arg1 and arg2

        self.functions = [
            func_with_0_args,
            func_with_1_arg,
            func_with_2_args,
            func_with_1_arg_with_default,
            func_with_2_args_with_default,
            func_with_1_arg_and_1_arg_with_default,
            wrapped_func_with_0_args,
            wrapped_func_with_1_arg,
            wrapped_func_with_2_args,
            wrapped_func_with_1_arg_with_default,
            wrapped_func_with_2_args_with_default,
            wrapped_func_with_1_arg_and_1_arg_with_default,
        ]

    def test_invoke_func(self):
        class PayloadMock(object):
            def __init__(self):
                self.destination = True

        event = True
        payload = PayloadMock()

        for func in self.functions:
            WebhookHandler._WebhookHandler__invoke_func(
                func, event, payload
            )


if __name__ == '__main__':
    unittest.main()
