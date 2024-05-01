"""Repository manipulation of users table."""

from typing import List
from src.domain.models.users import Users
from src.data.interfaces.users_repository import UsersRepositoryInterface


class UsersRepositorySpy(UsersRepositoryInterface):
    """Users Repository Class"""

    def __init__(self) -> None:
        self.insert_user_attributes = {}
        self.select_user_attributes = {}

    def insert_user(self, first_name: str, last_name: str, age: int) -> None:
        """Insert data in users table"""
        self.insert_user_attributes["first_name"] = first_name
        self.insert_user_attributes["last_name"] = last_name
        self.insert_user_attributes["age"] = age

    def select_user(self, first_name: str) -> List[Users]:
        """Select data in users table, by first_name."""
        self.select_user_attributes["first_name"] = first_name
        return [Users(4, first_name, "last", 43), Users(5, first_name, "minder", 39)]
