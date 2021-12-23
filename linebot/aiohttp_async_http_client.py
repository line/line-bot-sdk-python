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

"""linebot.aiohttp_async_http_client module."""

from linebot import AsyncHttpClient, AsyncHttpResponse


class AiohttpAsyncHttpClient(AsyncHttpClient):
    """HttpClient implemented by requests."""

    def __init__(self, session, timeout=AsyncHttpClient.DEFAULT_TIMEOUT):
        """__init__ method.

        :param timeout: (optional) How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, read timeout) float tuple.
            Default is :py:attr:`DEFAULT_TIMEOUT`
        :type timeout: float | tuple(float, float)
        """
        super(AiohttpAsyncHttpClient, self).__init__(timeout)
        self.session = session

    async def get(self, url, headers=None, params=None, timeout=None):
        """GET request.

        :param str url: Request url
        :param dict headers: (optional) Request headers
        :param dict params: (optional) Request query parameter
        :param timeout: (optional), How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, read timeout) float tuple.
            Default is :py:attr:`self.timeout`
        :type timeout: float | tuple(float, float)
        :rtype: :py:class:`AsyncHttpResponse`
        :return: AsyncHttpResponse instance
        """
        if timeout is None:
            timeout = self.timeout

        response = await self.session.get(url, headers=headers, params=params, timeout=timeout)
        return AiohttpAsyncHttpResponse(response)

    async def post(self, url, headers=None, data=None, timeout=None):
        """POST request.

        :param str url: Request url
        :param dict headers: (optional) Request headers
        :param data: (optional) Dictionary, bytes, or file-like object to send in the body
        :param timeout: (optional), How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, read timeout) float tuple.
            Default is :py:attr:`self.timeout`
        :type timeout: float | tuple(float, float)
        :rtype: :py:class:`AiohttpAsyncHttpResponse`
        :return: AiohttpAsyncHttpResponse instance
        """
        if timeout is None:
            timeout = self.timeout

        response = await self.session.post(url, headers=headers, data=data, timeout=timeout)
        return AiohttpAsyncHttpResponse(response)

    async def delete(self, url, headers=None, data=None, timeout=None):
        """DELETE request.

        :param str url: Request url
        :param dict headers: (optional) Request headers
        :param data: (optional) Dictionary, bytes, or file-like object to send in the body
        :param timeout: (optional), How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, read timeout) float tuple.
            Default is :py:attr:`self.timeout`
        :type timeout: float | tuple(float, float)
        :rtype: :py:class:`AiohttpAsyncHttpResponse`
        :return: AiohttpAsyncHttpResponse instance
        """
        if timeout is None:
            timeout = self.timeout

        response = await self.session.delete(url, headers=headers, data=data, timeout=timeout)
        return AiohttpAsyncHttpResponse(response)

    async def put(self, url, headers=None, data=None, timeout=None):
        """PUT request.

        :param str url: Request url
        :param dict headers: (optional) Request headers
        :param data: (optional) Dictionary, bytes, or file-like object to send in the body
        :param timeout: (optional), How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, read timeout) float tuple.
            Default is :py:attr:`self.timeout`
        :type timeout: float | tuple(float, float)
        :rtype: :py:class:`AiohttpAsyncHttpResponse`
        :return: AiohttpAsyncHttpResponse instance
        """
        if timeout is None:
            timeout = self.timeout

        response = await self.session.put(url, headers=headers, data=data, timeout=timeout)
        return AiohttpAsyncHttpResponse(response)


class AiohttpAsyncHttpResponse(AsyncHttpResponse):
    """AsyncHttpResponse implemented by aiohttp's response."""

    def __init__(self, response):
        """__init__ method.

        :param response: aiohttp's response
        """
        self.response = response

    @property
    def status_code(self):
        """Get status code."""
        return self.response.status

    @property
    def headers(self):
        """Get headers.

        :rtype :py:class:`aiohttp.multidict.CIMultiDictProxy`
        """
        return self.response.headers

    @property
    async def text(self):
        """Get response body as text-decoded."""
        return await self.response.text()

    @property
    async def content(self):
        """Get response body as binary."""
        return await self.response.content.read()

    @property
    async def json(self):
        """Get response body as json-decoded."""
        return await self.response.json()

    def iter_content(self, chunk_size=1024):
        """Get response body as iterator content (stream).

        :param int chunk_size:
        """
        return self.response.content.iter_chunked(chunk_size)
