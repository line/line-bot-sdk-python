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
from typing import overload, Optional, Union, Awaitable

from pydantic import Field, StrictBool, StrictBytes, StrictInt, StrictStr, constr

from typing import Optional, Union

from linebot.audience.models.create_audience_group_response import CreateAudienceGroupResponse

from linebot.audience.async_api_client import AsyncApiClient
from linebot.audience.api_response import ApiResponse
from linebot.audience.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class AsyncManageAudienceBlobApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = AsyncApiClient.get_default()
        self.api_client = api_client

    @overload
    async def add_user_ids_to_audience(self, file : Annotated[Union[StrictBytes, StrictStr], Field(..., description="A text file with one user ID or IFA entered per line. Specify text/plain as Content-Type. Max file number: 1 Max number: 1,500,000 ")], audience_group_id : Annotated[Optional[StrictInt], Field(description="The audience ID.")] = None, upload_description : Annotated[Optional[StrictStr], Field(description="The description to register with the job")] = None, **kwargs) -> None:  # noqa: E501
        ...

    @overload
    def add_user_ids_to_audience(self, file : Annotated[Union[StrictBytes, StrictStr], Field(..., description="A text file with one user ID or IFA entered per line. Specify text/plain as Content-Type. Max file number: 1 Max number: 1,500,000 ")], audience_group_id : Annotated[Optional[StrictInt], Field(description="The audience ID.")] = None, upload_description : Annotated[Optional[StrictStr], Field(description="The description to register with the job")] = None, async_req: Optional[bool]=True, **kwargs) -> None:  # noqa: E501
        ...

    @validate_arguments
    def add_user_ids_to_audience(self, file : Annotated[Union[StrictBytes, StrictStr], Field(..., description="A text file with one user ID or IFA entered per line. Specify text/plain as Content-Type. Max file number: 1 Max number: 1,500,000 ")], audience_group_id : Annotated[Optional[StrictInt], Field(description="The audience ID.")] = None, upload_description : Annotated[Optional[StrictStr], Field(description="The description to register with the job")] = None, async_req: Optional[bool]=None, **kwargs) -> Union[None, Awaitable[None]]:  # noqa: E501
        """add_user_ids_to_audience  # noqa: E501

        Add user IDs or Identifiers for Advertisers (IFAs) to an audience for uploading user IDs (by file).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.add_user_ids_to_audience(file, audience_group_id, upload_description, async_req=True)
        >>> result = thread.get()

        :param file: A text file with one user ID or IFA entered per line. Specify text/plain as Content-Type. Max file number: 1 Max number: 1,500,000  (required)
        :type file: bytearray
        :param audience_group_id: The audience ID.
        :type audience_group_id: int
        :param upload_description: The description to register with the job
        :type upload_description: str
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
            raise ValueError("Error! Please call the add_user_ids_to_audience_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        if async_req is not None:
            kwargs['async_req'] = async_req
        return self.add_user_ids_to_audience_with_http_info(file, audience_group_id, upload_description, **kwargs)  # noqa: E501

    @validate_arguments
    def add_user_ids_to_audience_with_http_info(self, file : Annotated[Union[StrictBytes, StrictStr], Field(..., description="A text file with one user ID or IFA entered per line. Specify text/plain as Content-Type. Max file number: 1 Max number: 1,500,000 ")], audience_group_id : Annotated[Optional[StrictInt], Field(description="The audience ID.")] = None, upload_description : Annotated[Optional[StrictStr], Field(description="The description to register with the job")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """add_user_ids_to_audience  # noqa: E501

        Add user IDs or Identifiers for Advertisers (IFAs) to an audience for uploading user IDs (by file).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.add_user_ids_to_audience_with_http_info(file, audience_group_id, upload_description, async_req=True)
        >>> result = thread.get()

        :param file: A text file with one user ID or IFA entered per line. Specify text/plain as Content-Type. Max file number: 1 Max number: 1,500,000  (required)
        :type file: bytearray
        :param audience_group_id: The audience ID.
        :type audience_group_id: int
        :param upload_description: The description to register with the job
        :type upload_description: str
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
            'file',
            'audience_group_id',
            'upload_description'
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
                    " to method add_user_ids_to_audience" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        if _params['audience_group_id']:
            _form_params.append(('audienceGroupId', _params['audience_group_id']))

        if _params['upload_description']:
            _form_params.append(('uploadDescription', _params['upload_description']))

        if _params['file']:
            _files['file'] = _params['file']

        # process the body parameter
        _body_params = None
        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['multipart/form-data']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = ['Bearer']  # noqa: E501

        _response_types_map = {}

        return self.api_client.call_api(
            '/v2/bot/audienceGroup/upload/byFile', 'PUT',
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

    @overload
    async def create_audience_for_uploading_user_ids(self, file : Annotated[Union[StrictBytes, StrictStr], Field(..., description="A text file with one user ID or IFA entered per line. Specify text/plain as Content-Type. Max file number: 1 Max number: 1,500,000 ")], description : Annotated[Optional[constr(strict=True, max_length=120)], Field(description="The audience's name. This is case-insensitive, meaning AUDIENCE and audience are considered identical. Max character limit: 120 ")] = None, is_ifa_audience : Annotated[Optional[StrictBool], Field(description="To specify recipients by IFAs: set `true`. To specify recipients by user IDs: set `false` or omit isIfaAudience property. ")] = None, upload_description : Annotated[Optional[StrictStr], Field(description="The description to register for the job (in `jobs[].description`). ")] = None, **kwargs) -> CreateAudienceGroupResponse:  # noqa: E501
        ...

    @overload
    def create_audience_for_uploading_user_ids(self, file : Annotated[Union[StrictBytes, StrictStr], Field(..., description="A text file with one user ID or IFA entered per line. Specify text/plain as Content-Type. Max file number: 1 Max number: 1,500,000 ")], description : Annotated[Optional[constr(strict=True, max_length=120)], Field(description="The audience's name. This is case-insensitive, meaning AUDIENCE and audience are considered identical. Max character limit: 120 ")] = None, is_ifa_audience : Annotated[Optional[StrictBool], Field(description="To specify recipients by IFAs: set `true`. To specify recipients by user IDs: set `false` or omit isIfaAudience property. ")] = None, upload_description : Annotated[Optional[StrictStr], Field(description="The description to register for the job (in `jobs[].description`). ")] = None, async_req: Optional[bool]=True, **kwargs) -> CreateAudienceGroupResponse:  # noqa: E501
        ...

    @validate_arguments
    def create_audience_for_uploading_user_ids(self, file : Annotated[Union[StrictBytes, StrictStr], Field(..., description="A text file with one user ID or IFA entered per line. Specify text/plain as Content-Type. Max file number: 1 Max number: 1,500,000 ")], description : Annotated[Optional[constr(strict=True, max_length=120)], Field(description="The audience's name. This is case-insensitive, meaning AUDIENCE and audience are considered identical. Max character limit: 120 ")] = None, is_ifa_audience : Annotated[Optional[StrictBool], Field(description="To specify recipients by IFAs: set `true`. To specify recipients by user IDs: set `false` or omit isIfaAudience property. ")] = None, upload_description : Annotated[Optional[StrictStr], Field(description="The description to register for the job (in `jobs[].description`). ")] = None, async_req: Optional[bool]=None, **kwargs) -> Union[CreateAudienceGroupResponse, Awaitable[CreateAudienceGroupResponse]]:  # noqa: E501
        """create_audience_for_uploading_user_ids  # noqa: E501

        Create audience for uploading user IDs (by file).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_audience_for_uploading_user_ids(file, description, is_ifa_audience, upload_description, async_req=True)
        >>> result = thread.get()

        :param file: A text file with one user ID or IFA entered per line. Specify text/plain as Content-Type. Max file number: 1 Max number: 1,500,000  (required)
        :type file: bytearray
        :param description: The audience's name. This is case-insensitive, meaning AUDIENCE and audience are considered identical. Max character limit: 120 
        :type description: str
        :param is_ifa_audience: To specify recipients by IFAs: set `true`. To specify recipients by user IDs: set `false` or omit isIfaAudience property. 
        :type is_ifa_audience: bool
        :param upload_description: The description to register for the job (in `jobs[].description`). 
        :type upload_description: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: CreateAudienceGroupResponse
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the create_audience_for_uploading_user_ids_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        if async_req is not None:
            kwargs['async_req'] = async_req
        return self.create_audience_for_uploading_user_ids_with_http_info(file, description, is_ifa_audience, upload_description, **kwargs)  # noqa: E501

    @validate_arguments
    def create_audience_for_uploading_user_ids_with_http_info(self, file : Annotated[Union[StrictBytes, StrictStr], Field(..., description="A text file with one user ID or IFA entered per line. Specify text/plain as Content-Type. Max file number: 1 Max number: 1,500,000 ")], description : Annotated[Optional[constr(strict=True, max_length=120)], Field(description="The audience's name. This is case-insensitive, meaning AUDIENCE and audience are considered identical. Max character limit: 120 ")] = None, is_ifa_audience : Annotated[Optional[StrictBool], Field(description="To specify recipients by IFAs: set `true`. To specify recipients by user IDs: set `false` or omit isIfaAudience property. ")] = None, upload_description : Annotated[Optional[StrictStr], Field(description="The description to register for the job (in `jobs[].description`). ")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """create_audience_for_uploading_user_ids  # noqa: E501

        Create audience for uploading user IDs (by file).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_audience_for_uploading_user_ids_with_http_info(file, description, is_ifa_audience, upload_description, async_req=True)
        >>> result = thread.get()

        :param file: A text file with one user ID or IFA entered per line. Specify text/plain as Content-Type. Max file number: 1 Max number: 1,500,000  (required)
        :type file: bytearray
        :param description: The audience's name. This is case-insensitive, meaning AUDIENCE and audience are considered identical. Max character limit: 120 
        :type description: str
        :param is_ifa_audience: To specify recipients by IFAs: set `true`. To specify recipients by user IDs: set `false` or omit isIfaAudience property. 
        :type is_ifa_audience: bool
        :param upload_description: The description to register for the job (in `jobs[].description`). 
        :type upload_description: str
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
        :rtype: tuple(CreateAudienceGroupResponse, status_code(int), headers(HTTPHeaderDict))
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
            'file',
            'description',
            'is_ifa_audience',
            'upload_description'
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
                    " to method create_audience_for_uploading_user_ids" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        if _params['description']:
            _form_params.append(('description', _params['description']))

        if _params['is_ifa_audience']:
            _form_params.append(('isIfaAudience', _params['is_ifa_audience']))

        if _params['upload_description']:
            _form_params.append(('uploadDescription', _params['upload_description']))

        if _params['file']:
            _files['file'] = _params['file']

        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['multipart/form-data']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = ['Bearer']  # noqa: E501

        _response_types_map = {
            '200': "CreateAudienceGroupResponse",
        }

        return self.api_client.call_api(
            '/v2/bot/audienceGroup/upload/byFile', 'POST',
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
