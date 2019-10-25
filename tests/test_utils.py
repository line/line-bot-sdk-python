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

from linebot.utils import to_camel_case, to_snake_case, safe_compare_digest


class TestUtils(unittest.TestCase):
    def test_to_snake_case(self):
        self.assertEqual(to_snake_case('hogeBarFuga'), 'hoge_bar_fuga')
        self.assertEqual(to_snake_case('uniqueMediaPlayed100Percent'), 'unique_media_played_100_percent')
        self.assertEqual(to_snake_case('festival20Days'), 'festival_20_days')
        self.assertEqual(to_snake_case('festival20days'), 'festival_20_days')

    def test_to_camel_case(self):
        self.assertEqual(to_camel_case('hoge_bar'), 'hogeBar')
        self.assertEqual(to_camel_case('unique_media_played_100_percent'), 'uniqueMediaPlayed100Percent')

    def test_safe_compare_digest_true(self):
        self.assertTrue(safe_compare_digest('/gg9a+LvFevTH1sd7', '/gg9a+LvFevTH1sd7'))

    def test_safe_compare_digest_false_same_size(self):
        self.assertFalse(safe_compare_digest('/gg9a+LvFevTH1sd7', '/gg9a+LvFevTH1sd8'))

    def test_safe_compare_digest_false_different_size(self):
        self.assertFalse(safe_compare_digest('/gg9a+LvFevTH1sd7', '/gg9a+LvFevTH1sd78'))


if __name__ == '__main__':
    unittest.main()
