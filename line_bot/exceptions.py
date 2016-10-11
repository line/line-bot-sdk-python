# -*- coding: utf-8 -*-
from __future__ import unicode_literals


class BaseError(Exception):
    def __init__(self, message='-'):
        self.message = message

    def __repr__(self):
        return str(self)

    def __str__(self):
        return '<{0} [{1}]>'.format(
            self.__class__.__name__, self.message
        )


class InvalidSignatureError(BaseError):
    def __init__(self, message='-'):
        super(InvalidSignatureError, self).__init__(message)


class LineBotApiError(BaseError):
    def __init__(self, status_code, error=None):
        """When BOT API response error, this error will be thrown.

        Args:
            status_code: http status code
            error: Error class object.
                https://devdocs.line.me/en/#error-response
        """
        super(LineBotApiError, self).__init__(error.message)

        self.status_code = status_code
        self.error = error
