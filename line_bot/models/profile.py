# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .base import Base


class Profile(Base):
    def __init__(
            self, display_name=None, user_id=None, picture_url=None,
            status_message=None, **kwargs
    ):
        """Profile

        https://devdocs.line.me/en/#bot-api-get-profile

        Args:
            display_name: Display name
            user_id: User ID
            picture_url: Image URL
            status_message: Status message
            **kwargs:
        """
        super(Profile, self).__init__(**kwargs)

        self.display_name = display_name
        self.user_id = user_id
        self.picture_url = picture_url
        self.status_message = status_message
