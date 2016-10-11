# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .base import Base


class Source(Base):
    """Base Class of Source"""

    def __init__(self, **kwargs):
        super(Source, self).__init__(**kwargs)
        self.type = None

    @property
    def sender_id(self):
        raise NotImplementedError


class SourceUser(Source):
    def __init__(self, user_id=None, **kwargs):
        """SourceUser

        https://devdocs.line.me/en/#source-user

        JSON object which contains the source user of the event.

        Args:
            user_id: ID of the source user
            **kwargs:
        """
        super(SourceUser, self).__init__(**kwargs)

        self.type = 'user'
        self.user_id = user_id

    @property
    def sender_id(self):
        return self.user_id


class SourceGroup(Source):
    def __init__(self, group_id=None, **kwargs):
        """SourceGroup

        https://devdocs.line.me/en/#source-group

        JSON object which contains the source group of the event.

        Args:
            group_id: ID of the source group
            **kwargs:
        """
        super(SourceGroup, self).__init__(**kwargs)

        self.type = 'group'
        self.group_id = group_id

    @property
    def sender_id(self):
        return self.group_id


class SourceRoom(Source):
    def __init__(self, room_id=None, **kwargs):
        """SourceRoom

        https://devdocs.line.me/en/#source-room

        JSON object which contains the source room of the event.

        Args:
            room_id: ID of the source room
            **kwargs:
        """
        super(SourceRoom, self).__init__(**kwargs)

        self.type = 'room'
        self.room_id = room_id

    @property
    def sender_id(self):
        return self.room_id
