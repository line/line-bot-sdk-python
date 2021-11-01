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

"""linebot.models.recipient module."""


from abc import ABCMeta

from future.utils import with_metaclass

from .base import Base


class Limit(with_metaclass(ABCMeta, Base)):
    """Limit.

    https://developers.line.biz/en/reference/messaging-api/#send-narrowcast-message

    """

    def __init__(self, max=None, up_to_remaining_quota=False, **kwargs):
        """__init__ method.

        :param kwargs:
        """
        super(Limit, self).__init__(**kwargs)

        self.max = max
        self.up_to_remaining_quota = up_to_remaining_quota
