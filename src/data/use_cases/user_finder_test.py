""" Test cases for the UserFinder use case. """

from icecream import ic
from src.infra.db.tests.users_repository import UsersRepositorySpy
from .user_finder import UserFinder


def test_find():
    """Testing the find method."""
    first_name = "meunome"

    repo = UsersRepositorySpy()
    user_finder = UserFinder(repo)
    response = user_finder.find(first_name)

    print()
    ic(repo.select_user_attributes)

    print()
    ic(response)

    assert repo.select_user_attributes["first_name"] == first_name

    assert response["type"] == "Users"
    assert response["count"] == len(response["attributes"])
    assert response["attributes"]


def test_find_error_in_valid_name():
    """Testing the find error of an invalid name."""
    first_name = "meunome123"

    repo = UsersRepositorySpy()
    user_finder = UserFinder(repo)

    try:
        user_finder.find(first_name)
        assert False
        # Para que o first_name seja invalido
    except Exception as exception:
        assert str(exception) == "Nome invalido para a busca"


def test_find_error_in_too_long_name():
    """Testing the find method of a too long nome."""
    first_name = "meunomesdfsjfjskjfksjsdskjfskjskjsdfjsfjsk"

    repo = UsersRepositorySpy()
    user_finder = UserFinder(repo)

    try:
        user_finder.find(first_name)
        assert False
        # Para que o first_name seja invalido
    except Exception as exception:
        assert str(exception) == "Nome muito grande para a busca"


def test_find_error_user_not_found():
    """Testing the find method with invalid name."""

    class UsersRepositoryError(UsersRepositorySpy):
        """Class UsersRepositoryError"""

        def select_user(self, first_name: str):
            """Select user method"""
            return []

    first_name = "meunome"

    repo = UsersRepositoryError()
    user_finder = UserFinder(repo)

    try:
        user_finder.find(first_name)
        assert False
        # Para que o first_name seja invalido
    except Exception as exception:
        assert str(exception) == "Usuario não encontrado"
