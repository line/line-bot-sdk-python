# -*- coding: utf-8 -*-
#  Licensed under the Apache License, Version 2.0 (the "License"); you may
#  not use this file except in compliance with the License. You may obtain
#  a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#  WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#  License for the specific language governing permissions and limitations
#  under the License.

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
