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

"""Tests for AsyncLineBotClient.

Verifies that AsyncLineBotClient correctly delegates to each underlying
async API client and sends proper HTTP requests.
"""

import json
import unittest

from pytest_httpserver import HTTPServer

from linebot.v3 import AsyncLineBotClient
from linebot.v3.messaging import (
    PushMessageRequest,
    ReplyMessageRequest,
    TextMessage,
)
from linebot.v3.messaging.exceptions import ApiException as MessagingApiException
from linebot.v3.shop.models import MissionStickerRequest


class TestAsyncLineBotClientMessagingApi(unittest.IsolatedAsyncioTestCase):
    """Test MessagingApi delegation through AsyncLineBotClient."""

    async def test_push_message(self):
        with HTTPServer() as httpserver:
            httpserver.expect_request(
                uri="/v2/bot/message/push",
                method="POST",
            ).respond_with_json(
                {"sentMessages": [{"id": "msg001", "quoteToken": "qt001"}]},
                status=200
            )

            async with AsyncLineBotClient(
                channel_access_token="test-token",
                host=httpserver.url_for("/")
            ) as client:
                req = PushMessageRequest(
                    to="U123",
                    messages=[TextMessage(text="hello")]
                )
                await client.push_message(push_message_request=req)

            self.assertEqual(len(httpserver.log), 1)
            request, _ = httpserver.log[0]
            self.assertEqual(request.method, "POST")
            self.assertEqual(request.path, "/v2/bot/message/push")
            body = json.loads(request.data.decode("utf-8"))
            self.assertEqual(body["to"], "U123")
            self.assertEqual(body["messages"][0]["type"], "text")
            self.assertEqual(body["messages"][0]["text"], "hello")

    async def test_reply_message(self):
        with HTTPServer() as httpserver:
            httpserver.expect_request(
                uri="/v2/bot/message/reply",
                method="POST",
            ).respond_with_json(
                {"sentMessages": [{"id": "msg002", "quoteToken": "qt002"}]},
                status=200
            )

            async with AsyncLineBotClient(
                channel_access_token="test-token",
                host=httpserver.url_for("/")
            ) as client:
                req = ReplyMessageRequest(
                    replyToken="reply-token-xxx",
                    messages=[TextMessage(text="hi")]
                )
                await client.reply_message(reply_message_request=req)

            self.assertEqual(len(httpserver.log), 1)
            request, _ = httpserver.log[0]
            self.assertEqual(request.method, "POST")
            body = json.loads(request.data.decode("utf-8"))
            self.assertEqual(body["replyToken"], "reply-token-xxx")
            self.assertEqual(body["messages"][0]["text"], "hi")

    async def test_get_followers_with_query_params(self):
        expected_response = {
            "userIds": ["U4af4980629", "U0c229f96c4"],
            "next": "yANU9IA..."
        }
        with HTTPServer() as httpserver:
            httpserver.expect_request(
                uri="/v2/bot/followers/ids",
                method="GET",
            ).respond_with_json(expected_response, status=200)

            async with AsyncLineBotClient(
                channel_access_token="test-token",
                host=httpserver.url_for("/")
            ) as client:
                response = await client.get_followers(start="xBQU2IB", limit=100)

            self.assertEqual(response.user_ids, expected_response["userIds"])
            self.assertEqual(response.next, expected_response["next"])
            self.assertEqual(len(httpserver.log), 1)
            request, _ = httpserver.log[0]
            self.assertEqual(request.method, "GET")
            self.assertIn(b"start=xBQU2IB", request.query_string)
            self.assertIn(b"limit=100", request.query_string)

    async def test_get_followers_without_start(self):
        expected_response = {"userIds": ["U4af4980629"]}
        with HTTPServer() as httpserver:
            httpserver.expect_request(
                uri="/v2/bot/followers/ids",
                method="GET",
            ).respond_with_json(expected_response, status=200)

            async with AsyncLineBotClient(
                channel_access_token="test-token",
                host=httpserver.url_for("/")
            ) as client:
                response = await client.get_followers()

            self.assertEqual(response.user_ids, ["U4af4980629"])
            request, _ = httpserver.log[0]
            self.assertEqual(request.query_string, b"")

    async def test_get_profile(self):
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

            async with AsyncLineBotClient(
                channel_access_token="test-token",
                host=httpserver.url_for("/")
            ) as client:
                response = await client.get_profile(user_id="U4af4980629")

            self.assertEqual(response.display_name, "Test User")
            self.assertEqual(response.user_id, "U4af4980629")
            self.assertEqual(len(httpserver.log), 1)
            request, _ = httpserver.log[0]
            self.assertEqual(request.method, "GET")
            self.assertEqual(request.path, "/v2/bot/profile/U4af4980629")


