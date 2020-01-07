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

"""linebot.models.flex_message module."""

from __future__ import unicode_literals

from abc import ABCMeta

from future.utils import with_metaclass

from .actions import get_action
from .base import Base
from .send_messages import SendMessage


class FlexSendMessage(SendMessage):
    """FlexSendMessage.

    https://developers.line.biz/en/reference/messaging-api/#flex-message

    Flex Messages are messages with a customizable layout.
    You can customize the layout freely by combining multiple elements.
    """

    def __init__(self, alt_text=None, contents=None, **kwargs):
        """__init__ method.

        :param str alt_text: Alternative text
        :param contents: Flex Message container object
        :type contents: :py:class:`linebot.models.flex_message.FlexContainer`
        :param kwargs:
        """
        super(FlexSendMessage, self).__init__(**kwargs)

        self.type = 'flex'
        self.alt_text = alt_text
        self.contents = self.get_or_new_from_json_dict_with_types(
            contents, {
                'bubble': BubbleContainer,
                'carousel': CarouselContainer
            }
        )


class FlexContainer(with_metaclass(ABCMeta, Base)):
    """FlexContainer.

    https://developers.line.biz/en/reference/messaging-api/#container

    A container is the top-level structure of a Flex Message.
    """

    def __init__(self, **kwargs):
        """__init__ method.

        :param kwargs:
        """
        super(FlexContainer, self).__init__(**kwargs)

        self.type = None


class BubbleContainer(FlexContainer):
    """BubbleContainer.

    https://developers.line.biz/en/reference/messaging-api/#bubble

    This is a container that contains one message bubble.
    It can contain four blocks: header, hero, body, and footer.
    """

    def __init__(self, size=None, direction=None, header=None, hero=None,
                 body=None, footer=None, styles=None, action=None, **kwargs):
        """__init__ method.

        :param str size: The size of the bubble. `nano`, `micro`, `kilo`, `mega`, or `giga`.
        :param str direction: Text directionality and the order of components
            in horizontal boxes in the container
        :param header: Header block
        :type header: :py:class:`linebot.models.flex_message.BoxComponent`
        :param hero: Hero block
        :type hero: :py:class:`linebot.models.flex_message.ImageComponent`
            | :py:class:`linebot.models.flex_message.BoxComponent`
        :param body: Body block
        :type body: :py:class:`linebot.models.flex_message.BoxComponent`
        :param footer: Footer block
        :type footer: :py:class:`linebot.models.flex_message.BoxComponent`
        :param styles: Style of each block
        :type styles: :py:class:`linebot.models.flex_message.BubbleStyle`
        :param action: Action performed when this button is tapped
        :type action: list[T <= :py:class:`linebot.models.actions.Action`]
        :param kwargs:
        """
        super(BubbleContainer, self).__init__(**kwargs)

        self.type = 'bubble'
        self.size = size
        self.direction = direction
        self.header = self.get_or_new_from_json_dict(header, BoxComponent)
        self.hero = self.get_or_new_from_json_dict(hero, ImageComponent)
        self.body = self.get_or_new_from_json_dict(body, BoxComponent)
        self.footer = self.get_or_new_from_json_dict(footer, BoxComponent)
        self.styles = self.get_or_new_from_json_dict(styles, BubbleStyle)
        self.action = get_action(action)


class BubbleStyle(with_metaclass(ABCMeta, Base)):
    """BubbleStyle.

    https://developers.line.biz/en/reference/messaging-api/#bubble-style
    """

    def __init__(self, header=None, hero=None, body=None, footer=None, **kwargs):
        """__init__ method.

        :param header: Style of the header block
        :type header: :py:class:`linebot.models.flex_message.BlockStyle`
        :param hero: Style of the hero block
        :type hero: :py:class:`linebot.models.flex_message.BlockStyle`
        :param body: Style of the body block
        :type body: :py:class:`linebot.models.flex_message.BlockStyle`
        :param footer: Style of the footer block
        :type footer: :py:class:`linebot.models.flex_message.BlockStyle`
        :param kwargs:
        """
        super(BubbleStyle, self).__init__(**kwargs)

        self.header = self.get_or_new_from_json_dict(header, BlockStyle)
        self.hero = self.get_or_new_from_json_dict(hero, BlockStyle)
        self.body = self.get_or_new_from_json_dict(body, BlockStyle)
        self.footer = self.get_or_new_from_json_dict(footer, BlockStyle)


