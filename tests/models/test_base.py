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

import json
import unittest

from linebot.models import Base


class Hoge(Base):
    def __init__(self, title=None, content=None, hoge_bar=None, **kwargs):
        super(Hoge, self).__init__(**kwargs)

        self.title = title
        self.content = content
        self.hoge_bar = hoge_bar


class TestBase(unittest.TestCase):
    def test_as_json_string(self):
        self.assertEqual(
            Hoge().as_json_string(),
            '{}')
        self.assertEqual(
            Hoge(title='title').as_json_string(),
            '{"title": "title"}')
        self.assertEqual(
            Hoge(title='title', content='content').as_json_string(),
            '{"content": "content", "title": "title"}')
        self.assertEqual(
            Hoge(title='title', content={"hoge": "hoge"}).as_json_string(),
            '{"content": {"hoge": "hoge"}, "title": "title"}')
        self.assertEqual(
            Hoge(title=[1, 2]).as_json_string(),
            '{"title": [1, 2]}')
        self.assertEqual(
            Hoge(hoge_bar='hoge_bar').as_json_string(),
            '{"hogeBar": "hoge_bar"}')

    def test_as_json_dict(self):
        self.assertEqual(
            Hoge().as_json_dict(),
            {})
        self.assertEqual(
            Hoge(title='title').as_json_dict(),
            {'title': 'title'})
        self.assertEqual(
            Hoge(title='title', content='content').as_json_dict(),
            {'content': 'content', 'title': 'title'})
        self.assertEqual(
            Hoge(title='title', content={"hoge": "hoge"}).as_json_dict(),
            {'content': {'hoge': 'hoge'}, 'title': 'title'})
        self.assertEqual(
            Hoge(title=[1, 2]).as_json_dict(),
            {'title': [1, 2]})

    def test_new_from_json_dict(self):
        self.assertEqual(
            Hoge.new_from_json_dict({"title": "title"}),
            Hoge(title='title'))
        self.assertEqual(
            Hoge.new_from_json_dict(json.loads('{"title": "title"}')),
            Hoge(title='title'))
        self.assertEqual(
            Hoge.new_from_json_dict({"hoge_bar": "hoge_bar"}),
            Hoge(hoge_bar='hoge_bar'))
        self.assertEqual(
            Hoge.new_from_json_dict({"hogeBar": "hoge_bar"}),
            Hoge(hoge_bar='hoge_bar'))


if __name__ == '__main__':
    unittest.main()
