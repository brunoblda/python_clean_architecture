# pylint: disable=too-few-public-methods

""" Class to test UserRegisterController """

# from icecream import ic
from src.presentation.controllers.user_register_controller import UserRegisterController
from src.presentation.http_types.http_response import HttpResponse
from src.data.testes.user_register import UserRegisterSpy


class HttpRequestMock:
    """Class to mock HttpRequest"""

    def __init__(self) -> None:
        self.body = {"first_name": "John", "last_name": "Doe", "age": 43}


def test_handle():
    """Test handle method"""
    http_request_mock = HttpRequestMock()
    use_case = UserRegisterSpy()
    user_register_controller = UserRegisterController(use_case)

    response = user_register_controller.handle(http_request_mock)

    # print()
    # ic(response)
    # ic(response.body)
    # ic(response.status_code)

    assert isinstance(response, HttpResponse)
    assert response.status_code == 200
    assert response.body["data"] is not None
