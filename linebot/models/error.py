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

"""linebot.models.error module."""


from .base import Base

from deprecated import deprecated
from linebot.deprecations import LineBotSdkDeprecatedIn30


@deprecated(reason="Use 'from linebot.v3.messaging import ErrorResponse' instead. See https://github.com/line/line-bot-sdk-python/blob/master/README.rst for more details.", version='3.0.0', category=LineBotSdkDeprecatedIn30)  # noqa: E501
class Error(Base):
    """Error response of LINE messaging API.

    https://developers.line.biz/en/reference/messaging-api/#error-response
    """

    def __init__(self, message=None, details=None, **kwargs):
        """__init__ method.

        :param str message: Summary of the error
        :param details: ErrorDetail instance list
        :type details: list[T <= :py:class:`linebot.models.error.ErrorDetail`]
        :param kwargs:
        """
        super(Error, self).__init__(**kwargs)

        self.message = message

        new_details = []
        if details:
            for detail in details:
                new_details.append(
                    self.get_or_new_from_json_dict(detail, ErrorDetail)
                )
        self.details = new_details


@deprecated(reason="Use 'from linebot.v3.messaging import ErrorDetail' instead. See https://github.com/line/line-bot-sdk-python/blob/master/README.rst for more details.", version='3.0.0', category=LineBotSdkDeprecatedIn30)  # noqa: E501
class ErrorDetail(Base):
    """ErrorDetail response of LINE messaging API."""

    def __init__(self, message=None, property=None, **kwargs):
        """__init__ method.

        :param str message: Details of the error message
        :param str property: Related property
        :param kwargs:
        """
        super(ErrorDetail, self).__init__(**kwargs)

        self.message = message
        self.property = property
