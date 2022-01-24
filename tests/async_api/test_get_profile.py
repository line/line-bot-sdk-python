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

from aiohttp import web

from linebot import (
    AsyncLineBotApi
)
from linebot.aiohttp_async_http_client import AiohttpAsyncHttpClient


async def test_async_profile(aiohttp_client, loop):
    expect = {
        'displayName': 'test',
        'userId': 'test',
        'language': 'en',
        'pictureUrl': 'https://obs.line-apps.com/...',
        'statusMessage': 'Hello, LINE!'
    }

    async def profile(request):
        return web.json_response(expect)

    app = web.Application()
    app.router.add_get('//v2/bot/profile/test', profile)

    aiohttp = await aiohttp_client(app, server_kwargs={"skip_url_asserts": True})
    async_client = AiohttpAsyncHttpClient(session=aiohttp)

    bot = AsyncLineBotApi('TOKENTOKEN', async_client, endpoint='/')
    profile_response = await bot.get_profile('test')
    assert profile_response.user_id == expect['userId']
    assert profile_response.display_name == expect['displayName']
