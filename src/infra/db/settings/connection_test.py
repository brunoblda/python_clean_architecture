""" Test cases for the database connection settings. """

# from icecream import ic
# from sqlalchemy import text
import pytest
from .connection import DBConnectionHandler


@pytest.mark.skip(reason="Sensive test")
def test_create_database_engine():
    """Test create database engine"""
    db_connection_handle = DBConnectionHandler()

    engine = db_connection_handle.get_engine()
    # print()
    # ic(engine)

    assert engine is not None

    # Insert test data

    # conn = engine.connect()
    # conn.execute(
    #     text("INSERT INTO users (first_name, last_name, age) VALUES ('ola', 'mundo', 20)")
    # )
    # conn.commit()
