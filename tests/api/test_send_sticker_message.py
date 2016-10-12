# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

import json
import responses
import unittest

from linebot import (
    LineBotApi
)
from linebot.models import (
    StickerSendMessage
)


class TestLineBotApi(unittest.TestCase):
    def setUp(self):
        self.tested = LineBotApi('channel_secret')

        self.sticker_message = StickerSendMessage(
            package_id='1', sticker_id='1'
        )

        self.message = [{
            "type": "sticker",
            "packageId": "1",
            "stickerId": "1"
        }]

    @responses.activate
    def test_push_sticker_message(self):
        responses.add(
            responses.POST,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/message/push',
            json={}, status=200
        )

        self.tested.push_message('to', self.sticker_message)

        request = responses.calls[0].request
        self.assertEqual(request.method, 'POST')
        self.assertEqual(
            request.url,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/message/push'
        )
        self.assertEqual(
            json.loads(request.body),
            {
                "to": "to",
                "messages": self.message
            }
        )

    @responses.activate
    def test_reply_sticker_message(self):
        responses.add(
            responses.POST,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/message/reply',
            json={}, status=200
        )

        self.tested.reply_message('replyToken', self.sticker_message)

        request = responses.calls[0].request
        self.assertEqual(request.method, 'POST')
        self.assertEqual(
            request.url,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/message/reply'
        )
        self.assertEqual(
            json.loads(request.body),
            {
                "replyToken": "replyToken",
                "messages": self.message
            }
        )
