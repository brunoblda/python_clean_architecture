""" Arquivo de testes para o validador de pesquisa de usuário.  """

from pytest import raises
from src.errors.types import HttpUnprocessableEntityError
from .user_finder_validator import user_finder_validator


class MockRequest:
    """Class MockRequest"""

    def __init__(self) -> None:
        self.args = None


def test_user_finder_validator():
    """Teste para o validador de pesquisa de usuário."""

    request = MockRequest()
    request.args = {"anose": "44", "first_nam": "meuNome"}

    with raises(HttpUnprocessableEntityError):
        assert isinstance(user_finder_validator(request), HttpUnprocessableEntityError)
