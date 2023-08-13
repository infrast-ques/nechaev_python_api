from src.module.api.requests.implementation.HTTPMethod import HTTPMethod


class TRequest:
    def __init__(self,
                 response_type: type,
                 method: HTTPMethod,
                 endpoint: str,
                 headers: dict = None,
                 cookies: dict = None,
                 content_type: str = None,
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
