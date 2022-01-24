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
from aiohttp.test_utils import AioHTTPTestCase
from linebot.exceptions import LineBotApiError
from aiohttp import web
from linebot import AsyncLineBotApi
from linebot.aiohttp_async_http_client import AiohttpAsyncHttpClient


class MyAppTestCase(AioHTTPTestCase):
    async def get_application(self):
        self.exception = {
            "message": "user id not found",
            "details": [
                {
                    "message": "user id not found",
                    "property": "... some property"
                }
            ]
        }

        async def profile(request):
            return web.json_response(self.exception, status=404)

        app = web.Application()
        app.router.add_get('//v2/bot/profile/failed', profile)
        return app

    async def test_async_get_profile_exception(self):
        self.server.skip_url_asserts = True
        async_client = AiohttpAsyncHttpClient(session=self.client)
        bot = AsyncLineBotApi('TOKENTOKEN', async_client, endpoint='/')
        with self.assertRaises(LineBotApiError):
            await bot.get_profile('failed')
