# pylint: disable=W0719
# pylint: disable=R0903

from typing import Dict, List
from src.domain.use_cases.user_finder import UserFinder as UserFinderInterface
from src.data.interfaces.users_repository import UsersRepositoryInterface
from src.domain.models.users import Users
from src.errors.types import HttpBadRequestError, HttpNotFoundError


class UserFinder(UserFinderInterface):
    """Class UserFinder"""

    def __init__(self, users_repository: UsersRepositoryInterface) -> None:
        self.__users_repository = users_repository

    def find(self, first_name: str) -> Dict:
        """Find user by first_name"""

        self.__validate_name(first_name)
        users = self.__search_user(first_name)
        response = self.__format_response(users)

        return response

    @classmethod
    def __validate_name(cls, first_name: str) -> None:
        """Validate first_name"""
        if not first_name.isalpha():
            raise HttpBadRequestError("Nome invalido para a busca")

        if len(first_name) > 18:
            raise HttpBadRequestError("Nome muito grande para a busca")

    def __search_user(self, first_name: str) -> List[Users]:
        """Search user by first_name"""
        users = self.__users_repository.select_user(first_name)
        if users == []:
            raise HttpNotFoundError("Usuario não encontrado")

        return users

    @classmethod
    def __format_response(cls, users: List[Users]) -> Dict:
        """Format response"""
        attributes = []
        for user in users:
            attributes.append(
                {
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "age": user.age,
                }
            )

        response = {"type": "Users", "count": len(users), "attributes": attributes}
        return response


# first_name não podem ter numeros
# first_name não pode ter mais de 18 letras
# retorna erro caso nao encontre o usuario
# formatar a reposta