class BlockStyle(with_metaclass(ABCMeta, Base)):
    """BlockStyle.

    https://developers.line.biz/en/reference/messaging-api/#block-style
    """

    def __init__(self, background_color=None, separator=None, separator_color=None, **kwargs):
        """__init__ method.

        :param str background_color: Background color of the block. Use a hexadecimal color code
        :param bool separator: True to place a separator above the block
            True will be ignored for the first block in a container
            because you cannot place a separator above the first block.
            The default value is False
        :param str separator_color: Color of the separator. Use a hexadecimal color code
        :param kwargs:
        """
        super(BlockStyle, self).__init__(**kwargs)
        self.background_color = background_color
        self.separator = separator
        self.separator_color = separator_color


class CarouselContainer(FlexContainer):
    """CarouselContainer.

    https://developers.line.biz/en/reference/messaging-api/#f-carousel

    This is a container that contains multiple bubble containers, or message bubbles.
    The bubbles will be shown in order by scrolling horizontally.
    """

    def __init__(self, contents=None, **kwargs):
        """__init__ method.

        :param contents: Array of bubble containers
        :type contents: list[T <= :py:class:`linebot.models.flex_message.BubbleContainer`]
        :param kwargs:
        """
        super(CarouselContainer, self).__init__(**kwargs)

        self.type = 'carousel'

        new_contents = []
        if contents:
            for it in contents:
                new_contents.append(self.get_or_new_from_json_dict(
                    it, BubbleContainer
                ))
        self.contents = new_contents


class FlexComponent(with_metaclass(ABCMeta, Base)):
    """FlexComponent.

    https://developers.line.biz/en/reference/messaging-api/#component

    Components are objects that compose a Flex Message container.
    """

    def __init__(self, **kwargs):
        """__init__ method.

        :param kwargs:
        """
        super(FlexComponent, self).__init__(**kwargs)

        self.type = None


class BoxComponent(FlexComponent):
    """BoxComponent.

    https://developers.line.biz/en/reference/messaging-api/#box

    This is a component that defines the layout of child components.
    You can also include a box in a box.
    """

    def __init__(self,
                 layout=None,
                 contents=None,
                 background_color=None,
                 border_color=None,
                 border_width=None,
                 corner_radius=None,
                 width=None,
                 height=None,
                 flex=None,
                 spacing=None,
                 margin=None,
                 padding_all=None,
                 padding_top=None,
                 padding_bottom=None,
                 padding_start=None,
                 padding_end=None,
                 position=None,
                 offset_top=None,
                 offset_bottom=None,
                 offset_start=None,
                 offset_end=None,
                 action=None,
                 **kwargs):
        """__init__ method.

        :param str layout: The placement style of components in this box
        :param contents: Components in this box
        :type contents: list[T <= :py:class:`linebot.models.flex_message.FlexComponent`]
        :param str background_color: Background color of the block
        :param str border_color: Color of box border
        :param str border_width: Width of box border
        :param str corner_radius: Radius at the time of rounding the corners of the border
        :param str width: Width of the box
        :param str height: Height of the box
        :param float flex: The ratio of the width or height of this box within the parent box
            and the previous component in the parent box
        :param str spacing: Minimum space between components in this box
        :param str margin: Minimum space between this box
        :param str padding_all: Free space between the borders of this box and the child element
        :param str padding_top: Free space between the border at the upper end of this box
            and the upper end of the child element
        :param str padding_bottom: Free space between the border at the lower end of this box
            and the lower end of the child element
        :param str padding_start: Free space between the border at the left end of this box
            and the left end of the child element
        :param str padding_end: Free space between the border at the right end of this box
            and the right end of the child element
        :param str position: Reference position for placing this box
        :param str offset_top: The top offset
        :param str offset_bottom: The bottom offset
        :param str offset_start: The left offset
        :param str offset_end: The right offset
        :param action: Action performed when this button is tapped
        :type action: list[T <= :py:class:`linebot.models.actions.Action`]
        :param kwargs:
        """
        super(BoxComponent, self).__init__(**kwargs)
        self.type = 'box'
        self.layout = layout
        self.background_color = background_color
        self.border_color = border_color
        self.border_width = border_width
        self.corner_radius = corner_radius
        self.width = width
        self.height = height
        self.flex = flex
        self.spacing = spacing
        self.margin = margin
        self.padding_all = padding_all
        self.padding_top = padding_top
        self.padding_bottom = padding_bottom
        self.padding_start = padding_start
        self.padding_end = padding_end
        self.position = position
        self.offset_top = offset_top
        self.offset_bottom = offset_bottom
        self.offset_start = offset_start
        self.offset_end = offset_end
        self.action = get_action(action)

        new_contents = []
        if contents:
            for it in contents:
                new_contents.append(self.get_or_new_from_json_dict_with_types(
                    it, {
                        'box': BoxComponent,
                        'button': ButtonComponent,
                        'filler': FillerComponent,
                        'icon': IconComponent,
                        'image': ImageComponent,
                        'span': SpanComponent,
                        'separator': SeparatorComponent,
                        'spacer': SpacerComponent,
                        'text': TextComponent
                    }
                ))
        self.contents = new_contents


