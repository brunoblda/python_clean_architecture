# pylint: disable=W0221
"""Repository manipulation of users table."""

from typing import List
from src.data.interfaces.users_repository import UsersRepositoryInterface
from src.infra.db.settings.connection import DBConnectionHandler
from src.infra.db.entities.users import Users as UsersEntity
from src.domain.models.users import Users


class UsersRepository(UsersRepositoryInterface):
    """Users Repository Class"""

    @classmethod
    def insert_user(cls, first_name: str, last_name: str, age: int) -> None:
        """Insert data in users table"""
        with DBConnectionHandler() as database:
            try:
                new_registry = UsersEntity(
                    first_name=first_name, last_name=last_name, age=age
                )
                database.session.add(new_registry)
                database.session.commit()

            except Exception as exception:
                database.session.rollback()
                raise exception

    @classmethod
    def select_user(cls, first_name: str) -> List[Users]:
        """Select data in users table, by first_name."""
        with DBConnectionHandler() as database:
            try:
                users = (
                    database.session.query(UsersEntity)
                    .filter(UsersEntity.first_name == first_name)
                    .all()
                )
                return users
            except Exception as exception:
                database.session.rollback()
                raise exception
