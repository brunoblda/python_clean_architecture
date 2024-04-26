""" Users model. """

# pylint: disable=redefined-builtin
# pylint: disable=invalid-name
# pylint: disable=too-few-public-methods


class Users:
    """Users model"""

    def __init__(self, id: int, first_name: str, last_name: str, age: int) -> None:
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __repr__(self) -> str:
        return f"User: [id: {self.id}, first_name: {self.first_name}, last_name: {self.last_name}, age: {self.age}]"
