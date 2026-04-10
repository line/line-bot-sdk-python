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

"""linebot.models.limit module."""


from abc import ABCMeta

from future.utils import with_metaclass

from .base import Base

from deprecated import deprecated
from linebot.deprecations import LineBotSdkDeprecatedIn30


@deprecated(reason="Use 'linebot.v3.messaging' module instead. See https://github.com/line/line-bot-sdk-python/blob/master/README.rst for more details.", version='3.0.0', category=LineBotSdkDeprecatedIn30)  # noqa: E501
class Recipient(with_metaclass(ABCMeta, Base)):
    """Recipient.

    https://developers.line.biz/en/reference/messaging-api/#narrowcast-recipient

    Recipient objects represent audiences. You can specify recipients based on
    a combination of criteria using logical operator objects.
    """

    def __init__(self, **kwargs):
        """__init__ method.

        :param kwargs:
        """
        super(Recipient, self).__init__(**kwargs)

        self.type = None


@deprecated(reason="Use 'from linebot.v3.messaging import AudienceRecipient' instead. See https://github.com/line/line-bot-sdk-python/blob/master/README.rst for more details.", version='3.0.0', category=LineBotSdkDeprecatedIn30)  # noqa: E501
class AudienceRecipient(Recipient):
    """AudienceRecipient."""

    def __init__(self, group_id=None, **kwargs):
        """__init__ method.

        :param int group_id: The audience ID. Create audiences with the
            Manage Audience API.
        :param kwargs:
        """
        super(AudienceRecipient, self).__init__(**kwargs)

        self.type = "audience"
        self.audience_group_id = group_id


@deprecated(reason="Use 'from linebot.v3.messaging import RedeliveryRecipient' instead. See https://github.com/line/line-bot-sdk-python/blob/master/README.rst for more details.", version='3.0.0', category=LineBotSdkDeprecatedIn30)  # noqa: E501
class RedeliveryRecipient(Recipient):
    """RedeliveryRecipient."""

    def __init__(self, request_id=None, **kwargs):
        """__init__ method.

        :param str request_id: The request ID of the narrowcast message previously sent.
            The request IDs is an ID issued for each Messaging API request.
        :param kwargs:
        """
        super(RedeliveryRecipient, self).__init__(**kwargs)

        self.type = "redelivery"
        self.request_id = request_id
