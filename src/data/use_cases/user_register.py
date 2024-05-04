# pylint: disable=W0719
# pylint: disable=R0903

from typing import Dict
from src.domain.use_cases.user_register import UserRegister as UserRegisterInterface
from src.data.interfaces.users_repository import UsersRepositoryInterface
from src.errors.types import HttpBadRequestError


class UserRegister(UserRegisterInterface):
    """Class UserRegister"""

    def __init__(self, users_repository: UsersRepositoryInterface) -> None:
        self.__users_repository = users_repository

    def register(self, first_name: str, last_name: str, age: int) -> Dict:
        """Register user by first_name, last_name and age"""

        self.__validate_name(first_name)
        self.__validate_name(last_name)

        self.__registry_user_informations(first_name, last_name, age)

        response = self.__format_response(first_name, last_name, age)

        return response

    @classmethod
    def __validate_name(cls, name: str) -> None:
        """Validate name"""
        if not name.isalpha():
            raise HttpBadRequestError("Nome invalido para o cadastro")

        if len(name) > 18:
            raise HttpBadRequestError("Nome muito grande para o cadastro")

    def __registry_user_informations(
        self, first_name: str, last_name: str, age: int
    ) -> None:
        self.__users_repository.insert_user(first_name, last_name, age)

    @classmethod
    def __format_response(cls, first_name: str, last_name: str, age: int) -> Dict:
        """Format response"""

        response = {
            "type": "Users",
            "count": 1,
            "attributes": {
                "first_name": first_name,
                "last_name": last_name,
                "age": age,
            },
        }

        return response
