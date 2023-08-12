import logging
from urllib.parse import urlunparse, urlunsplit

import requests

from src.module.api.requests.Request import TRequest
from src.module.deserializer.deserialize import deserialize


class ApiClient:
    def __init__(self,
                 host: str,
                 scheme: str = 'https',
                 header_dict: dict = None,
                 cookies: dict = None):
        self.response = None
        self.response_body = None
        self.scheme = scheme
        self.host = host
        self.headers = header_dict
        self.cookies = cookies

    logging.basicConfig(level=logging.NOTSET)

    def send_request(self, request: TRequest):

        headers = {}
        if self.headers is not None:
            headers.update(self.headers)
        if request.headers is not None:
            headers.update(request.headers)
        if request.content_type is not None:
            headers.update(request.content_type)

        cookies = {}
        if self.cookies is not None:
            cookies.update(self.cookies)
        if request.cookies is not None:
            cookies.update(request.cookies)

        url = f"{self.scheme}://{self.host}{request.endpoint}"

        self.response = requests.request(request.method.value,
                                         url=url,
                                         headers=headers,
                                         cookies=cookies,
                                         params=request.params,
                                         json=request.body)
        print(self.response)
        self.response_body = deserialize(request.response_type, self.response.json())
        return self
