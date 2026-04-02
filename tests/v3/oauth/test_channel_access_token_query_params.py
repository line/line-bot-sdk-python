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

"""
Regression tests verifying that query parameter names are sent as snake_case,
not camelCase.
"""

import unittest
from urllib.parse import parse_qs

from pytest_httpserver.httpserver import HTTPServer

from linebot.v3.oauth import (
    ApiClient,
    Configuration,
    ChannelAccessToken,
)


class TestQueryParamNamesAreSnakeCase(unittest.TestCase):
    """
    Verify that GET endpoints send snake_case query keys to the LINE API,
    not camelCase keys produced by the OpenAPI generator's paramName conversion.
    """

    def test_verify_channel_token_by_jwt_uses_snake_case_key(self):
        """
        verify_channel_token_by_jwt() must send `access_token=...` in the query
        string, NOT `accessToken=...`.

        Endpoint: GET /oauth2/v2.1/verify
        """
        dummy_access_token = "dummy_access_token_value"

        expected_response = {
            "client_id": "1234567890",
            "expires_in": 3599,
            "scope": "profile",
        }

        with HTTPServer() as httpserver:
            httpserver.expect_request(
                uri="/oauth2/v2.1/verify",
                method="GET",
            ).respond_with_json(expected_response, status=200)

            configuration = Configuration(
                host=httpserver.url_for("/")
            )

            with ApiClient(configuration) as api_client:
                api = ChannelAccessToken(api_client)
                api.verify_channel_token_by_jwt(access_token=dummy_access_token)

            self.assertEqual(len(httpserver.log), 1)
            req, _ = httpserver.log[0]

            query_string = req.query_string.decode("utf-8")
            parsed = parse_qs(query_string)

            # snake_case key must be present
            self.assertIn(
                "access_token", parsed,
                "Query string must contain 'access_token' (snake_case), "
                f"but got: {query_string!r}"
            )
            self.assertEqual(parsed["access_token"], [dummy_access_token])

            # camelCase key must NOT be present
            self.assertNotIn(
                "accessToken", parsed,
                "Query string must NOT contain 'accessToken' (camelCase), "
                f"but got: {query_string!r}"
            )

    def test_gets_all_valid_channel_access_token_key_ids_uses_snake_case_keys(self):
        """
        gets_all_valid_channel_access_token_key_ids() must send
        `client_assertion_type=...` and `client_assertion=...` in the query
        string, NOT `clientAssertionType=...` / `clientAssertion=...`.

        Endpoint: GET /oauth2/v2.1/tokens/kid
        """
        dummy_client_assertion_type = (
            "urn:ietf:params:oauth:client-assertion-type:jwt-bearer"
        )
        dummy_client_assertion = "eyJhbGciOiJSUzI1NiJ9.dummy.signature"

        expected_response = {
            "kids": ["key_id_1", "key_id_2"],
        }

        with HTTPServer() as httpserver:
            httpserver.expect_request(
                uri="/oauth2/v2.1/tokens/kid",
                method="GET",
            ).respond_with_json(expected_response, status=200)

            configuration = Configuration(
                host=httpserver.url_for("/")
            )

            with ApiClient(configuration) as api_client:
                api = ChannelAccessToken(api_client)
                api.gets_all_valid_channel_access_token_key_ids(
                    client_assertion_type=dummy_client_assertion_type,
                    client_assertion=dummy_client_assertion,
                )

            self.assertEqual(len(httpserver.log), 1)
            req, _ = httpserver.log[0]

            query_string = req.query_string.decode("utf-8")
            parsed = parse_qs(query_string)

            # snake_case keys must be present
            self.assertIn(
                "client_assertion_type", parsed,
                "Query string must contain 'client_assertion_type' (snake_case), "
                f"but got: {query_string!r}"
            )
            self.assertEqual(
                parsed["client_assertion_type"], [dummy_client_assertion_type]
            )

            self.assertIn(
                "client_assertion", parsed,
                "Query string must contain 'client_assertion' (snake_case), "
                f"but got: {query_string!r}"
            )
            self.assertEqual(
                parsed["client_assertion"], [dummy_client_assertion]
            )

            # camelCase keys must NOT be present
            self.assertNotIn(
                "clientAssertionType", parsed,
                "Query string must NOT contain 'clientAssertionType' (camelCase), "
                f"but got: {query_string!r}"
            )
            self.assertNotIn(
                "clientAssertion", parsed,
                "Query string must NOT contain 'clientAssertion' (camelCase), "
                f"but got: {query_string!r}"
            )


if __name__ == "__main__":
    unittest.main()
