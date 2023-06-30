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

"""linebot.models.sources module."""


import warnings
from abc import ABCMeta, abstractproperty

from future.utils import with_metaclass

from .base import Base


class Source(with_metaclass(ABCMeta, Base)):
    """Abstract Base Class of Source."""

    def __init__(self, **kwargs):
        """__init__ method.

        :param kwargs:
        """
        super(Source, self).__init__(**kwargs)
        self.type = None

    @abstractproperty
    def sender_id(self):
        """Abstract property of id to send a message.

        If SourceUser, return user_id.
        If SourceGroup, return group_id.
        If SourceRoom, return room_id.

        'sender_id' is deprecated.

        :rtype: str
        """
        warnings.warn("'sender_id' is deprecated.", DeprecationWarning, stacklevel=2)
        raise NotImplementedError


class SourceUser(Source):
    """SourceUser.

    https://developers.line.biz/en/reference/messaging-api/#source-user

    JSON object which contains the source user of the event.
    """

    def __init__(self, user_id=None, **kwargs):
        """__init__ method.

        :param str user_id: ID of the source user
        :param kwargs:
        """
        super(SourceUser, self).__init__(**kwargs)

        self.type = 'user'
        self.user_id = user_id

    @property
    def sender_id(self):
        """Alias of user_id.

        'sender_id' is deprecated. Use 'user_id' instead.

        :rtype: str
        """
        warnings.warn("'sender_id' is deprecated.", DeprecationWarning, stacklevel=2)
        return self.user_id


class SourceGroup(Source):
    """SourceGroup.

    https://developers.line.biz/en/reference/messaging-api/#source-group

    JSON object which contains the source group of the event.
    """

    def __init__(self, group_id=None, user_id=None, **kwargs):
        """__init__ method.

        :param str group_id: ID of the source group
        :param str user_id: ID of the source user
        :param kwargs:
        """
        super(SourceGroup, self).__init__(**kwargs)

        self.type = 'group'
        self.group_id = group_id
        self.user_id = user_id

    @property
    def sender_id(self):
        """Alias of group_id.

        'sender_id' is deprecated. Use 'group_id' instead.

        :rtype: str
        """
        warnings.warn("'sender_id' is deprecated.", DeprecationWarning, stacklevel=2)
        return self.group_id


class SourceRoom(Source):
    """SourceRoom.

    https://developers.line.biz/en/reference/messaging-api/#source-room

    JSON object which contains the source room of the event.
    """

    def __init__(self, room_id=None, user_id=None, **kwargs):
        """__init__ method.

        :param str room_id: ID of the source room
        :param str user_id: ID of the source user
        :param kwargs:
        """
        super(SourceRoom, self).__init__(**kwargs)

        self.type = 'room'
        self.room_id = room_id
        self.user_id = user_id

    @property
    def sender_id(self):
        """Alias of room_id.

        'sender_id' is deprecated. Use 'room_id' instead.

        :rtype: str
        """
        warnings.warn("'sender_id' is deprecated.", DeprecationWarning, stacklevel=2)
        return self.room_id
