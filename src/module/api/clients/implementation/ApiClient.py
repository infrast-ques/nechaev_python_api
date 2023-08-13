import json
from enum import IntEnum
from typing import List

import requests
from colorama import Style

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
        self.response_typed_body = None
        self.response_dict_body = None
        self.scheme = scheme
        self.host = host
        self.headers = header_dict
        self.cookies = cookies

        Logger.init_console_logger(self)

    def send_request(self, request: TRequest):

        headers = {}
        if self.headers is not None:
            headers.update(self.headers)
        if request.headers is not None:
            headers.update(request.headers)
        if request.content_type is not None:
            headers.update({'Content-type': request.content_type})

        cookies = {}
        if self.cookies is not None:
            cookies.update(self.cookies)
        if request.cookies is not None:
            cookies.update(request.cookies)

        __url = f'{self.scheme}://{self.host}{request.endpoint}'
        __params_format = request.params

        self.__request_log(__url, request)

        self.response = requests.request(request.method.value,
                                         url=__url,
                                         headers=headers,
                                         cookies=cookies,
                                         params=request.params,
                                         json=request.body)

        self.__response_log()

        self.__verify_status_code(request.expected_status_codes)

        self.response_dict_body = self.response.json()
        self.response_typed_body = deserialize(request.response_type, self.response.json())
        return self

    def __verify_status_code(self, status_codes: List[IntEnum]):
        assert self.response.status_code in list(map(lambda code: code._value_, status_codes))

    def __request_log(self, url: str, request: TRequest):
        self.logger.info(f'\n{Style.BRIGHT}Request START: ─────────────────────────────────────── {Style.RESET_ALL}')
        self.logger.info(f'Sending url: {Style.BRIGHT}{request.method.value} - {url}{Style.RESET_ALL}')
        if request.headers is not None:
            self.logger.info(f'Sending headers:\n{Style.BRIGHT}{request.headers}{Style.RESET_ALL}')
        else:
            self.logger.info(f'Sending headers:')
        if request.cookies is not None:
            self.logger.info(f'Sending cookies:\n{Style.BRIGHT}{request.cookies}{Style.RESET_ALL}')
        else:
            self.logger.info(f'Sending cookies:')
        if request.body is not None:
            self.logger.info(f'Sending body:\n{Style.BRIGHT}{json.dumps(request.body, indent=4)}{Style.RESET_ALL}')
        else:
            self.logger.info(f'Sending body:')
        self.logger.info(f'{Style.BRIGHT}Request END: ─────────────────────────────────────── {Style.RESET_ALL}')

    def __response_log(self):
        self.logger.info(f'{Style.BRIGHT}Response START: ─────────────────────────────────────── {Style.RESET_ALL}')
        self.logger.info(f'Response code {Style.BRIGHT}{self.response.status_code}{Style.RESET_ALL}')
        self.logger.info(f'Response body:\n{Style.BRIGHT}{json.dumps(json.loads(self.response.text), indent=4)}{Style.RESET_ALL}')
        self.logger.info(f'{Style.BRIGHT}Response END: ─────────────────────────────────────── {Style.RESET_ALL}')
        self.logger.info('\n')
