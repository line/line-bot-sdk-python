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

import unittest

from linebot.v3 import (
    WebhookParser, WebhookHandler
)
from linebot.v3.exceptions import InvalidSignatureError

class TestWebhookParserWithSkipSignatureVerification(unittest.TestCase):
    def setUp(self):
        self.parser = WebhookParser('channel_secret')
        self.parser_with_skip = WebhookParser('channel_secret', skip_signature_verification=lambda: True)

    def test_parse_with_invalid_signature(self):
        body = '{"events": []}'
        signature = 'invalid_signature'

        # Should raise InvalidSignatureError when skip_signature_verification is False (default)
        with self.assertRaises(InvalidSignatureError):
            self.parser.parse(body, signature)

        # Should not raise InvalidSignatureError when skip_signature_verification is True
        try:
            self.parser_with_skip.parse(body, signature)
        except InvalidSignatureError:
            self.fail("parse() raised InvalidSignatureError unexpectedly!")

class TestWebhookHandlerWithSkipSignatureVerification(unittest.TestCase):
    def setUp(self):
        self.handler = WebhookHandler('channel_secret')
        self.handler_with_skip = WebhookHandler('channel_secret', skip_signature_verification=lambda: True)
        self.handler_called = False
        self.handler_with_skip_called = False

        @self.handler.default()
        def default(event):
            self.handler_called = True

        @self.handler_with_skip.default()
        def default_with_skip(event):
            self.handler_with_skip_called = True

    def test_handle_with_invalid_signature(self):
        body = '{"events": [{"type": "message", "message": {"type": "text", "id": "123", "text": "test"}, "timestamp": 1462629479859, "source": {"type": "user", "userId": "U123"}, "replyToken": "reply_token", "mode": "active", "webhookEventId": "test_id", "deliveryContext": {"isRedelivery": false}}]}'
        signature = 'invalid_signature'

        # Should raise InvalidSignatureError when skip_signature_verification is False (default)
        with self.assertRaises(InvalidSignatureError):
            self.handler.handle(body, signature)

        # Handler should not be called when signature verification fails
        self.assertFalse(self.handler_called)

        # Should not raise InvalidSignatureError when skip_signature_verification is True
        try:
            self.handler_with_skip.handle(body, signature)
        except InvalidSignatureError:
            self.fail("handle() raised InvalidSignatureError unexpectedly!")

        # Handler should be called when signature verification is skipped
        self.assertTrue(self.handler_with_skip_called)

    def test_dynamic_skip_signature_verification(self):
        body = '{"events": [{"type": "message", "message": {"type": "text", "id": "123", "text": "test"}, "timestamp": 1462629479859, "source": {"type": "user", "userId": "U123"}, "replyToken": "reply_token", "mode": "active", "webhookEventId": "test_id", "deliveryContext": {"isRedelivery": false}}]}'
        signature = 'invalid_signature'
        skip_flag = [False]

        # Create a handler with dynamic skip flag
        handler_with_dynamic_skip = WebhookHandler(
            'channel_secret',
            skip_signature_verification=lambda: skip_flag[0]
        )

        dynamic_handler_called = [False]

        @handler_with_dynamic_skip.default()
        def default_dynamic(event):
            dynamic_handler_called[0] = True

        # Should raise InvalidSignatureError when skip_signature_verification returns False
        with self.assertRaises(InvalidSignatureError):
            handler_with_dynamic_skip.handle(body, signature)

        # Handler should not be called
        self.assertFalse(dynamic_handler_called[0])

        # Change the skip flag
        skip_flag[0] = True

        # Should not raise InvalidSignatureError now
        try:
            handler_with_dynamic_skip.handle(body, signature)
        except InvalidSignatureError:
            self.fail("handle() raised InvalidSignatureError unexpectedly!")

        # Handler should be called now
        self.assertTrue(dynamic_handler_called[0])

if __name__ == '__main__':
    unittest.main()

