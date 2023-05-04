# coding: utf-8

"""
    LINE Messaging API

    This document describes LINE Messaging API.  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import re  # noqa: F401
import io

from pydantic import validate_arguments, ValidationError
from typing_extensions import Annotated

from pydantic import Field, StrictBytes, StrictStr

from typing import Optional, Union

from linebot.messaging.models.get_message_content_transcoding_response import GetMessageContentTranscodingResponse

from linebot.messaging.api_client import ApiClient
from linebot.messaging.api_response import ApiResponse
from linebot.messaging.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class MessagingApiBlobApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def get_message_content(self, message_id : Annotated[StrictStr, Field(..., description="Message ID of video or audio")], **kwargs) -> bytearray:  # noqa: E501
        """get_message_content  # noqa: E501

        Download image, video, and audio data sent from users.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_message_content(message_id, async_req=True)
        >>> result = thread.get()

        :param message_id: Message ID of video or audio (required)
        :type message_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: bytearray
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the get_message_content_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.get_message_content_with_http_info(message_id, **kwargs)  # noqa: E501

    @validate_arguments
    def get_message_content_with_http_info(self, message_id : Annotated[StrictStr, Field(..., description="Message ID of video or audio")], **kwargs) -> ApiResponse:  # noqa: E501
        """get_message_content  # noqa: E501

        Download image, video, and audio data sent from users.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_message_content_with_http_info(message_id, async_req=True)
        >>> result = thread.get()

        :param message_id: Message ID of video or audio (required)
        :type message_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(bytearray, status_code(int), headers(HTTPHeaderDict))
        """

        _hosts = [
            'https://api-data.line.me'
        ]
        _host = _hosts[0]
        if kwargs.get('_host_index'):
            _host_index = int(kwargs.get('_host_index'))
            if _host_index < 0 or _host_index >= len(_hosts):
                raise ApiValueError(
                    "Invalid host index. Must be 0 <= index < %s"
                    % len(_host)
                )
            _host = _hosts[_host_index]
        _params = locals()

        _all_params = [
            'message_id'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params and _key != "_host_index":
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_message_content" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['message_id']:
            _path_params['messageId'] = _params['message_id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # authentication setting
        _auth_settings = ['Bearer']  # noqa: E501

        _response_types_map = {
            '200': "bytearray",
        }

        return self.api_client.call_api(
            '/v2/bot/message/{messageId}/content', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            _host=_host,
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def get_message_content_preview(self, message_id : Annotated[StrictStr, Field(..., description="Message ID of image or video")], **kwargs) -> bytearray:  # noqa: E501
        """get_message_content_preview  # noqa: E501

        Get a preview image of the image or video  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_message_content_preview(message_id, async_req=True)
        >>> result = thread.get()

        :param message_id: Message ID of image or video (required)
        :type message_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: bytearray
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the get_message_content_preview_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.get_message_content_preview_with_http_info(message_id, **kwargs)  # noqa: E501

    @validate_arguments
    def get_message_content_preview_with_http_info(self, message_id : Annotated[StrictStr, Field(..., description="Message ID of image or video")], **kwargs) -> ApiResponse:  # noqa: E501
        """get_message_content_preview  # noqa: E501

        Get a preview image of the image or video  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_message_content_preview_with_http_info(message_id, async_req=True)
        >>> result = thread.get()

        :param message_id: Message ID of image or video (required)
        :type message_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(bytearray, status_code(int), headers(HTTPHeaderDict))
        """

        _hosts = [
            'https://api-data.line.me'
        ]
        _host = _hosts[0]
        if kwargs.get('_host_index'):
            _host_index = int(kwargs.get('_host_index'))
            if _host_index < 0 or _host_index >= len(_hosts):
                raise ApiValueError(
                    "Invalid host index. Must be 0 <= index < %s"
                    % len(_host)
                )
            _host = _hosts[_host_index]
        _params = locals()

        _all_params = [
            'message_id'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params and _key != "_host_index":
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_message_content_preview" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['message_id']:
            _path_params['messageId'] = _params['message_id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # authentication setting
        _auth_settings = ['Bearer']  # noqa: E501

        _response_types_map = {
            '200': "bytearray",
        }

        return self.api_client.call_api(
            '/v2/bot/message/{messageId}/content/preview', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            _host=_host,
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def get_message_content_transcoding_by_message_id(self, message_id : Annotated[StrictStr, Field(..., description="Message ID of video or audio")], **kwargs) -> GetMessageContentTranscodingResponse:  # noqa: E501
        """get_message_content_transcoding_by_message_id  # noqa: E501

        Verify the preparation status of a video or audio for getting  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_message_content_transcoding_by_message_id(message_id, async_req=True)
        >>> result = thread.get()

        :param message_id: Message ID of video or audio (required)
        :type message_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: GetMessageContentTranscodingResponse
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the get_message_content_transcoding_by_message_id_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.get_message_content_transcoding_by_message_id_with_http_info(message_id, **kwargs)  # noqa: E501

    @validate_arguments
    def get_message_content_transcoding_by_message_id_with_http_info(self, message_id : Annotated[StrictStr, Field(..., description="Message ID of video or audio")], **kwargs) -> ApiResponse:  # noqa: E501
        """get_message_content_transcoding_by_message_id  # noqa: E501

        Verify the preparation status of a video or audio for getting  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_message_content_transcoding_by_message_id_with_http_info(message_id, async_req=True)
        >>> result = thread.get()

        :param message_id: Message ID of video or audio (required)
        :type message_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(GetMessageContentTranscodingResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _hosts = [
            'https://api-data.line.me'
        ]
        _host = _hosts[0]
        if kwargs.get('_host_index'):
            _host_index = int(kwargs.get('_host_index'))
            if _host_index < 0 or _host_index >= len(_hosts):
                raise ApiValueError(
                    "Invalid host index. Must be 0 <= index < %s"
                    % len(_host)
                )
            _host = _hosts[_host_index]
        _params = locals()

        _all_params = [
            'message_id'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params and _key != "_host_index":
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_message_content_transcoding_by_message_id" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['message_id']:
            _path_params['messageId'] = _params['message_id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['Bearer']  # noqa: E501

        _response_types_map = {
            '200': "GetMessageContentTranscodingResponse",
        }

        return self.api_client.call_api(
            '/v2/bot/message/{messageId}/content/transcoding', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            _host=_host,
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def get_rich_menu_image(self, rich_menu_id : Annotated[StrictStr, Field(..., description="ID of the rich menu with the image to be downloaded")], **kwargs) -> bytearray:  # noqa: E501
        """get_rich_menu_image  # noqa: E501

        Download rich menu image.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_rich_menu_image(rich_menu_id, async_req=True)
        >>> result = thread.get()

        :param rich_menu_id: ID of the rich menu with the image to be downloaded (required)
        :type rich_menu_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: bytearray
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the get_rich_menu_image_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.get_rich_menu_image_with_http_info(rich_menu_id, **kwargs)  # noqa: E501

    @validate_arguments
    def get_rich_menu_image_with_http_info(self, rich_menu_id : Annotated[StrictStr, Field(..., description="ID of the rich menu with the image to be downloaded")], **kwargs) -> ApiResponse:  # noqa: E501
        """get_rich_menu_image  # noqa: E501

        Download rich menu image.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_rich_menu_image_with_http_info(rich_menu_id, async_req=True)
        >>> result = thread.get()

        :param rich_menu_id: ID of the rich menu with the image to be downloaded (required)
        :type rich_menu_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(bytearray, status_code(int), headers(HTTPHeaderDict))
        """

        _hosts = [
            'https://api-data.line.me'
        ]
        _host = _hosts[0]
        if kwargs.get('_host_index'):
            _host_index = int(kwargs.get('_host_index'))
            if _host_index < 0 or _host_index >= len(_hosts):
                raise ApiValueError(
                    "Invalid host index. Must be 0 <= index < %s"
                    % len(_host)
                )
            _host = _hosts[_host_index]
        _params = locals()

        _all_params = [
            'rich_menu_id'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params and _key != "_host_index":
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_rich_menu_image" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['rich_menu_id']:
            _path_params['richMenuId'] = _params['rich_menu_id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # authentication setting
        _auth_settings = ['Bearer']  # noqa: E501

        _response_types_map = {
            '200': "bytearray",
        }

        return self.api_client.call_api(
            '/v2/bot/richmenu/{richMenuId}/content', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            _host=_host,
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def set_rich_menu_image(self, rich_menu_id : Annotated[StrictStr, Field(..., description="The ID of the rich menu to attach the image to")], body : Optional[Union[StrictBytes, StrictStr]] = None, **kwargs) -> None:  # noqa: E501
        """set_rich_menu_image  # noqa: E501

        Upload rich menu image  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.set_rich_menu_image(rich_menu_id, body, async_req=True)
        >>> result = thread.get()

        :param rich_menu_id: The ID of the rich menu to attach the image to (required)
        :type rich_menu_id: str
        :param body:
        :type body: bytearray
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the set_rich_menu_image_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.set_rich_menu_image_with_http_info(rich_menu_id, body, **kwargs)  # noqa: E501

    @validate_arguments
    def set_rich_menu_image_with_http_info(self, rich_menu_id : Annotated[StrictStr, Field(..., description="The ID of the rich menu to attach the image to")], body : Optional[Union[StrictBytes, StrictStr]] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """set_rich_menu_image  # noqa: E501

        Upload rich menu image  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.set_rich_menu_image_with_http_info(rich_menu_id, body, async_req=True)
        >>> result = thread.get()

        :param rich_menu_id: The ID of the rich menu to attach the image to (required)
        :type rich_menu_id: str
        :param body:
        :type body: bytearray
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """

        _hosts = [
            'https://api-data.line.me'
        ]
        _host = _hosts[0]
        if kwargs.get('_host_index'):
            _host_index = int(kwargs.get('_host_index'))
            if _host_index < 0 or _host_index >= len(_hosts):
                raise ApiValueError(
                    "Invalid host index. Must be 0 <= index < %s"
                    % len(_host)
                )
            _host = _hosts[_host_index]
        _params = locals()

        _all_params = [
            'rich_menu_id',
            'body'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params and _key != "_host_index":
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method set_rich_menu_image" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['rich_menu_id']:
            _path_params['richMenuId'] = _params['rich_menu_id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['body'] is not None:
            _body_params = _params['body']
            # convert to byte array if the input is a file name (str)
            if isinstance(_body_params, str):
                with io.open(_body_params, "rb") as _fp:
                   _body_params_from_file = _fp.read()
                _body_params = _body_params_from_file

        # authentication setting
        _auth_settings = ['Bearer']  # noqa: E501

        _response_types_map = {}

        return self.api_client.call_api(
            '/v2/bot/richmenu/{richMenuId}/content', 'POST',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            _host=_host,
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))