class TestAsyncLineBotClientInsight(unittest.IsolatedAsyncioTestCase):
    """Test Insight API delegation through AsyncLineBotClient."""

    async def test_get_number_of_followers(self):
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

            async with AsyncLineBotClient(
                channel_access_token="test-token",
                host=httpserver.url_for("/")
            ) as client:
                response = await client.get_number_of_followers(var_date="20240101")

            self.assertEqual(response.followers, 123)
            self.assertEqual(response.targeted_reaches, 100)
            self.assertEqual(response.blocks, 5)
            self.assertEqual(len(httpserver.log), 1)
            request, _ = httpserver.log[0]
            self.assertIn(b"date=20240101", request.query_string)


class TestAsyncLineBotClientLiff(unittest.IsolatedAsyncioTestCase):
    """Test LIFF API delegation through AsyncLineBotClient."""

    async def test_get_all_liff_apps(self):
        with HTTPServer() as httpserver:
            httpserver.expect_request(
                uri="/liff/v1/apps",
                method="GET",
            ).respond_with_json({"apps": []}, status=200)

            async with AsyncLineBotClient(
                channel_access_token="test-token",
                host=httpserver.url_for("/")
            ) as client:
                response = await client.get_all_liff_apps()

            self.assertEqual(response.apps, [])
            self.assertEqual(len(httpserver.log), 1)
            request, _ = httpserver.log[0]
            self.assertEqual(request.method, "GET")
            self.assertEqual(request.path, "/liff/v1/apps")


class TestAsyncLineBotClientAudience(unittest.IsolatedAsyncioTestCase):
    """Test ManageAudience API delegation through AsyncLineBotClient."""

    async def test_delete_audience_group(self):
        with HTTPServer() as httpserver:
            httpserver.expect_request(
                uri="/v2/bot/audienceGroup/12345",
                method="DELETE",
            ).respond_with_json({}, status=200)

            async with AsyncLineBotClient(
                channel_access_token="test-token",
                host=httpserver.url_for("/")
            ) as client:
                await client.delete_audience_group(audience_group_id=12345)

            self.assertEqual(len(httpserver.log), 1)
            request, _ = httpserver.log[0]
            self.assertEqual(request.method, "DELETE")
            self.assertEqual(request.path, "/v2/bot/audienceGroup/12345")


class TestAsyncLineBotClientModule(unittest.IsolatedAsyncioTestCase):
    """Test LineModule API delegation through AsyncLineBotClient."""

    async def test_get_modules(self):
        expected_response = {
            "bots": [{"userId": "U111", "basicId": "@bot", "displayName": "TestBot"}],
            "next": "next-token"
        }
        with HTTPServer() as httpserver:
            httpserver.expect_request(
                uri="/v2/bot/list",
                method="GET",
            ).respond_with_json(expected_response, status=200)

            async with AsyncLineBotClient(
                channel_access_token="test-token",
                host=httpserver.url_for("/")
            ) as client:
                await client.get_modules(start="start-token", limit=20)

            self.assertEqual(len(httpserver.log), 1)
            request, _ = httpserver.log[0]
            self.assertEqual(request.method, "GET")
            self.assertIn(b"start=start-token", request.query_string)
            self.assertIn(b"limit=20", request.query_string)


