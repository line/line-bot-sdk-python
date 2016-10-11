# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

import json
import unittest

from line_bot import Base


class Hoge(Base):
    def __init__(self, **kwargs):
        super(Hoge, self).__init__(**kwargs)

        param_defaults = {
            'title': None,
            'content': None,
            'hoge_bar': None
        }
        self.set_attrs(param_defaults, kwargs)


class TestBase(unittest.TestCase):
    def test_as_json_string(self):
        self.assertEqual(
            Hoge().as_json_string(),
            '{"content": null, "hogeBar": null, "title": null}'
        )
        self.assertEqual(
            Hoge(title='title').as_json_string(),
            '{"content": null, "hogeBar": null, "title": "title"}'
        )
        self.assertEqual(
            Hoge(title='title', content='content').as_json_string(),
            '{"content": "content", "hogeBar": null, "title": "title"}'
        )
        self.assertEqual(
            Hoge(title='title', content={"hoge": "hoge"}).as_json_string(),
            '{"content": {"hoge": "hoge"}, "hogeBar": null, "title": "title"}'
        )
        self.assertEqual(
            Hoge(title=[1, 2]).as_json_string(),
            '{"content": null, "hogeBar": null, "title": [1, 2]}'
        )
        self.assertEqual(
            Hoge(hoge_bar='hoge_bar').as_json_string(),
            '{"content": null, "hogeBar": "hoge_bar", "title": null}'
        )

    def test_as_json_dict(self):
        self.assertEqual(
            Hoge().as_json_dict(),
            {'content': None, 'hogeBar': None, 'title': None}
        )
        self.assertEqual(
            Hoge(title='title').as_json_dict(),
            {'content': None, 'hogeBar': None, 'title': 'title'}
        )
        self.assertEqual(
            Hoge(title='title', content='content').as_json_dict(),
            {'content': 'content', 'hogeBar': None, 'title': 'title'}
        )
        self.assertEqual(
            Hoge(title='title', content={"hoge": "hoge"}).as_json_dict(),
            {'content': {'hoge': 'hoge'}, 'hogeBar': None, 'title': 'title'}
        )
        self.assertEqual(
            Hoge(title=[1, 2]).as_json_dict(),
            {'content': None, 'hogeBar': None, 'title': [1, 2]}
        )

    def test_new_from_json_dict(self):
        self.assertEqual(
            Hoge.new_from_json_dict({"title": "title"}),
            Hoge(title='title')
        )
        self.assertEqual(
            Hoge.new_from_json_dict(json.loads('{"title": "title"}')),
            Hoge(title='title')
        )
        self.assertEqual(
            Hoge.new_from_json_dict({"hoge_bar": "hoge_bar"}),
            Hoge(hoge_bar='hoge_bar')
        )
        self.assertEqual(
            Hoge.new_from_json_dict({"hogeBar": "hoge_bar"}),
            Hoge(hoge_bar='hoge_bar')
        )
