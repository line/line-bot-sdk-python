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

"""linebot.models.emojis module."""


from abc import ABCMeta

from future.utils import with_metaclass

from .base import Base


class Emojis(with_metaclass(ABCMeta, Base)):
    """Emojis.

    https://developers.line.biz/en/reference/messaging-api/#text-message

    """

    def __init__(self, index=None, length=None, product_id=None, emoji_id=None, **kwargs):
        """__init__ method.

        :param kwargs:
        """
        super(Emojis, self).__init__(**kwargs)

        self.index = index
        self.length = length
        self.product_id = product_id
        self.emoji_id = emoji_id
