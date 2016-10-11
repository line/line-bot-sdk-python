# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import base64
import hashlib
import hmac
import inspect
import json

from .exceptions import InvalidSignatureError
from .models.events import (
    MessageEvent,
    FollowEvent,
    UnfollowEvent,
    JoinEvent,
    LeaveEvent,
    PostbackEvent,
    BeaconEvent
)
from .utils import LOGGER, PY3


class SignatureValidator(object):
    def __init__(self, channel_secret):
        """Signature validator

        https://devdocs.line.me/en/#webhook-authentication

        Args:
            channel_secret: Channel secret
        """
        self.channel_secret = channel_secret.encode('utf-8')

    def validate(self, body, signature):
        """Check signature.

        https://devdocs.line.me/en/#webhook-authentication

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


class WebhookParser(object):
    def __init__(self, channel_secret):
        self.signature_validator = SignatureValidator(channel_secret)

    def parse(self, body, signature):
        """Parse webhook request body as text.

        Args:
            body: Webhook request body (as test)
            signature: X-Line-Signature value (as text)

        Returns: Event object list

        """

        if not self.signature_validator.validate(body, signature):
            raise InvalidSignatureError(
                'Invalid signature. signature=' + signature)

        body_json = json.loads(body)
        events = []
        for event in body_json['events']:
            event_type = event['type']
            if event_type == 'message':
                events.append(MessageEvent.new_from_json_dict(event))
            elif event_type == 'follow':
                events.append(FollowEvent.new_from_json_dict(event))
            elif event_type == 'unfollow':
                events.append(UnfollowEvent.new_from_json_dict(event))
            elif event_type == 'join':
                events.append(JoinEvent.new_from_json_dict(event))
            elif event_type == 'leave':
                events.append(LeaveEvent.new_from_json_dict(event))
            elif event_type == 'postback':
                events.append(PostbackEvent.new_from_json_dict(event))
            elif event_type == 'beacon':
                events.append(BeaconEvent.new_from_json_dict(event))
            else:
                LOGGER.warn('Unknown event type. type=' + event_type)

        return events


class WebhookHandler(object):
    def __init__(self, channel_secret):
        self.parser = WebhookParser(channel_secret)
        self._handlers = {}
        self._default = None

    def add(self, event, message=None):
        """[Decorator] Add handler method

        Args:
            event: Specify a kind of Event class
            message: If event is MessageEvent, a kind of Message class

        Returns: Decorator

        """

        def decorator(func):
            if isinstance(message, (list, tuple)):
                for it in message:
                    self.__add_handler(func, event, message=it)
            else:
                self.__add_handler(func, event, message=message)

            return func

        return decorator

    def default(self):
        """[Decorator] Default handler method

        Returns: Decorator

        """

        def decorator(func):
            self._default = func
            return func

        return decorator

    def handle(self, body, signature):
        """Handle webhook

        Args:
            body: Webhook request body (as test)
            signature: X-Line-Signature value (as text)
        """

        events = self.parser.parse(body, signature)

        for event in events:
            func = None
            key = None

            if isinstance(event, MessageEvent):
                key = self.__get_handler_key(
                    event.__class__, event.message.__class__)
                func = self._handlers.get(key, None)

            if func is None:
                key = self.__get_handler_key(event.__class__)
                func = self._handlers.get(key, None)

            if func is None:
                func = self._default

            if func is None:
                LOGGER.info('No handler of ' + key + ' and no default handler')
            else:
                args_count = self.__get_args_count(func)
                if args_count == 0:
                    func()
                else:
                    func(event)

    def __add_handler(self, func, event, message=None):
        key = self.__get_handler_key(event, message=message)
        self._handlers[key] = func

    @staticmethod
    def __get_args_count(func):
        if PY3:
            arg_spec = inspect.getfullargspec(func)
            return len(arg_spec.args)
        else:
            arg_spec = inspect.getargspec(func)
            return len(arg_spec.args)

    @staticmethod
    def __get_handler_key(event, message=None):
        if message is None:
            return event.__name__
        else:
            return event.__name__ + '_' + message.__name__
