# pylint: disable=too-many-arguments

""" This module contains the HttpRequest class """


class HttpRequest:
    """HttpRequest class"""

    def __init__(
        self,
        headers=None,
        body=None,
        query_params=None,
        path_params=None,
        url=None,
        ipv4=None,
    ) -> None:
        self.headers = headers
        self.body = body
        self.query_params = query_params
        self.path_params = path_params
        self.url = url
        self.ipv4 = ipv4
