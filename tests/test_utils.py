# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

import unittest

from linebot.utils import to_camel_case, to_snake_case


class TestUtils(unittest.TestCase):
    def test_to_camel_case(self):
        self.assertEqual(
            to_snake_case('hogeBar'),
            'hoge_bar'
        )

    def test_to_camel_case(self):
        self.assertEqual(
            to_camel_case('hoge_bar'),
            'hogeBar'
        )
