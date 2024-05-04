from src.infra.db.tests.users_repository import UsersRepositorySpy
from .user_register import UserRegister


def test_register():
    first_name = "ola"
    last_name = "aqui"
    age = 3

    repo = UsersRepositorySpy()
    user_register = UserRegister(repo)

    response = user_register.register(first_name, last_name, age)

    # print()
    # ic(repo.insert_user_attributes)
    assert response["attributes"]["first_name"] == first_name
    assert response["attributes"]["last_name"] == last_name
    assert response["attributes"]["age"] == age

    assert response["type"] == "Users"
    assert response["count"] == 1
    assert response["attributes"]


def test_register_first_name_error():

    first_name = "ola242342423423"
    last_name = "aqui"
    age = 3

    repo = UsersRepositorySpy()
    user_register = UserRegister(repo)

    try:
        user_register.register(first_name, last_name, age)
        assert False
    except Exception as exception:
        assert str(exception) == "Nome invalido para a busca"
