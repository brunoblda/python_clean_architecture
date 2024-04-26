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
    ic(response)

    assert repo.select_user_attributes["first_name"] == first_name
    assert response["type"] == "Users"
    assert response["count"] == len(response["attributes"])
    assert response["attributes"] != []
