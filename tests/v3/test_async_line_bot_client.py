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

import pytest
from pytest_httpserver import HTTPServer

from linebot.v3 import AsyncLineBotClient
from linebot.v3.messaging import (
    PushMessageRequest,
    TextMessage,
)
from linebot.v3.messaging.exceptions import ApiException as MessagingApiException


@pytest.mark.asyncio
async def test_async_push_message():
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

        assert len(httpserver.log) == 1
        request, _ = httpserver.log[0]
        assert request.method == "POST"
        assert request.path == "/v2/bot/message/push"
        body = json.loads(request.data.decode("utf-8"))
        assert body["to"] == "U123"
        assert body["messages"][0]["type"] == "text"
        assert body["messages"][0]["text"] == "hello"


@pytest.mark.asyncio
async def test_async_get_followers():
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

        assert response.user_ids == expected_response["userIds"]
        assert response.next == expected_response["next"]
        assert len(httpserver.log) == 1
        request, _ = httpserver.log[0]
        assert request.method == "GET"
        assert b"start=xBQU2IB" in request.query_string
        assert b"limit=100" in request.query_string


@pytest.mark.asyncio
async def test_async_get_number_of_followers():
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

        assert response.followers == 123
        assert response.targeted_reaches == 100
        request, _ = httpserver.log[0]
        assert b"date=20240101" in request.query_string


@pytest.mark.asyncio
async def test_async_get_profile():
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

        assert response.display_name == "Test User"
        assert response.user_id == "U4af4980629"
        request, _ = httpserver.log[0]
        assert request.path == "/v2/bot/profile/U4af4980629"


@pytest.mark.asyncio
async def test_async_api_error():
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
            with pytest.raises(MessagingApiException) as exc_info:
                await client.push_message(push_message_request=req)

            assert exc_info.value.status == 400


if __name__ == '__main__':
    unittest.main()
