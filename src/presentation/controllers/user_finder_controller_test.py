""" Class to test UserFinderController """

# from icecream import ic
from src.presentation.controllers.user_finder_controller import UserFinderController
from src.presentation.http_types.http_response import HttpResponse
from src.data.testes.user_finder import UserFinderSpy


class HttpRequestMock:
    """Class to mock HttpRequest"""

    def __init__(self) -> None:
        self.query_params = {"first_name": "John"}


def test_handle():
    """Test handle method"""
    http_request_mock = HttpRequestMock()
    use_case = UserFinderSpy()
    user_finder_controller = UserFinderController(use_case)

    response = user_finder_controller.handle(http_request_mock)

    # print()
    # ic(response)
    # ic(response.body)
    # ic(response.status_code)

    assert isinstance(response, HttpResponse)
    assert response.status_code == 200
    assert response.body["data"] is not None