class TestAsyncLineBotClientModuleAttach(unittest.IsolatedAsyncioTestCase):
    """Test LineModuleAttach API delegation through AsyncLineBotClient."""

    async def test_attach_module(self):
        expected_response = {
            "bot_id": "U1234567890",
            "scopes": ["message:send"]
        }
        with HTTPServer() as httpserver:
            httpserver.expect_request(
                uri="/module/auth/v1/token",
                method="POST",
            ).respond_with_json(expected_response, status=200)

            async with AsyncLineBotClient(
                channel_access_token="test-token",
                host=httpserver.url_for("/")
            ) as client:
                response = await client.attach_module(
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


class TestAsyncLineBotClientShop(unittest.IsolatedAsyncioTestCase):
    """Test Shop API delegation through AsyncLineBotClient."""

    async def test_mission_sticker_v3(self):
        with HTTPServer() as httpserver:
            httpserver.expect_request(
                uri="/shop/v3/mission",
                method="POST",
            ).respond_with_json({}, status=200)

            async with AsyncLineBotClient(
                channel_access_token="test-token",
                host=httpserver.url_for("/")
            ) as client:
                req = MissionStickerRequest(
                    to="U4af4980629",
                    productId="prod_id",
                    productType="prod_type",
                    sendPresentMessage=False
                )
                await client.mission_sticker_v3(mission_sticker_request=req)

            self.assertEqual(len(httpserver.log), 1)
            request, _ = httpserver.log[0]
            self.assertEqual(request.method, "POST")
            self.assertEqual(request.path, "/shop/v3/mission")
            body = json.loads(request.data.decode("utf-8"))
            self.assertEqual(body["to"], "U4af4980629")
            self.assertEqual(body["productId"], "prod_id")
            self.assertEqual(body["productType"], "prod_type")
            self.assertEqual(body["sendPresentMessage"], False)


class TestAsyncLineBotClientAuthorizationHeader(unittest.IsolatedAsyncioTestCase):
    """Test that the Authorization header is correctly propagated to all domains."""

    def _assert_bearer_token(self, httpserver, expected_token):
        request, _ = httpserver.log[-1]
        self.assertEqual(
            request.headers.get("Authorization"), f"Bearer {expected_token}"
        )

    async def test_messaging_api_sends_bearer_token(self):
        with HTTPServer() as httpserver:
            httpserver.expect_request(
                uri="/v2/bot/profile/U123",
                method="GET",
            ).respond_with_json(
                {"displayName": "T", "userId": "U123"}, status=200
            )

            async with AsyncLineBotClient(
                channel_access_token="my-secret-token",
                host=httpserver.url_for("/")
            ) as client:
                await client.get_profile(user_id="U123")

            self._assert_bearer_token(httpserver, "my-secret-token")

    async def test_insight_api_sends_bearer_token(self):
        with HTTPServer() as httpserver:
            httpserver.expect_request(
                uri="/v2/bot/insight/followers",
                method="GET",
            ).respond_with_json(
                {"status": "ready", "followers": 0, "targetedReaches": 0, "blocks": 0},
                status=200
            )

            async with AsyncLineBotClient(
                channel_access_token="insight-token",
                host=httpserver.url_for("/")
            ) as client:
                await client.get_number_of_followers(var_date="20240101")

            self._assert_bearer_token(httpserver, "insight-token")

    async def test_audience_api_sends_bearer_token(self):
        with HTTPServer() as httpserver:
            httpserver.expect_request(
                uri="/v2/bot/audienceGroup/99999",
                method="DELETE",
            ).respond_with_json({}, status=200)

            async with AsyncLineBotClient(
                channel_access_token="audience-token",
                host=httpserver.url_for("/")
            ) as client:
                await client.delete_audience_group(audience_group_id=99999)

            self._assert_bearer_token(httpserver, "audience-token")

    async def test_liff_api_sends_bearer_token(self):
        with HTTPServer() as httpserver:
            httpserver.expect_request(
                uri="/liff/v1/apps",
                method="GET",
            ).respond_with_json({"apps": []}, status=200)

            async with AsyncLineBotClient(
                channel_access_token="liff-token",
                host=httpserver.url_for("/")
            ) as client:
                await client.get_all_liff_apps()

            self._assert_bearer_token(httpserver, "liff-token")

    async def test_module_api_sends_bearer_token(self):
        with HTTPServer() as httpserver:
            httpserver.expect_request(
                uri="/v2/bot/list",
                method="GET",
            ).respond_with_json({"bots": []}, status=200)

            async with AsyncLineBotClient(
                channel_access_token="module-token",
                host=httpserver.url_for("/")
            ) as client:
                await client.get_modules()

            self._assert_bearer_token(httpserver, "module-token")

    async def test_shop_api_sends_bearer_token(self):
        with HTTPServer() as httpserver:
            httpserver.expect_request(
                uri="/shop/v3/mission",
                method="POST",
            ).respond_with_json({}, status=200)

            async with AsyncLineBotClient(
                channel_access_token="shop-token",
                host=httpserver.url_for("/")
            ) as client:
                req = MissionStickerRequest(
                    to="U123",
                    productId="p",
                    productType="t",
                    sendPresentMessage=False
                )
                await client.mission_sticker_v3(mission_sticker_request=req)

            self._assert_bearer_token(httpserver, "shop-token")


class TestAsyncLineBotClientWithHttpInfo(unittest.IsolatedAsyncioTestCase):
    """Test _with_http_info methods return ApiResponse with status/headers/data."""

    async def test_push_message_with_http_info(self):
        with HTTPServer() as httpserver:
            httpserver.expect_request(
                uri="/v2/bot/message/push",
                method="POST",
            ).respond_with_json(
                {"sentMessages": [{"id": "msg001", "quoteToken": "qt001"}]},
                status=200
            )

            async with AsyncLineBotClient(
                channel_access_token="test-token",
                host=httpserver.url_for("/")
            ) as client:
                req = PushMessageRequest(
                    to="U123",
                    messages=[TextMessage(text="hello")]
                )
                api_response = await client.push_message_with_http_info(
                    push_message_request=req
                )

            self.assertEqual(api_response.status_code, 200)
            self.assertIsNotNone(api_response.data)
            self.assertEqual(api_response.data.sent_messages[0].id, "msg001")


class TestAsyncLineBotClientBlobApi(unittest.IsolatedAsyncioTestCase):
    """Test MessagingApiBlob delegation through AsyncLineBotClient."""

    async def test_get_message_content(self):
        content = b"fake-binary-content"
        with HTTPServer() as httpserver:
            httpserver.expect_request(
                uri="/v2/bot/message/msg123/content",
                method="GET",
            ).respond_with_data(content, status=200, content_type="image/jpeg")

            async with AsyncLineBotClient(
                channel_access_token="test-token",
                host=httpserver.url_for("/")
            ) as client:
                result = await client.get_message_content(message_id="msg123")

            self.assertEqual(result, content)
            request, _ = httpserver.log[0]
            self.assertEqual(request.method, "GET")
            self.assertEqual(request.path, "/v2/bot/message/msg123/content")


class TestAsyncLineBotClientErrors(unittest.IsolatedAsyncioTestCase):
    """Test error handling through AsyncLineBotClient."""

    async def test_api_error_from_messaging(self):
        with HTTPServer() as httpserver:
            httpserver.expect_request(
                uri="/v2/bot/message/push",
                method="POST",
            ).respond_with_json(
                {"message": "Invalid request"},
                status=400
            )

            async with AsyncLineBotClient(
                channel_access_token="test-token",
                host=httpserver.url_for("/")
            ) as client:
                req = PushMessageRequest(
                    to="U123",
                    messages=[TextMessage(text="hello")]
                )
                with self.assertRaises(MessagingApiException) as ctx:
                    await client.push_message(push_message_request=req)

                self.assertEqual(ctx.exception.status, 400)


if __name__ == '__main__':
    unittest.main()
