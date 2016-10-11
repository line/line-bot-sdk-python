# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

import json
import unittest

import responses

from line_bot import (
    LineBotApi
)
from line_bot.models import (
    AudioSendMessage
)


class TestLineBotApi(unittest.TestCase):
    def setUp(self):
        self.tested = LineBotApi('channel_secret')

        self.audio_message = AudioSendMessage(
            original_content_url='https://example.com/original.m4a',
            duration=240000
        )

        self.message = [{
            "type": "audio",
            "originalContentUrl": "https://example.com/original.m4a",
            "duration": 240000,
        }]

    @responses.activate
    def test_push_audio_message(self):
        responses.add(
            responses.POST,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/message/push',
            body='{}', status=200
        )

        self.tested.push_message('to', self.audio_message)

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
    def test_reply_audio_message(self):
        responses.add(
            responses.POST,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/message/reply',
            body='{}', status=200
        )

        self.tested.reply_message('replyToken', self.audio_message)

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
