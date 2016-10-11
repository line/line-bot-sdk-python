# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import base64
import hashlib
import hmac


class SignatureValidator(object):
    def __init__(self, channel_secret):
        """Signature validator

        https://devdocs.line.me/ja/#webhook-authentication

        Args:
            channel_secret: Channel secret
        """
        self.channel_secret = channel_secret.encode('utf-8')

    def validate(self, body, signature):
        """Check signature.

        https://devdocs.line.me/ja/#webhook-authentication

        Args:
            body: Request body (as text)
            signature: X-Line-Signature value (as text)

        Returns:

        """
        gen_signature = hmac.new(
            self.channel_secret,
            body.encode('utf-8'),
            hashlib.sha256
        ).digest()

        return hmac.compare_digest(
            signature.encode('utf-8'), base64.b64encode(gen_signature)
        )
