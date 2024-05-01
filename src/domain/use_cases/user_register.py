""" UserRegister use case class """

# pylint: disable=R0903

from abc import ABC, abstractmethod
from typing import Dict


class UserRegister(ABC):
    """UserRegister use case abstract class"""

    @abstractmethod
    def register(self, first_name: str, last_name: str, age: int) -> Dict:
        """Register user by first_name, last_name and age"""
        raise NotImplementedError("Method not implemented")
