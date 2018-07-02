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

"""linebot.exceptions module."""

from __future__ import unicode_literals

from abc import ABCMeta

from future.utils import with_metaclass


class BaseError(with_metaclass(ABCMeta, Exception)):
    """Base Exception class."""

    def __init__(self, message='-'):
        """__init__ method.

        :param str message: Human readable message
        """
        self.message = message

    def __repr__(self):
        """repr.

        :return:
        """
        return str(self)

    def __str__(self):
        """str.

        :rtype: str
        :return:
        """
        return '<{0} [{1}]>'.format(
            self.__class__.__name__, self.message)


class InvalidSignatureError(BaseError):
    """When Webhook signature does NOT match, this error will be raised."""

    def __init__(self, message='-'):
        """__init__ method.

        :param str message: Human readable message
        """
        super(InvalidSignatureError, self).__init__(message)


class LineBotApiError(BaseError):
    """When LINE Messaging API response error, this error will be raised."""

    def __init__(self, status_code, error=None):
        """__init__ method.

        :param int status_code: http status code
        :param error: (optional) Error class object.
        :type error: :py:class:`linebot.models.error.Error`
        """
        super(LineBotApiError, self).__init__(error.message)

        self.status_code = status_code
        self.error = error

    def __str__(self):
        """str.

        :rtype: str
        :return:
        """
        return '{0}: status_code={1}, error_response={2}'.format(
            self.__class__.__name__, self.status_code, self.error)
