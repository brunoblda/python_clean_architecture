# pylint: disable=W0719
# pylint: disable=R0903

from typing import Dict
from src.domain.use_cases.user_finder import UserFinder as UserFinderInterface
from src.data.interfaces.users_repository import UsersRepositoryInterface


class UserFinder(UserFinderInterface):
    """Class UserFinder"""

    def __init__(self, users_repository: UsersRepositoryInterface) -> None:
        self.__users_repository = users_repository

    def find(self, first_name: str) -> Dict:
        """Find user by first_name"""
        if not first_name.isalpha():
            raise Exception("Nome invalido para a busca")

        if len(first_name) > 18:
            raise Exception("Nome muito grande para a busca")

        users = self.__users_repository.select_user(first_name)
        if users == []:
            raise Exception("Usuario não encontrado")

        response = {"type": "Users", "count": len(users), "attributes": users}

        return response


# first_name não podem ter numeros
# first_name não pode ter mais de 18 letras
# retorna erro caso nao encontre o usuario
# formatar a reposta
