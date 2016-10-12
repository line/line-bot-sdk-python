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

"""linebot.http_client module."""

from __future__ import unicode_literals

from abc import ABCMeta, abstractmethod

import requests
from future.utils import with_metaclass


class HttpClient(with_metaclass(ABCMeta)):
    """Abstract Base Classes of HttpClient."""

    DEFAULT_TIMEOUT = 5

    def __init__(self, timeout=DEFAULT_TIMEOUT):
        """__init__ method.

        :param float|tuple(float, float) timeout: (optional), How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, readtimeout) float tuple.
            Default is DEFAULT_TIMEOUT
        """
        self.timeout = timeout

    @abstractmethod
    def get(self, url, headers=None, params=None, timeout=None):
        """GET request.

        :param str url: Request url
        :param dict headers: (optional) Request headers
        :param dict params: (optional) Request query parameter
        :param float|tuple(float, float) timeout: (optional), How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, readtimeout) float tuple.
            Default is DEFAULT_TIMEOUT
        """
        raise NotImplementedError

    @abstractmethod
    def get_stream(self, url, headers=None, params=None, timeout=None,
                   chunk_size=1024, decode_unicode=False):
        """GET request. Response is chunk content.

        :param str url: Request url
        :param dict headers: (optional) Request headers
        :param dict params: (optional) Request query parameter
        :param float|tuple(float, float) timeout: (optional), How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, readtimeout) float tuple.
            Default is DEFAULT_TIMEOUT
        :param int chunk_size: (optional) Chunk size
        :param boole decode_unicode: (optional) Decode unicode
        """
        raise NotImplementedError

    @abstractmethod
    def post(self, url, headers=None, data=None, timeout=None):
        """POST request.

        :param str url: Request url
        :param dict headers: (optional) Request headers
        :param data: (optional) Dictionary, bytes, or file-like object to send in the body
        :param float|tuple(float, float) timeout: (optional), How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, readtimeout) float tuple.
            Default is DEFAULT_TIMEOUT
        """
        raise NotImplementedError


class RequestsHttpClient(HttpClient):
    """HttpClient implemented by requests."""

    def __init__(self, timeout=HttpClient.DEFAULT_TIMEOUT):
        """__init__ method.

        :param float|tuple(float, float) timeout: (optional), How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, readtimeout) float tuple.
            Default is HttpClient.DEFAULT_TIMEOUT
        """
        super(RequestsHttpClient, self).__init__(timeout)

    def get(self, url, headers=None, params=None, timeout=None):
        """GET request.

        :param str url: Request url
        :param dict headers: (optional) Request headers
        :param dict params: (optional) Request query parameter
        :param float|tuple(float, float) timeout: (optional), How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, readtimeout) float tuple.
            Default is DEFAULT_TIMEOUT
        :rtype: HttpResponse
        :return:
        """
        if timeout is None:
            timeout = self.timeout

        response = requests.get(
            url, headers=headers, params=params, timeout=timeout
        )

        return HttpResponse(
            status_code=response.status_code, headers=response.headers,
            body=response.text)

    def get_stream(self, url, headers=None, params=None, timeout=None,
                   chunk_size=1024, decode_unicode=False):
        """GET request. Response is chunk content.

        :param str url: Request url
        :param dict headers: (optional) Request headers
        :param dict params: (optional) Request query parameter
        :param float|tuple(float, float) timeout: (optional), How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, readtimeout) float tuple.
            Default is DEFAULT_TIMEOUT
        :param int chunk_size: (optional) Chunk size
        :param boole decode_unicode: (optional) Decode unicode
        :rtype: HttpResponse
        :return:
        """
        if timeout is None:
            timeout = self.timeout

        response = requests.get(
            url, headers=headers, params=params, timeout=timeout,
            stream=True
        )

        if 200 <= response.status_code < 300:
            return HttpResponse(
                status_code=response.status_code, headers=response.headers,
                body_stream=response.iter_content(
                    chunk_size=chunk_size, decode_unicode=decode_unicode
                )
            )
        else:
            return HttpResponse(
                status_code=response.status_code, headers=response.headers,
                body=response.text)

    def post(self, url, headers=None, data=None, timeout=None):
        """POST request.

        :param str url: Request url
        :param dict headers: (optional) Request headers
        :param data: (optional) Dictionary, bytes, or file-like object to send in the body
        :param float|tuple(float, float) timeout: (optional), How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, readtimeout) float tuple.
            Default is DEFAULT_TIMEOUT
        :rtype: HttpResponse
        :return:
        """
        if timeout is None:
            timeout = self.timeout

        response = requests.post(
            url, headers=headers, data=data, timeout=timeout
        )

        return HttpResponse(
            status_code=response.status_code, headers=response.headers,
            body=response.text)


class HttpResponse(object):
    """HttpResponse container."""

    def __init__(self, status_code=None, body=None, headers=None, body_stream=None):
        """__init__ method.

        :param str status_code: Status code
        :param str body: Response body as text
        :param dict headers: Response headers
        :param iterator body_stream:
        """
        self.status_code = status_code
        self.headers = headers
        self.body = body
        self.body_stream = body_stream
