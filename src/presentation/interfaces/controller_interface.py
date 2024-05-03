""" Controller Interface """

from abc import ABC, abstractmethod
from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse


class ControllerInterface(ABC):
    """Controller Interface"""

    @abstractmethod
    def handle(self, http_request: HttpRequest) -> HttpResponse:
        """Method to handle the http_request"""
        raise NotImplementedError("Method not implemented")
