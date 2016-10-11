# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

import json
import responses
import unittest

from line_bot import (
    LineBotApi, ImageSendMessage
)


class TestLineBotApi(unittest.TestCase):
    def setUp(self):
        self.tested = LineBotApi('channel_secret')

        self.image_message = ImageSendMessage(
            original_content_url='https://example.com/original.jpg',
            preview_image_url='https://example.com/preview.jpg'
        )

        self.message = [{
            "type": "image",
            "originalContentUrl": "https://example.com/original.jpg",
            "previewImageUrl": "https://example.com/preview.jpg",
        }]

    @responses.activate
    def test_push_image_message(self):
        responses.add(
            responses.POST,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/message/push',
            body='{}', status=200
        )

        self.tested.push_message('to', self.image_message)

        request = responses.calls[0].request
        self.assertEqual(
            request.url,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/message/push'
        )
        self.assertEqual(request.method, 'POST')
        self.assertEqual(
            json.loads(request.body.decode("utf-8")),
            {
                "to": "to",
                "messages": self.message
            }
        )

    @responses.activate
    def test_reply_image_message(self):
        responses.add(
            responses.POST,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/message/reply',
            body='{}', status=200
        )

        self.tested.reply_message('replyToken', self.image_message)

        request = responses.calls[0].request
        self.assertEqual(request.method, 'POST')
        self.assertEqual(
            request.url,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/message/reply'
        )
        self.assertEqual(
            json.loads(request.body.decode("utf-8")),
            {
                "replyToken": "replyToken",
                "messages": self.message
            }
        )
