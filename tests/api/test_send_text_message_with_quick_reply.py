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

import json
import unittest

import responses

from linebot import (
    LineBotApi
)
from linebot.models import (
    TextSendMessage, QuickReply, QuickReplyButton,
    PostbackAction, MessageAction, DatetimePickerAction,
    CameraAction, CameraRollAction, LocationAction
)


class TestLineBotApi(unittest.TestCase):
    def setUp(self):
        self.tested = LineBotApi('channel_secret')

        # test data
        self.text_message = TextSendMessage(text='Hello, world')
        self.message = [{"type": "text", "text": "Hello, world"}]

    @responses.activate
    def test_push_text_message_with_quick_reply(self):
        responses.add(
            responses.POST,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/message/push',
            json={}, status=200
        )

        self.tested.push_message('to',
                                 TextSendMessage(
                                     text='Hello, world',
                                     quick_reply=QuickReply(items=[
                                         QuickReplyButton(
                                             image_url='https://example.com',
                                             action=PostbackAction(label="label1", data="data1")
                                         ),
                                         QuickReplyButton(
                                             action=MessageAction(label="label2", text="text2")
                                         ),
                                         QuickReplyButton(
                                             action=DatetimePickerAction(label="label3",
                                                                         data="data3",
                                                                         mode="date")
                                         ),
                                         QuickReplyButton(
                                             action=CameraAction(label="label4")
                                         ),
                                         QuickReplyButton(
                                             action=CameraRollAction(label="label5")
                                         ),
                                         QuickReplyButton(
                                             action=LocationAction(label="label6")
                                         ),
                                     ])))

        request = responses.calls[0].request
        self.assertEqual(request.method, 'POST')
        self.assertEqual(
            request.url,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/message/push')
        self.assertEqual(
            json.loads(request.body),
            {
                "to": "to",
                'notificationDisabled': False,
                "messages": [
                    {
                        "type": "text",
                        "text": "Hello, world",
                        "quickReply": {
                            "items": [
                                {
                                    "type": "action",
                                    "imageUrl": "https://example.com",
                                    "action": {
                                        "type": "postback",
                                        "label": "label1",
                                        "data": "data1",
                                    }
                                },
                                {
                                    "type": "action",
                                    "action": {
                                        "type": "message",
                                        "label": "label2",
                                        "text": "text2",
                                    }
                                },
                                {
                                    "type": "action",
                                    "action": {
                                        "type": "datetimepicker",
                                        "label": "label3",
                                        "data": "data3",
                                        "mode": "date",
                                    }
                                },
                                {
                                    "type": "action",
                                    "action": {
                                        "type": "camera",
                                        "label": "label4",
                                    }
                                },
                                {
                                    "type": "action",
                                    "action": {
                                        "type": "cameraRoll",
                                        "label": "label5",
                                    }
                                },
                                {
                                    "type": "action",
                                    "action": {
                                        "type": "location",
                                        "label": "label6",
                                    }
                                },
                            ]
                        }
                    }
                ]
            }
        )


if __name__ == '__main__':
    unittest.main()
