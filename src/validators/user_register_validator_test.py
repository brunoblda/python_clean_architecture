""" Testes para o validador de registro de usuário. """

from pytest import raises
from src.errors.types import HttpUnprocessableEntityError
from .user_register_validator import user_register_validator


class MockRequest:
    """Class MockRequest"""

    def __init__(self) -> None:
        self.json = None


def test_user_register_validator():
    """Teste para o validador de registro de usuário."""

    request = MockRequest()
    request.json = {"first_nam": "meuNome", "last_name": 33, "age": "44"}

    with raises(HttpUnprocessableEntityError):
        assert isinstance(
            user_register_validator(request), HttpUnprocessableEntityError
        )
