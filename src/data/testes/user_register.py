""" Spy test para UserRegister """

from typing import Dict


class UserRegisterSpy:
    """Spy class para UserRegister"""

    def __init__(self) -> None:
        self.register_attributes = {}

    def register(self, first_name: str, last_name: str, age: int) -> Dict:
        """Spy para o metodo find"""
        self.register_attributes["first_name"] = first_name
        self.register_attributes["last_name"] = last_name
        self.register_attributes["age"] = age

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
