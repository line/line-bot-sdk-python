# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

import unittest

from linebot import (
    LineBotApi
)


class TestLineBotApi(unittest.TestCase):
    def setUp(self):
        self.tested = LineBotApi('channel_secret')

    def test_get_content(self):
        pass
        # stream = self.tested.get_content(12345)
        # with open('/tmp/content.jpg', 'wb') as f:
        #     for chunk in stream:
        #         f.write(chunk)
        #     f.close()

if __name__ == '__main__':
    unittest.main()
