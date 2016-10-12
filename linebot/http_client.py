# -*- coding: utf-8 -*-
#  Licensed under the Apache License, Version 2.0 (the "License"); you may
#  not use this file except in compliance with the License. You may obtain
#  a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#  WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#  License for the specific language governing permissions and limitations
#  under the License.

from __future__ import unicode_literals

from abc import ABCMeta, abstractmethod
from future.utils import with_metaclass
import requests


class HttpClient(with_metaclass(ABCMeta)):
    DEFAULT_TIMEOUT = 5

    def __init__(self, timeout=DEFAULT_TIMEOUT):
        """Constructor of HttpClient

        Args:
            timeout: How long to wait for the server to send data before giving up,
                as a float, or a :ref:`(connect timeout, read timeout) <timeouts>` tuple.
        """

        self.timeout = timeout

    @abstractmethod
    def get(self, url, headers=None, params=None, timeout=None):
        """GET request

        Args:
            url: Request url
            headers: Request headers
            params: Request query parameter
            timeout: How long to wait for the server to send data before giving up,
                as a float, or a :ref:`(connect timeout, read timeout) <timeouts>` tuple.
                Default is self.timeout
        """
        raise NotImplementedError

    @abstractmethod
    def get_stream(self, url, headers=None, params=None, timeout=None,
                   chunk_size=1024, decode_unicode=False):
        """GET request. response is chunk content.

        Args:
            url: Request url
            headers: Request headers
            params: Request query parameter
            timeout: How long to wait for the server to send data before giving up,
                as a float, or a :ref:`(connect timeout, read timeout) <timeouts>` tuple. Default is self.timeout
            chunk_size:
            decode_unicode:
        """
        raise NotImplementedError

    @abstractmethod
    def post(self, url, headers=None, data=None, timeout=None):
        """POST request.

        Args:
            url: Request url
            headers: Request headers
            data: Dictionary, bytes, or file-like object to send in the body
            timeout: How long to wait for the server to send data before giving up,
                as a float, or a :ref:`(connect timeout, read timeout) <timeouts>` tuple. Default is self.timeout
        """
        raise NotImplementedError


class RequestsHttpClient(HttpClient):
    def __init__(self, timeout=HttpClient.DEFAULT_TIMEOUT):
        """Constructor of RequestsHttpClient

        'requests' implementation.

        Args:
            timeout: How long to wait for the server to send data before giving up,
                as a float, or a :ref:`(connect timeout, readtimeout) <timeouts>` tuple.
        """

        super(RequestsHttpClient, self).__init__(timeout)

    def get(self, url, headers=None, params=None, timeout=None):
        """GET request

        Args:
            url: Request url
            headers: Request headers
            params: Request query parameter
            timeout: How long to wait for the server to send data before giving up,
                as a float, or a :ref:`(connect timeout, read timeout) <timeouts>` tuple. Default is self.timeout

        Returns: Response object
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
        """GET request. response is chunk content.

        Args:
            url: Request url
            headers: Request headers
            params: Request query parameter
            timeout: How long to wait for the server to send data before giving up,
                as a float, or a :ref:`(connect timeout, read timeout) <timeouts>` tuple. Default is self.timeout
            chunk_size:
            decode_unicode: If decode_unicode is True, content will be decoded
                using the best available encoding based on the response.

        Returns: Response object
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

        Args:
            url: Request url
            headers: Request headers
            data: Dictionary, bytes, or file-like object to send in the body
            timeout: How long to wait for the server to send data before giving up,
                as a float, or a :ref:`(connect timeout, read timeout) <timeouts>` tuple. Default is self.timeout

        Returns: Response object
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
    def __init__(self, status_code=None, body=None, headers=None, body_stream=None):
        self.status_code = status_code
        self.headers = headers
        self.body = body
        self.body_stream = body_stream
