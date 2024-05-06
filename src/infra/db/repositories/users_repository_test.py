# pylint: disable=protected-access
"""Test for UsersRepository"""

import pytest
from sqlalchemy import text
from icecream import ic
from src.infra.db.settings.connection import DBConnectionHandler
from .users_repository import UsersRepository


@pytest.mark.skip(reason="Sensive test")
def test_insert_user():
    # teste de integracao com o banco de dados
    """Test insert_user in UsersRepository"""

    db_connection_handler = DBConnectionHandler()
    db_connection_handler.__connection_string = (
        "mysql+pymysql://root@127.0.0.1:3306/clean_database"
    )
    connection = db_connection_handler.get_engine().connect()

    mocked_first_name = "first_i"
    mocked_last_name = "last_i"
    mocked_age = 40

    users_repository = UsersRepository()
    users_repository.insert_user(mocked_first_name, mocked_last_name, mocked_age)

    sql_insert = f"""
        SELECT * FROM users
        WHERE first_name = '{mocked_first_name}'
        AND last_name = '{mocked_last_name}'
        AND age = {mocked_age}
        """
    response = connection.execute(text(sql_insert))
    registry = response.fetchall()[-1]

    assert registry.first_name == mocked_first_name
    assert registry.last_name == mocked_last_name
    assert registry.age == mocked_age

    # print()
    # ic(registry)

    sql_delete = f"""
        DELETE FROM users
        WHERE id = {registry.id}
        """

    connection.execute(text(sql_delete))
    connection.commit()


@pytest.mark.skip(reason="Sensive test")
def test_select_user():
    # teste de integracao com o banco de dados
    """Test select_user in UsersRepository"""

    db_connection_handler = DBConnectionHandler()
    db_connection_handler.__connection_string = (
        "mysql+pymysql://root@127.0.0.1:3306/clean_database"
    )
    connection = db_connection_handler.get_engine().connect()

    mocked_first_name = "first_s"
    mocked_last_name = "last_s"
    mocked_age = 50

    sql_insert = f"""
        INSERT INTO users (first_name, last_name, age)
        VALUES ('{mocked_first_name}', '{mocked_last_name}', {mocked_age})
        """
    connection.execute(text(sql_insert))
    connection.commit()

    users_repository = UsersRepository()
    response = users_repository.select_user(mocked_first_name)

    print()
    ic(response)

    assert response[-1].first_name == mocked_first_name
    assert response[-1].last_name == mocked_last_name
    assert response[-1].age == mocked_age

    # print()
    # ic(response)

    sql_delete = f"""
        DELETE FROM users
        WHERE id = {response[0].id}
        """

    connection.execute(text(sql_delete))
    connection.commit()
