""" Users Repository Interface Module """

from abc import ABC, abstractmethod
from typing import List
from src.domain.models.users import Users


class UsersRepositoryInterface(ABC):
    """Users Repository Interface"""

    @abstractmethod
    def insert_user(self, first_name: str, last_name: str, age: int) -> None:
        """Insert data in users table"""
        raise NotImplementedError

    @abstractmethod
    def select_user(self, first_name: str) -> List[Users]:
        """Select data in users table, by first_name"""
        raise NotImplementedError
