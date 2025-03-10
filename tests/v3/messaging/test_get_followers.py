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

import unittest
from pytest_httpserver.httpserver import HTTPServer

from linebot.v3.messaging import (
    Configuration,
    ApiClient,
    MessagingApi,
)


class TestGetFollowersWithQueryParam(unittest.TestCase):
    def test_get_followers_with_query(self):
        expected_response = {
            "userIds": [
                "U4af4980629",
                "U0c229f96c4",
                "U95afb1d4df"
            ],
            "next": "yANU9IA..."
        }

        with HTTPServer() as httpserver:
            httpserver.expect_request(
                uri="/v2/bot/followers/ids",
                method="GET",
            ).respond_with_json(
                expected_response,
                status=200
            )

            configuration = Configuration(
                access_token="dummy-channel-access-token",
                host=httpserver.url_for("/")
            )

            with ApiClient(configuration) as api_client:
                line_bot_api = MessagingApi(api_client)
                response = line_bot_api.get_followers()

            # Verify response
            self.assertEqual(response.user_ids, expected_response["userIds"])
            self.assertEqual(response.next, expected_response["next"])

            # Verify request details
            self.assertEqual(len(httpserver.log), 1)
            req, res = httpserver.log[0]
            self.assertEqual(req.method, "GET")
            self.assertEqual(req.path, "/v2/bot/followers/ids")
            self.assertEqual(req.query_string, b"")

    def test_get_followers_with_start(self):
        expected_response = {
            "userIds": [
                "U4af4980629",
                "U0c229f96c4",
                "U95afb1d4df"
            ],
            "next": "yANU9IA..."
        }

        with HTTPServer() as httpserver:
            httpserver.expect_request(
                uri="/v2/bot/followers/ids",
                method="GET",
            ).respond_with_json(
                expected_response,
                status=200
            )

            configuration = Configuration(
                access_token="dummy-channel-access-token",
                host=httpserver.url_for("/")
            )

            with ApiClient(configuration) as api_client:
                line_bot_api = MessagingApi(api_client)
                response = line_bot_api.get_followers(start="dummy-start", limit=123)

            # Verify response
            self.assertEqual(response.user_ids, expected_response["userIds"])
            self.assertEqual(response.next, expected_response["next"])

            # Verify request details
            self.assertEqual(len(httpserver.log), 1)
            req, res = httpserver.log[0]
            self.assertEqual(req.method, "GET")
            self.assertEqual(req.path, "/v2/bot/followers/ids")
            self.assertEqual(req.query_string, b"start=dummy-start&limit=123")


if __name__ == '__main__':
    unittest.main()
