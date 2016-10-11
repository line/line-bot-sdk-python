# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

import json
import responses
import unittest

from line_bot import (
    LineBotApi, TextSendMessage
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
            body='{}', status=200
        )

        self.tested.push_message('to', self.text_message)

        request = responses.calls[0].request
        self.assertEqual(request.method, 'POST')
        self.assertEqual(
            request.url,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/message/push'
        )
        self.assertEqual(
            json.loads(request.body.decode("utf-8")),
            {
                "to": "to",
                "messages": self.message
            }
        )

    @responses.activate
    def test_reply_text_message(self):
        responses.add(
            responses.POST,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/message/reply',
            body='{}', status=200
        )

        self.tested.reply_message('replyToken', self.text_message)

        request = responses.calls[0].request
        self.assertEqual(
            request.url,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/message/reply'
        )
        self.assertEqual(request.method, 'POST')
        self.assertEqual(
            json.loads(request.body.decode("utf-8")),
            {
                "replyToken": "replyToken",
                "messages": self.message
            }
        )