class ButtonComponent(FlexComponent):
    """ButtonComponent.

    https://developers.line.biz/en/reference/messaging-api/#button

    This component draws a button.
    When the user taps a button, a specified action is performed.
    """

    def __init__(self,
                 action=None,
                 flex=None,
                 margin=None,
                 position=None,
                 offset_top=None,
                 offset_bottom=None,
                 offset_start=None,
                 offset_end=None,
                 height=None,
                 style=None,
                 color=None,
                 gravity=None,
                 **kwargs):
        """__init__ method.

        :param action: Action performed when this button is tapped
        :type action: list[T <= :py:class:`linebot.models.actions.Action`]
        :param float flex: The ratio of the width or height of this component within the parent box
        :param str margin: Minimum space between this component
            and the previous component in the parent box
        :param str position: Reference position for placing this box
        :param str offset_top: The top offset
        :param str offset_bottom: The bottom offset
        :param str offset_start: The left offset
        :param str offset_end: The right offset
        :param str height: Height of the button
        :param str style: Style of the button
        :param str color: Character color when the style property is link.
            Background color when the style property is primary or secondary.
            Use a hexadecimal color code
        :param str gravity: Vertical alignment style
        :param kwargs:
        """
        super(ButtonComponent, self).__init__(**kwargs)
        self.type = 'button'
        self.action = get_action(action)
        self.flex = flex
        self.margin = margin
        self.position = position
        self.offset_top = offset_top
        self.offset_bottom = offset_bottom
        self.offset_start = offset_start
        self.offset_end = offset_end
        self.height = height
        self.style = style
        self.color = color
        self.gravity = gravity


class FillerComponent(FlexComponent):
    """FillerComponent.

    https://developers.line.biz/en/reference/messaging-api/#filler

    This is an invisible component to fill extra space between components.
    """

    def __init__(self, flex=None, **kwargs):
        """__init__ method.

        :param kwargs:
        """
        super(FillerComponent, self).__init__(**kwargs)
        self.type = 'filler'
        self.flex = flex


class IconComponent(FlexComponent):
    """IconComponent.

    https://developers.line.biz/en/reference/messaging-api/#icon

    This component draws an icon.
    """

    def __init__(self,
                 url=None,
                 margin=None,
                 position=None,
                 offset_top=None,
                 offset_bottom=None,
                 offset_start=None,
                 offset_end=None,
                 size=None,
                 aspect_ratio=None,
                 **kwargs):
        """__init__ method.

        :param str url: Image URL
            Protocol: HTTPS
            Image format: JPEG or PNG
        :param str margin: Minimum space between this component
            and the previous component in the parent box
        :param str position: Reference position for placing this box
        :param str offset_top: The top offset
        :param str offset_bottom: The bottom offset
        :param str offset_start: The left offset
        :param str offset_end: The right offset
        :param str size: Maximum size of the icon width
        :param str aspect_ratio: Aspect ratio of the icon
        :param kwargs:
        """
        super(IconComponent, self).__init__(**kwargs)
        self.type = 'icon'
        self.url = url
        self.margin = margin
        self.position = position
        self.offset_top = offset_top
        self.offset_bottom = offset_bottom
        self.offset_start = offset_start
        self.offset_end = offset_end
        self.size = size
        self.aspect_ratio = aspect_ratio


class ImageComponent(FlexComponent):
    """ImageComponent.

    https://developers.line.biz/en/reference/messaging-api/#f-image

    This component draws an image.
    """

    def __init__(self,
                 url=None,
                 flex=None,
                 margin=None,
                 position=None,
                 offset_top=None,
                 offset_bottom=None,
                 offset_start=None,
                 offset_end=None,
                 align=None,
                 gravity=None,
                 size=None,
                 aspect_ratio=None,
                 aspect_mode=None,
                 background_color=None,
                 action=None,
                 **kwargs):
        """__init__ method.

        :param str url: Image URL
            Protocol: HTTPS
            Image format: JPEG or PNG
        :param float flex: The ratio of the width or height of this component within the parent box
        :param str margin: Minimum space between this component
            and the previous component in the parent box
        :param str position: Reference position for placing this box
        :param str offset_top: The top offset
        :param str offset_bottom: The bottom offset
        :param str offset_start: The left offset
        :param str offset_end: The right offset
        :param str align: Horizontal alignment style
        :param str gravity: Vertical alignment style
        :param str size: Maximum size of the image width
        :param str aspect_ratio: Aspect ratio of the image
        :param str aspect_mode: Style of the image
        :param str background_color: Background color of the image. Use a hexadecimal color code.
        :param action: Action performed when this image is tapped
        :type action: list[T <= :py:class:`linebot.models.actions.Action`]
        :param kwargs:
        """
        super(ImageComponent, self).__init__(**kwargs)
        self.type = 'image'
        self.url = url
        self.flex = flex
        self.margin = margin
        self.position = position
        self.offset_top = offset_top
        self.offset_bottom = offset_bottom
        self.offset_start = offset_start
        self.offset_end = offset_end
        self.align = align
        self.gravity = gravity
        self.size = size
        self.aspect_ratio = aspect_ratio
        self.aspect_mode = aspect_mode
        self.background_color = background_color
        self.action = get_action(action)


