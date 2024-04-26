"""Connection module"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DBConnectionHandler:
    """DBConnectionHandler class"""

    def __init__(self) -> None:
        self.__connection_string = "mysql+pymysql://root@127.0.0.1:3306/clean_database"
        self.__engine = self.__create_database_engine()
        self.session = None

    def __create_database_engine(self):
        """Create the database engine"""
        engine = create_engine(self.__connection_string)
        return engine

    def get_engine(self):
        """Return the engine connection"""
        return self.__engine

    def __enter__(self):
        session_make = sessionmaker(bind=self.__engine)
        self.session = session_make()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
