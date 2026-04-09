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

"""Tests for LineBotClient.

Verifies that LineBotClient correctly delegates to each underlying API client
and sends proper HTTP requests. Uses pytest_httpserver for HTTP mocking.

Reference: line-bot-sdk-nodejs/test/line-bot-client.spec.ts
"""

import json
import unittest

from pytest_httpserver import HTTPServer

from linebot.v3 import LineBotClient
from linebot.v3.messaging import (
    PushMessageRequest,
    ReplyMessageRequest,
    TextMessage,
)
from linebot.v3.messaging.exceptions import ApiException as MessagingApiException
from linebot.v3.shop.models import MissionStickerRequest


class TestLineBotClientInit(unittest.TestCase):
    """Test initialization and context manager."""

    def test_init(self):
        client = LineBotClient(channel_access_token="test-token")
        self.assertIsNotNone(client._manage_audience)
        self.assertIsNotNone(client._manage_audience_blob)
        self.assertIsNotNone(client._insight)
        self.assertIsNotNone(client._liff)
        self.assertIsNotNone(client._messaging_api)
        self.assertIsNotNone(client._messaging_api_blob)
        self.assertIsNotNone(client._line_module)
        self.assertIsNotNone(client._line_module_attach)
        self.assertIsNotNone(client._shop)
        client.close()

    def test_context_manager(self):
        with LineBotClient(channel_access_token="test-token") as client:
            self.assertIsNotNone(client)


class TestLineBotClientMessagingApi(unittest.TestCase):
    """Test MessagingApi delegation through LineBotClient."""

    def test_push_message(self):
        with HTTPServer() as httpserver:
            httpserver.expect_request(
                uri="/v2/bot/message/push",
                method="POST",
            ).respond_with_json(
                {"sentMessages": [{"id": "msg001", "quoteToken": "qt001"}]},
                status=200
            )

            with LineBotClient(
                channel_access_token="test-token",
                host=httpserver.url_for("/")
            ) as client:
                req = PushMessageRequest(
                    to="U123",
                    messages=[TextMessage(text="hello")]
                )
                client.push_message(push_message_request=req)

            self.assertEqual(len(httpserver.log), 1)
            request, _ = httpserver.log[0]
            self.assertEqual(request.method, "POST")
            self.assertEqual(request.path, "/v2/bot/message/push")
            body = json.loads(request.data.decode("utf-8"))
            self.assertEqual(body["to"], "U123")
            self.assertEqual(body["messages"][0]["type"], "text")
            self.assertEqual(body["messages"][0]["text"], "hello")

    def test_reply_message(self):
        with HTTPServer() as httpserver:
            httpserver.expect_request(
                uri="/v2/bot/message/reply",
                method="POST",
            ).respond_with_json(
                {"sentMessages": [{"id": "msg002", "quoteToken": "qt002"}]},
                status=200
            )

            with LineBotClient(
                channel_access_token="test-token",
                host=httpserver.url_for("/")
            ) as client:
                req = ReplyMessageRequest(
                    replyToken="reply-token-xxx",
                    messages=[TextMessage(text="hi")]
                )
                client.reply_message(reply_message_request=req)

            self.assertEqual(len(httpserver.log), 1)
            request, _ = httpserver.log[0]
            self.assertEqual(request.method, "POST")
            body = json.loads(request.data.decode("utf-8"))
            self.assertEqual(body["replyToken"], "reply-token-xxx")
            self.assertEqual(body["messages"][0]["text"], "hi")

    def test_get_followers_with_query_params(self):
        expected_response = {
            "userIds": ["U4af4980629", "U0c229f96c4"],
            "next": "yANU9IA..."
        }
        with HTTPServer() as httpserver:
            httpserver.expect_request(
                uri="/v2/bot/followers/ids",
                method="GET",
            ).respond_with_json(expected_response, status=200)

            with LineBotClient(
                channel_access_token="test-token",
                host=httpserver.url_for("/")
            ) as client:
                response = client.get_followers(start="xBQU2IB", limit=100)

            self.assertEqual(response.user_ids, expected_response["userIds"])
            self.assertEqual(response.next, expected_response["next"])
            self.assertEqual(len(httpserver.log), 1)
            request, _ = httpserver.log[0]
            self.assertEqual(request.method, "GET")
            self.assertIn(b"start=xBQU2IB", request.query_string)
            self.assertIn(b"limit=100", request.query_string)

    def test_get_followers_without_start(self):
        expected_response = {"userIds": ["U4af4980629"]}
        with HTTPServer() as httpserver:
            httpserver.expect_request(
                uri="/v2/bot/followers/ids",
                method="GET",
            ).respond_with_json(expected_response, status=200)

            with LineBotClient(
                channel_access_token="test-token",
                host=httpserver.url_for("/")
            ) as client:
                response = client.get_followers()

            self.assertEqual(response.user_ids, ["U4af4980629"])
            request, _ = httpserver.log[0]
            self.assertEqual(request.query_string, b"")

    def test_get_profile(self):
        expected_response = {
            "displayName": "Test User",
            "userId": "U4af4980629",
            "pictureUrl": "https://example.com/pic.png",
            "statusMessage": "Hello"
        }
        with HTTPServer() as httpserver:
            httpserver.expect_request(
                uri="/v2/bot/profile/U4af4980629",
                method="GET",
            ).respond_with_json(expected_response, status=200)

            with LineBotClient(
                channel_access_token="test-token",
                host=httpserver.url_for("/")
            ) as client:
                response = client.get_profile(user_id="U4af4980629")

            self.assertEqual(response.display_name, "Test User")
            self.assertEqual(response.user_id, "U4af4980629")
            self.assertEqual(len(httpserver.log), 1)
            request, _ = httpserver.log[0]
            self.assertEqual(request.method, "GET")
            self.assertEqual(request.path, "/v2/bot/profile/U4af4980629")


