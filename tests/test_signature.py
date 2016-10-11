# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

import unittest

from line_bot import SignatureValidator


class TestSignatureValidator(unittest.TestCase):
    def test_validate(self):
        signature_validator = SignatureValidator('channel_secret')

        self.assertEqual(
            signature_validator.validate(
                'bodybodybodybody',
                '/gg9a+LvFevTH1sd7XCQycD7tsWclCsInj7MhBHxN7k='
            ),
            True
        )
        self.assertEqual(
            signature_validator.validate(
                'bodybodybodybody', 'invalid_signature'
            ),
            False
        )
