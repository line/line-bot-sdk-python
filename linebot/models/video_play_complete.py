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

"""linebot.models.video_play_complete module."""


from abc import ABCMeta

from future.utils import with_metaclass

from .base import Base

from deprecated import deprecated

from linebot.deprecations import (
    LineBotSdkDeprecatedIn30
)


@deprecated(reason="Use 'from linebot.v3.webhooks import VideoPlayComplete' instead. See https://github.com/line/line-bot-sdk-python/blob/master/README.rst for more details.", version='3.0.0', category=LineBotSdkDeprecatedIn30)  # noqa: E501
class VideoPlayComplete(with_metaclass(ABCMeta, Base)):
    """Abstract Base Class of VideoPlayComplete."""

    def __init__(self, tracking_id=None, **kwargs):
        """__init__ method.

        :param str tracking_id: the video viewing complete event occurs
            when the user finishes watching the video.
            Max character limit: 100.
        :param kwargs:
        """
        super(VideoPlayComplete, self).__init__(**kwargs)
        self.tracking_id = tracking_id
