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

"""linebot.async_http_client module."""

from __future__ import unicode_literals

from abc import ABCMeta, abstractmethod, abstractproperty

from future.utils import with_metaclass


class AsyncHttpClient(with_metaclass(ABCMeta)):
    """Abstract Base Classes of HttpClient."""

    DEFAULT_TIMEOUT = 5

    def __init__(self, timeout=DEFAULT_TIMEOUT):
        """__init__ method.

        :param timeout: (optional) How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, read timeout) float tuple.
            Default is :py:attr:`DEFAULT_TIMEOUT`
        :type timeout: float | tuple(float, float)
        :rtype: T <= :py:class:`HttpResponse`
        :return: HttpResponse instance
        """
        self.timeout = timeout

    @abstractmethod
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
        :rtype: T <= :py:class:`HttpResponse`
        :return: HttpResponse instance
        """
        raise NotImplementedError

    @abstractmethod
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
        :rtype: T <= :py:class:`HttpResponse`
        :return: HttpResponse instance
        """
        raise NotImplementedError

    @abstractmethod
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
        :rtype: T <= :py:class:`HttpResponse`
        :return: HttpResponse instance
        """
        raise NotImplementedError

    @abstractmethod
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
        :rtype: :py:class:`AsyncHttpResponse`
        :return: AsyncHttpResponse instance
        """
        raise NotImplementedError


class AsyncHttpResponse(with_metaclass(ABCMeta)):
    """HttpResponse."""

    @abstractproperty
    def status_code(self):
        """Get status code."""
        raise NotImplementedError

    @abstractproperty
    def headers(self):
        """Get headers."""
        raise NotImplementedError

    @abstractproperty
    async def text(self):
        """Get response body as text-decoded."""
        raise NotImplementedError

    @abstractproperty
    async def content(self):
        """Get response body as binary."""
        raise NotImplementedError

    @abstractproperty
    def json(self):
        """Get response body as json-decoded."""
        raise NotImplementedError

    @abstractmethod
    def iter_content(self, chunk_size=1024):
        """Get response body as iterator content (stream).

        :param int chunk_size:
        """
        raise NotImplementedError
