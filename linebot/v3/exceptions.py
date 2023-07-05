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

"""linebot.v3.exceptions module."""


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
        """repr."""
        return str(self)

    def __str__(self):
        """str.

        :rtype: str
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
