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

"""linebot.constants.postback_input_option module."""

from deprecated import deprecated
from linebot.deprecations import LineBotSdkDeprecatedIn30


@deprecated(reason="Use 'from linebot.v3.messaging import PostbackAction' instead. See https://github.com/line/line-bot-sdk-python/blob/master/README.rst for more details.", version='3.0.0', category=LineBotSdkDeprecatedIn30)  # noqa: E501
class PostbackInputOption:
    """Constant class for Postback input option."""

    CLOSE_RICH_MENU = "closeRichMenu"
    OPEN_RICH_MENU = "openRichMenu"
    OPEN_KEYBOARD = "openKeyboard"
    OPEN_VOICE = "openVoice"