class TestLineBotClientInsight(unittest.TestCase):
    """Test Insight API delegation through LineBotClient."""

    def test_get_number_of_followers(self):
        expected_response = {
            "status": "ready",
            "followers": 123,
            "targetedReaches": 100,
            "blocks": 5
        }
        with HTTPServer() as httpserver:
            httpserver.expect_request(
                uri="/v2/bot/insight/followers",
                method="GET",
            ).respond_with_json(expected_response, status=200)

            with LineBotClient(
                channel_access_token="test-token",
                host=httpserver.url_for("/")
            ) as client:
                response = client.get_number_of_followers(var_date="20240101")

            self.assertEqual(response.followers, 123)
            self.assertEqual(response.targeted_reaches, 100)
            self.assertEqual(response.blocks, 5)
            self.assertEqual(len(httpserver.log), 1)
            request, _ = httpserver.log[0]
            self.assertIn(b"date=20240101", request.query_string)


class TestLineBotClientLiff(unittest.TestCase):
    """Test LIFF API delegation through LineBotClient."""

    def test_get_all_liff_apps(self):
        expected_response = {"apps": []}
        with HTTPServer() as httpserver:
            httpserver.expect_request(
                uri="/liff/v1/apps",
                method="GET",
            ).respond_with_json(expected_response, status=200)

            with LineBotClient(
                channel_access_token="test-token",
                host=httpserver.url_for("/")
            ) as client:
                response = client.get_all_liff_apps()

            self.assertEqual(response.apps, [])
            self.assertEqual(len(httpserver.log), 1)
            request, _ = httpserver.log[0]
            self.assertEqual(request.method, "GET")
            self.assertEqual(request.path, "/liff/v1/apps")


class TestLineBotClientAudience(unittest.TestCase):
    """Test ManageAudience API delegation through LineBotClient."""

    def test_delete_audience_group(self):
        with HTTPServer() as httpserver:
            httpserver.expect_request(
                uri="/v2/bot/audienceGroup/12345",
                method="DELETE",
            ).respond_with_json({}, status=200)

            with LineBotClient(
                channel_access_token="test-token",
                host=httpserver.url_for("/")
            ) as client:
                client.delete_audience_group(audience_group_id=12345)

            self.assertEqual(len(httpserver.log), 1)
            request, _ = httpserver.log[0]
            self.assertEqual(request.method, "DELETE")
            self.assertEqual(request.path, "/v2/bot/audienceGroup/12345")


