import json
from enum import IntEnum
from typing import List

import requests
from colorama import Style, Fore

from src.module.api.clients.implementation.Logger import Logger
from src.module.api.requests.implementation.TRequest import TRequest
from src.module.utils.deserializer.deserialize import deserialize


class ApiClient:
    def __init__(self,
                 host: str,
                 scheme: str = 'https',
                 header_dict: dict = None,
                 cookies: dict = None):
        self.logger = None
        self.response = None
        self.typed_body = None
        self.dict_body = None
        self.scheme = scheme
        self.host = host
        self.headers = header_dict
        self.cookies = cookies

        Logger.init_console_logger(self)

    def send_request(self, request: TRequest):

        headers = self.__union_headers(request_headers=request.headers,
                                       request_content_type=request.content_type)

        cookies = self.__union_cookies(request.cookies)

        __url = f'{self.scheme}://{self.host}{request.endpoint}'

        Logger.request_log(self.logger, __url, request)

        self.response = requests.request(request.method.value,
                                         url=__url,
                                         headers=headers,
                                         cookies=cookies,
                                         params=request.params,
                                         json=request.body)

        Logger.response_log(self.logger, self.response)

        self.__verify_response_status_code(request.expected_status_codes)

        self.dict_body = self.response.json()
        self.typed_body = deserialize(request.response_type, self.response.json())
        return self

    def __union_headers(self, request_headers: dict, request_content_type: str) -> dict:
        headers = {}
        if self.headers is not None:
            headers.update(self.headers)
        if request_headers is not None:
            headers.update(request_headers)
        if request_content_type is not None:
            headers.update({'Content-type': request_content_type})
        return headers

    def __union_cookies(self, request_cookies: dict) -> dict:
        cookies = {}
        if self.cookies is not None:
            cookies.update(self.cookies)
        if request_cookies is not None:
            cookies.update(request_cookies)
        return cookies

    def __verify_response_status_code(self, status_codes: List[IntEnum]):
        assert self.response.status_code in list(map(lambda code: code._value_, status_codes))
