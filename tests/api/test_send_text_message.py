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
    TextSendMessage
)


class TestSendTestMessage(unittest.TestCase):
    def setUp(self):
        self.tested = LineBotApi('channel_secret')
        # test data
        self.text_message = TextSendMessage(text='Hello, world')
        self.message = [{"type": "text", "text": "Hello, world"}]

    @responses.activate
    def test_push_text_message(self):
        responses.add(
            responses.POST,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/message/push',
            json={}, status=200
        )

        self.tested.push_message('to', self.text_message)

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
                "messages": self.message
            }
        )

    @responses.activate
    def test_push_text_message_with_retry_key(self):
        responses.add(
            responses.POST,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/message/push',
            json={}, status=200,
            headers={'X-Line-Retry-Key': '123e4567-e89b-12d3-a456-426614174000'}
        )

        self.tested.push_message(
            'to',
            self.text_message,
            retry_key='123e4567-e89b-12d3-a456-426614174000'
        )

        request = responses.calls[0].request

        self.assertEqual(request.method, 'POST')
        self.assertEqual(
            request.url,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/message/push')
        self.assertEqual(
            request.headers['X-Line-Retry-Key'],
            '123e4567-e89b-12d3-a456-426614174000'
        )
        self.assertEqual(
            json.loads(request.body),
            {
                "to": "to",
                'notificationDisabled': False,
                "messages": self.message
            }
        )

    @responses.activate
    def test_reply_text_message(self):
        responses.add(
            responses.POST,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/message/reply',
            json={}, status=200
        )

        self.tested.reply_message('replyToken', self.text_message)

        request = responses.calls[0].request
        self.assertEqual(
            request.url,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/message/reply')
        self.assertEqual(request.method, 'POST')
        self.assertEqual(
            json.loads(request.body),
            {
                "replyToken": "replyToken",
                'notificationDisabled': False,
                "messages": self.message
            }
        )

    @responses.activate
    def test_multicast_text_message(self):
        responses.add(
            responses.POST,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/message/multicast',
            json={}, status=200
        )

        self.tested.multicast(['to1', 'to2'], self.text_message)

        request = responses.calls[0].request
        self.assertEqual(
            request.url,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/message/multicast')
        self.assertEqual(request.method, 'POST')
        self.assertEqual(
            json.loads(request.body),
            {
                "to": ['to1', 'to2'],
                'notificationDisabled': False,
                "messages": self.message
            }
        )

    @responses.activate
    def test_multicast_text_message_with_retry_key(self):
        responses.add(
            responses.POST,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/message/multicast',
            json={}, status=200,
            headers={'X-Line-Retry-Key': '123e4567-e89b-12d3-a456-426614174000'}

        )

        self.tested.multicast(
            ['to1', 'to2'],
            self.text_message,
            retry_key='123e4567-e89b-12d3-a456-426614174000'
        )

        request = responses.calls[0].request
        self.assertEqual(
            request.url,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/message/multicast')
        self.assertEqual(request.method, 'POST')
        self.assertEqual(
            request.headers['X-Line-Retry-Key'],
            '123e4567-e89b-12d3-a456-426614174000'
        )
        self.assertEqual(
            json.loads(request.body),
            {
                "to": ['to1', 'to2'],
                'notificationDisabled': False,
                "messages": self.message
            }
        )

    @responses.activate
    def test_broadcast_text_message(self):
        responses.add(
            responses.POST,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/message/broadcast',
            json={}, status=200, headers={'X-Line-Request-Id': 'request_id_test'}
        )

        response = self.tested.broadcast(self.text_message)

        request = responses.calls[0].request
        self.assertEqual(
            request.url,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/message/broadcast')
        self.assertEqual(request.method, 'POST')
        self.assertEqual(
            json.loads(request.body),
            {
                'notificationDisabled': False,
                "messages": self.message
            }
        )
        self.assertEqual('request_id_test', response.request_id)

        # call with notification_disable=True
        response = self.tested.broadcast(self.text_message, notification_disabled=True)

        request = responses.calls[1].request
        self.assertEqual(
            request.url,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/message/broadcast')
        self.assertEqual(request.method, 'POST')
        self.assertEqual(
            json.loads(request.body),
            {
                'notificationDisabled': True,
                "messages": self.message
            }
        )
        self.assertEqual('request_id_test', response.request_id)

    @responses.activate
    def test_broadcast_text_message_with_retry_key(self):
        responses.add(
            responses.POST,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/message/broadcast',
            json={}, status=200,
            headers={
                'X-Line-Request-Id': 'request_id_test',
                'X-Line-Retry-Key': '123e4567-e89b-12d3-a456-426614174000'
            }
        )

        response = self.tested.broadcast(
            self.text_message,
            retry_key='123e4567-e89b-12d3-a456-426614174000'
        )

        request = responses.calls[0].request
        self.assertEqual(
            request.url,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/message/broadcast')
        self.assertEqual(request.method, 'POST')
        self.assertEqual(
            request.headers['X-Line-Retry-Key'],
            '123e4567-e89b-12d3-a456-426614174000'
        )
        self.assertEqual(
            json.loads(request.body),
            {
                'notificationDisabled': False,
                "messages": self.message
            }
        )
        self.assertEqual('request_id_test', response.request_id)


if __name__ == '__main__':
    unittest.main()
