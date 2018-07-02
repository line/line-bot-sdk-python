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

from __future__ import unicode_literals, absolute_import

import unittest

from linebot.exceptions import LineBotApiError
from linebot.models import Error, ErrorDetail


class TestUtils(unittest.TestCase):
    def test_str(self):
        line_bot_api_error = LineBotApiError(
            400,
            error=Error(message='The request body has 1 error(s)',
                        details=[ErrorDetail(message='May not be empty',
                                             property='messages[0].text')]))
        self.assertEqual(line_bot_api_error.__str__(),
                         'LineBotApiError: status_code=400, error_response={"details": '
                         '[{"message": "May not be empty", "property": "messages[0].text"}], '
                         '"message": "The request body has 1 error(s)"}')


if __name__ == '__main__':
    unittest.main()
