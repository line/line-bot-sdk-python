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

from __future__ import unicode_literals

from abc import ABCMeta

from future.utils import with_metaclass

from .actions import get_action, get_actions
from .base import Base
from .send_messages import SendMessage

class FlexSendMessage(with_metaclass(ABCMeta, Base)):
    def __init__(self, alt_text=None, contents=None, **kwargs):
        super(FlexSendMessage, self).__init__(**kwargs)

        self.type = 'flex'
        self.alt_text = alt_text
        self.contents = contents

class FlexContainer(with_metaclass(ABCMeta, Base)):
    def __init__(self, **kwargs):
        super(FlexContainer, self).__init__(**kwargs)

        self.type = None

class BubbleContainer(FlexContainer):
    def __init__(self, direction=None, styles=None, header=None, hero=None, body=None, footer=None, **kwargs):
        super(BubbleContainer, self).__init__(**kwargs)

        self.type = 'bubble'
        self.direction = direction
        self.styles = styles
        self.header = header
        self.hero = hero
        self.body = body
        self.footer = footer

class BubbleStyle(with_metaclass(ABCMeta, Base)):
    def __init__(self, header=None, hero=None, body=None, footer=None):
        super(BubbleStyle, self).__init__(**kwargs)

        self.type = 'carousel'
        self.header = header
        self.hero = hero
        self.body = body
        self.footer = footer

class BlockStyle(with_metaclass(ABCMeta, Base)):
    def __init__(self, background_color=None, separator=None, separator_color=None):
        super(BlockStyle, self).__init__(**kwargs)
        self.background_color = background_color
        self.separator = separator
        self.separator_color = separator_color

class CarouselContainer(FlexContainer):
    def __init__(self, contents=None):
        super(CarouselContainer, self).__init__(**kwargs)

        self.type = 'carousel'
        self.contents = contents

class FlexComponent(with_metaclass(ABCMeta, Base)):
    def __init__(self, **kwargs):
        super(FlexComponent, self).__init__(**kwargs)

        self.type = None

class BoxComponent(FlexComponent):
    def __init__(self, layout=None, contents=None, flex=None, spacing=None, margin=None):
        self.type = 'box'
        self.layout = layout
        self.contents = contents
        self.flex = flex
        self.spacing = spacing
        self.margin = margin

class ButtonComponent(FlexComponent):
    def __init__(self, action=None, flex=None, margin=None, height=None, style=None, color=None, gravity=None):
        self.type = 'button'
        self.action = get_action(action)
        self.flex = flex
        self.margin = margin
        self.height = height
        self.style = style
        self.color = color
        self.gravity = gravity

class FilterComponent(FlexComponent):
    def __init__(self):
        self.type = 'filter'

class IconComponent(FlexComponent):
    def __init__(self, url=None, margin=None, size=None, aspect_ratio=None, **kwargs):
        super(IconComponent, self).__init__(**kwargs)
        self.type = 'icon'
        self.url = url
        self.margin = margin
        self.size = size
        self.aspect_ratio = aspect_ratio

class ImageComponent(FlexComponent):
    def __init__(self, url=None, flex=None, margin=None, align=None, gravity=None, size=None, aspect_ratio=None, aspect_mode=None, background_color=None, action=None, **kwargs):
        super(ImageComponent, self).__init__(**kwargs)
        self.type = 'image'
        self.url = url
        self.flex = flex
        self.margin = margin
        self.align = align
        self.gravity = gravity
        self.size = size
        self.aspect_ratio = aspect_ratio
        self.aspect_mode = aspect_mode
        self.background_color = background_color
        self.action = get_action(action)

class SeparatorComponent(FlexComponent):
    def __init__(self, margin=None, color=None, **kwargs):
        super(SeparatorComponent, self).__init__(**kwargs)
        self.type = 'separator'
        self.margin = margin
        self.color = color

class SpacerComponent(FlexComponent):
    def __init__(self, size=None, **kwargs):
        super(SpacerComponent, self).__init__(**kwargs)
        self.type = 'spacer'
        self.size = size

class TextComponent(FlexComponent):
    def __init__(self, text=None, flex=None, margin=None, size=None, align=None, gravity=None, wrap=None, weight=None, color=None, action=None, **kwargs):
        super(TextComponent, self).__init__(**kwargs)
        self.type = 'text'
        self.text = text
        self.flex = flex
        self.margin = margin
        self.size = size
        self.align = align
        self.gravity = gravity
        self.wrap = wrap
        self.weight = weight
        self.color = color
        self.action = get_action(action)

