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


class BaseError(Exception):
    def __init__(self, message='-'):
        self.message = message

    def __repr__(self):
        return str(self)

    def __str__(self):
        return '<{0} [{1}]>'.format(
            self.__class__.__name__, self.message
        )


class InvalidSignatureError(BaseError):
    def __init__(self, message='-'):
        super(InvalidSignatureError, self).__init__(message)


class LineBotApiError(BaseError):
    def __init__(self, status_code, error=None):
        """When BOT API response error, this error will be thrown.

        Args:
            status_code: http status code
            error: Error class object.
                https://devdocs.line.me/en/#error-response
        """
        super(LineBotApiError, self).__init__(error.message)

        self.status_code = status_code
        self.error = error