class TestLineBotClientModule(unittest.TestCase):
    """Test LineModule API delegation through LineBotClient."""

    def test_get_modules_with_query_params(self):
        expected_response = {
            "bots": [{"userId": "U111", "basicId": "@bot", "displayName": "TestBot"}],
            "next": "next-token"
        }
        with HTTPServer() as httpserver:
            httpserver.expect_request(
                uri="/v2/bot/list",
                method="GET",
            ).respond_with_json(expected_response, status=200)

            with LineBotClient(
                channel_access_token="test-token",
                host=httpserver.url_for("/")
            ) as client:
                client.get_modules(start="start-token", limit=20)

            self.assertEqual(len(httpserver.log), 1)
            request, _ = httpserver.log[0]
            self.assertEqual(request.method, "GET")
            self.assertIn(b"start=start-token", request.query_string)
            self.assertIn(b"limit=20", request.query_string)

    def test_get_modules_without_start(self):
        expected_response = {"bots": []}
        with HTTPServer() as httpserver:
            httpserver.expect_request(
                uri="/v2/bot/list",
                method="GET",
            ).respond_with_json(expected_response, status=200)

            with LineBotClient(
                channel_access_token="test-token",
                host=httpserver.url_for("/")
            ) as client:
                client.get_modules()

            self.assertEqual(len(httpserver.log), 1)
            request, _ = httpserver.log[0]
            self.assertNotIn(b"start=", request.query_string)


class TestLineBotClientModuleAttach(unittest.TestCase):
    """Test LineModuleAttach API delegation through LineBotClient."""

    def test_attach_module(self):
        expected_response = {
            "bot_id": "U1234567890",
            "scopes": ["message:send"]
        }
        with HTTPServer() as httpserver:
            httpserver.expect_request(
                uri="/module/auth/v1/token",
                method="POST",
            ).respond_with_json(expected_response, status=200)

            with LineBotClient(
                channel_access_token="test-token",
                host=httpserver.url_for("/")
            ) as client:
                response = client.attach_module(
                    grant_type="authorization_code",
                    code="auth_code",
                    redirect_uri="https://example.com/callback"
                )

            self.assertEqual(response.bot_id, "U1234567890")
            self.assertEqual(response.scopes, ["message:send"])
            self.assertEqual(len(httpserver.log), 1)
            request, _ = httpserver.log[0]
            self.assertEqual(request.method, "POST")
            self.assertEqual(request.path, "/module/auth/v1/token")


class TestLineBotClientShop(unittest.TestCase):
    """Test Shop API delegation through LineBotClient."""

    def test_mission_sticker_v3(self):
        with HTTPServer() as httpserver:
            httpserver.expect_request(
                uri="/shop/v3/mission",
                method="POST",
            ).respond_with_json({}, status=200)

            with LineBotClient(
                channel_access_token="test-token",
                host=httpserver.url_for("/")
            ) as client:
                req = MissionStickerRequest(
                    to="U4af4980629",
                    productId="prod_id",
                    productType="prod_type",
                    sendPresentMessage=False
                )
                client.mission_sticker_v3(mission_sticker_request=req)

            self.assertEqual(len(httpserver.log), 1)
            request, _ = httpserver.log[0]
            self.assertEqual(request.method, "POST")
            self.assertEqual(request.path, "/shop/v3/mission")
            body = json.loads(request.data.decode("utf-8"))
            self.assertEqual(body["to"], "U4af4980629")
            self.assertEqual(body["productId"], "prod_id")
            self.assertEqual(body["productType"], "prod_type")
            self.assertEqual(body["sendPresentMessage"], False)


class TestLineBotClientErrors(unittest.TestCase):
    """Test error handling through LineBotClient."""

    def test_api_error_from_messaging(self):
        with HTTPServer() as httpserver:
            httpserver.expect_request(
                uri="/v2/bot/message/push",
                method="POST",
            ).respond_with_json(
                {"message": "Invalid request"},
                status=400
            )

            with LineBotClient(
                channel_access_token="test-token",
                host=httpserver.url_for("/")
            ) as client:
                req = PushMessageRequest(
                    to="U123",
                    messages=[TextMessage(text="hello")]
                )
                with self.assertRaises(MessagingApiException) as ctx:
                    client.push_message(push_message_request=req)

                self.assertEqual(ctx.exception.status, 400)


if __name__ == '__main__':
    unittest.main()
