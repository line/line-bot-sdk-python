# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

import json
import responses
import unittest

from line_bot import (
    LineBotApi, ImagemapSendMessage, BaseSize, URIImagemapAction,
    ImagemapArea, MessageImagemapAction
)


class TestLineBotApi(unittest.TestCase):
    def setUp(self):
        self.tested = LineBotApi('channel_secret')

        self.imagemap_message = ImagemapSendMessage(
            base_url='https://example.com/base',
            alt_text='this is an imagemap',
            base_size=BaseSize(height=1040, width=1040),
            actions=[
                URIImagemapAction(
                    link_uri='https://example.com/',
                    area=ImagemapArea(
                        x=0, y=0, width=520, height=1040
                    )
                ),
                MessageImagemapAction(
                    text='hello',
                    area=ImagemapArea(
                        x=520, y=0, width=520, height=1040
                    )
                )
            ]
        )

        self.message = [{
            "type": "imagemap",
            "baseUrl": "https://example.com/base",
            "altText": "this is an imagemap",
            "baseSize": {
                "height": 1040,
                "width": 1040
            },
            "actions": [
                {
                    "type": "uri",
                    "linkUri": "https://example.com/",
                    "area": {
                        "x": 0,
                        "y": 0,
                        "width": 520,
                        "height": 1040
                    }
                },
                {
                    "type": "message",
                    "text": "hello",
                    "area": {
                        "x": 520,
                        "y": 0,
                        "width": 520,
                        "height": 1040
                    }
                }
            ]
        }]

    @responses.activate
    def test_push_imagemap_message(self):
        responses.add(
            responses.POST,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/message/push',
            body='{}', status=200
        )

        self.tested.push_message('to', self.imagemap_message)

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
    def test_reply_imagemap_message(self):
        responses.add(
            responses.POST,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/message/reply',
            body='{}', status=200
        )

        self.tested.reply_message('replyToken', self.imagemap_message)

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
