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
import responses

from linebot import (
    LineBotApi
)
from linebot.models.rich_menu import RichMenuAlias


class TestLineBotApi(unittest.TestCase):
    maxDiff = None

    def setUp(self):
        self.tested = LineBotApi('channel_secret')

        self.alias_id_a = 'richmenu-alias-a'
        self.alias_id_b = 'richmenu-alias-b'
        self.rich_menu_id_a = 'richmenu-0000000'
        self.rich_menu_id_b = 'richmenu-1111111'

    @responses.activate
    def test_create_rich_menu_alias(self):
        responses.add(
            responses.POST,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/richmenu/alias',
            json={
                "richMenuAliasId": self.alias_id_a,
                "richMenuId": self.rich_menu_id_a
            }, status=200
        )
        alias = RichMenuAlias(
            rich_menu_alias_id=self.alias_id_a,
            rich_menu_id=self.rich_menu_id_a
        )
        result = self.tested.create_rich_menu_alias(alias)

        request = responses.calls[0].request
        self.assertEqual(request.method, 'POST')
        self.assertEqual(
            request.url,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/richmenu/alias'
        )
        self.assertEqual(result, None)

    @responses.activate
    def test_delete_rich_menu(self):
        responses.add(
            responses.DELETE,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/richmenu/alias/' + self.alias_id_a,
            json={}, status=200
        )

        result = self.tested.delete_rich_menu_alias(self.alias_id_a)

        request = responses.calls[0].request
        self.assertEqual(request.method, 'DELETE')
        self.assertEqual(
            request.url,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/richmenu/alias/richmenu-alias-a'
        )
        self.assertEqual(result, None)

    @responses.activate
    def test_update_rich_menu_alias(self):
        responses.add(
            responses.POST,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/richmenu/alias/' + self.alias_id_a,
            json={}, status=200
        )

        alias = RichMenuAlias(rich_menu_id=self.rich_menu_id_a)
        result = self.tested.update_rich_menu_alias(
            rich_menu_alias_id=self.alias_id_a, rich_menu_alias=alias
        )

        request = responses.calls[0].request
        self.assertEqual(request.method, 'POST')
        self.assertEqual(
            request.url,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/richmenu/alias/richmenu-alias-a'
        )
        self.assertEqual(result, None)

    @responses.activate
    def test_get_rich_menu_alias(self):
        responses.add(
            responses.GET,
            LineBotApi.DEFAULT_API_ENDPOINT +
            '/v2/bot/richmenu/alias/' + self.alias_id_a,
            json={
                "richMenuAliasId": self.alias_id_a,
                "richMenuId": self.rich_menu_id_a
            }, status=200
        )

        result = self.tested.get_rich_menu_alias(rich_menu_alias_id=self.alias_id_a)
        request = responses.calls[0].request
        self.assertEqual(request.method, 'GET')
        self.assertEqual(
            request.url,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/richmenu/alias/richmenu-alias-a'
        )
        self.assertEqual(result.rich_menu_alias_id, 'richmenu-alias-a')
        self.assertEqual(result.rich_menu_id, 'richmenu-0000000')

    @responses.activate
    def test_get_rich_menu_alias_list(self):
        responses.add(
            responses.GET,
            LineBotApi.DEFAULT_API_ENDPOINT +
            '/v2/bot/richmenu/alias/list',
            json={
                "aliases": [{
                    "richMenuAliasId": self.alias_id_a,
                    "richMenuId": self.rich_menu_id_a
                }, {
                    "richMenuAliasId": self.alias_id_b,
                    "richMenuId": self.rich_menu_id_b
                }]
            }, status=200
        )

        result = self.tested.get_rich_menu_alias_list()
        request = responses.calls[0].request
        self.assertEqual(request.method, 'GET')
        self.assertEqual(
            request.url,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/richmenu/alias/list'
        )
        self.assertEqual(type(result.aliases), list)
        self.assertEqual(result.aliases[0].rich_menu_alias_id, "richmenu-alias-a")
        self.assertEqual(
            result.aliases[0].rich_menu_id, "richmenu-0000000"
        )
        self.assertEqual(result.aliases[1].rich_menu_alias_id, "richmenu-alias-b")
        self.assertEqual(
            result.aliases[1].rich_menu_id, "richmenu-1111111"
        )

    @responses.activate
    def test_get_rich_menu_alias_empty_list(self):
        responses.add(
            responses.GET,
            LineBotApi.DEFAULT_API_ENDPOINT +
            '/v2/bot/richmenu/alias/list',
            json={"aliases": []},
            status=200
        )

        result = self.tested.get_rich_menu_alias_list()
        request = responses.calls[0].request
        self.assertEqual(request.method, 'GET')
        self.assertEqual(
            request.url,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/richmenu/alias/list'
        )
        self.assertEqual(type(result.aliases), list)
        self.assertEqual(len(result.aliases), 0)


if __name__ == '__main__':
    unittest.main()
