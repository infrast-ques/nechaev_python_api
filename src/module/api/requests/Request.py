from src.module.api.requests.HTTPMethod import HTTPMethod


class TRequest:
    def __init__(self,
                 response_type: type,
                 method: HTTPMethod,
                 endpoint: str,
                 headers: dict = None,
                 cookies: dict = None,
                 content_type: dict = None,
                 params: dict = None,
                 body: object = None):
        self.response_type = response_type
        self.method = method
        self.endpoint = endpoint
        self.headers = headers
        self.cookies = cookies
        self.content_type = content_type
        self.params = params
        self.body = body


# class Request:
#     def __init__(self, method, endpoint, header_dict=None, params=None, data=None):
#         self.method = method
#         self.endpoint = endpoint
#         self.header_dict = header_dict
#         self.params = params
#         self.data = data
import requests
