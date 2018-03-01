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
from linebot.models import (
    URITemplateAction,
    RichMenu, RichMenuBound, RichMenuArea
)


class TestLineBotApi(unittest.TestCase):

    maxDiff = None

    def setUp(self):
        self.tested = LineBotApi('channel_secret')

        self.rich_menu_id = 'richmenu-0000000000'
        self.user_id = 'userid'
        self.rich_menu = RichMenu(
                size=RichMenuBound(
                    width=2500,
                    height=1686
                ),
                selected=False,
                name="nice richmenu",
                chatBarText="touch me",
                areas=[
                    RichMenuArea(
                        RichMenuBound(
                            x=0,
                            y=0,
                            width=833,
                            height=843
                        ),
                        URITemplateAction(
                            uri='line://nv/location'
                        )
                    )
                ]
            )

    @responses.activate
    def test_delete_rich_menu(self):
        responses.add(
            responses.DELETE,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/richmenu/{rich_menu_id}'.format(
                rich_menu_id=self.rich_menu_id
            ),
            json={}, status=200
        )

        self.tested.delete_rich_menu(self.rich_menu_id)

        request = responses.calls[0].request
        self.assertEqual(request.method, 'DELETE')
        self.assertEqual(
            request.url,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/richmenu/{rich_menu_id}'.format(
                rich_menu_id=self.rich_menu_id
            )
        )

    @responses.activate
    def test_link_rich_menu_to_user(self):
        responses.add(
            responses.POST,
            LineBotApi.DEFAULT_API_ENDPOINT +
            '/v2/bot/user/{user_id}/richmenu/{rich_menu_id}'.format(
                user_id=self.user_id,
                rich_menu_id=self.rich_menu_id
            ),
            json={}, status=200
        )

        self.tested.link_rich_menu_to_user(self.user_id, self.rich_menu_id)

        request = responses.calls[0].request
        self.assertEqual(request.method, 'POST')
        self.assertEqual(
            request.url,
            LineBotApi.DEFAULT_API_ENDPOINT +
            '/v2/bot/user/{user_id}/richmenu/{rich_menu_id}'.format(
                user_id=self.user_id,
                rich_menu_id=self.rich_menu_id
            )
        )

    @responses.activate
    def test_unlink_rich_menu_from_user(self):
        responses.add(
            responses.DELETE,
            LineBotApi.DEFAULT_API_ENDPOINT +
            '/v2/bot/user/{user_id}/richmenu'.format(user_id=self.user_id),
            json={}, status=200
        )

        self.tested.unlink_rich_menu_from_user(self.user_id)

        request = responses.calls[0].request
        self.assertEqual(request.method, 'DELETE')
        self.assertEqual(
            request.url,
            LineBotApi.DEFAULT_API_ENDPOINT +
            '/v2/bot/user/{user_id}/richmenu'.format(user_id=self.user_id)
        )

    @responses.activate
    def test_get_rich_menu_id_of_user(self):
        responses.add(
            responses.GET,
            LineBotApi.DEFAULT_API_ENDPOINT +
            '/v2/bot/user/{user_id}/richmenu'.format(user_id=self.user_id),
            json={}, status=200
        )

        self.tested.get_rich_menu_id_of_user(self.user_id)

        request = responses.calls[0].request
        self.assertEqual(request.method, 'GET')
        self.assertEqual(
            request.url,
            LineBotApi.DEFAULT_API_ENDPOINT +
            '/v2/bot/user/{user_id}/richmenu'.format(user_id=self.user_id)
        )

    @responses.activate
    def test_get_rich_menu_list(self):
        responses.add(
            responses.GET,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/richmenu/list',
            json={'richmenus': []}, status=200
        )

        self.tested.get_rich_menu_list()

        request = responses.calls[0].request
        self.assertEqual(request.method, 'GET')
        self.assertEqual(
            request.url,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/richmenu/list'
        )

    @responses.activate
    def test_create_rich_menu(self):
        responses.add(
            responses.POST,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/richmenu',
            json={}, status=200
        )

        self.tested.create_rich_menu(self.rich_menu)

        request = responses.calls[0].request
        self.assertEqual(request.method, 'POST')
        self.assertEqual(
            request.url,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/richmenu'
        )


if __name__ == '__main__':
    unittest.main()
