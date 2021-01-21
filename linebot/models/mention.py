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

"""linebot.models.mention module."""

from __future__ import unicode_literals

from abc import ABCMeta

from future.utils import with_metaclass

from .base import Base


class Mention(with_metaclass(ABCMeta, Base)):
    """Mention.

    https://developers.line.biz/en/reference/messaging-api/#text-message

    Object containing the contents of the mentioned user.
    """

    def __init__(self, mentionees=None, **kwargs):
        """__init__ method.

        :param List mentionees: Array of LINE mentionee objects
        :param kwargs:
        """
        super(Mention, self).__init__(**kwargs)

        self.mentionees = mentionees