class SeparatorComponent(FlexComponent):
    """SeparatorComponent.

    https://developers.line.biz/en/reference/messaging-api/#separator

    This component draws a separator between components in the parent box.
    """

    def __init__(self, margin=None, color=None, **kwargs):
        """__init__ method.

        :param str margin: Minimum space between this component
            and the previous component in the parent box
        :param str color: Color of the separator. Use a hexadecimal color code
        :param kwargs:
        """
        super(SeparatorComponent, self).__init__(**kwargs)
        self.type = 'separator'
        self.margin = margin
        self.color = color


class SpacerComponent(FlexComponent):
    """SpacerComponent.

    https://developers.line.biz/en/reference/messaging-api/#spacer

    This is an invisible component that places a fixed-size space
    at the beginning or end of the box
    """

    def __init__(self, size=None, **kwargs):
        """__init__ method.

        :param str size: Size of the space
        :param kwargs:
        """
        super(SpacerComponent, self).__init__(**kwargs)
        self.type = 'spacer'
        self.size = size


class SpanComponent(FlexComponent):
    """SpanComponent.

    https://developers.line.biz/en/reference/messaging-api/#span

    This component renders multiple text strings with different designs in one row.
    """

    def __init__(self,
                 text=None,
                 color=None,
                 size=None,
                 weight=None,
                 style=None,
                 decoration=None,
                 **kwargs):
        r"""__init__ method.

        :param str text: Text
        :param str color: Font color
        :param str size: Font size
        :param str weight: Font weight
        :param str style: Style of the text
        :param str decoration: Decoration of the text
        :param kwargs:
        """
        super(SpanComponent, self).__init__(**kwargs)
        self.type = 'span'
        self.text = text
        self.size = size
        self.weight = weight
        self.color = color
        self.style = style
        self.decoration = decoration


class TextComponent(FlexComponent):
    """TextComponent.

    https://developers.line.biz/en/reference/messaging-api/#f-text

    This component draws text. You can format the text.
    """

    def __init__(self,
                 text=None,
                 contents=None,
                 flex=None,
                 margin=None,
                 position=None,
                 offset_top=None,
                 offset_bottom=None,
                 offset_start=None,
                 offset_end=None,
                 size=None,
                 align=None,
                 gravity=None,
                 wrap=None,
                 max_lines=None,
                 weight=None,
                 color=None,
                 action=None,
                 style=None,
                 decoration=None,
                 **kwargs):
        r"""__init__ method.

        :param str text: Text
        :param contents: Array of spans
        :type contents: list[T <= :py:class:`linebot.models.flex_message.SpanComponent`]
        :param float flex: The ratio of the width or height of this component within the parent box
        :param str margin: Minimum space between this component
            and the previous component in the parent box
        :param str position: Reference position for placing this box
        :param str offset_top: The top offset
        :param str offset_bottom: The bottom offset
        :param str offset_start: The left offset
        :param str offset_end: The right offset
        :param str size: Font size
        :param str align: Horizontal alignment style
        :param str gravity: Vertical alignment style
        :param bool wrap: rue to wrap text. The default value is False.
            If set to True, you can use a new line character (\n) to begin on a new line.
        :param int max_lines: Max number of lines
        :param str weight: Font weight
        :param str color: Font color
        :param action: Action performed when this image is tapped
        :type action: list[T <= :py:class:`linebot.models.actions.Action`]
        :param str style: Style of the text
        :param str decoration: Decoration of the text
        :param kwargs:
        """
        super(TextComponent, self).__init__(**kwargs)
        self.type = 'text'
        self.text = text
        self.flex = flex
        self.margin = margin
        self.position = position
        self.offset_top = offset_top
        self.offset_bottom = offset_bottom
        self.offset_start = offset_start
        self.offset_end = offset_end
        self.size = size
        self.align = align
        self.gravity = gravity
        self.wrap = wrap
        self.max_lines = max_lines
        self.weight = weight
        self.color = color
        self.action = get_action(action)
        self.style = style
        self.decoration = decoration

        if contents:
            self.contents = [self.get_or_new_from_json_dict(it, SpanComponent) for it in contents]
        else:
            self.contents = None
