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

"""linebot.v3.models.events module."""

from linebot.v3.webhooks.models.event import Event
from linebot.v3.utils import to_snake_case

class UnknownEvent(Event):
    """Unknown event.

    We welcome your contribution to line-bot-sdk-python!
    """

    @classmethod
    def new_from_json_dict(cls, data):
        """Create a new instance from a dict.

        :param data: JSON dict
        """
        new_data = {to_snake_case(key): value
                    for key, value in data.items()}

        return cls(**new_data)
