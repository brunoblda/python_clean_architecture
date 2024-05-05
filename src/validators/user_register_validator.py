""" This module contains the user_register_validator function. """

from cerberus import Validator
from src.errors.types import HttpUnprocessableEntityError


def user_register_validator(request: any):
    """Function to validate the user registration request."""

    body_validator = Validator(
        {
            "first_name": {"type": "string", "required": True, "empty": False},
            "last_name": {"type": "string", "required": True, "empty": False},
            "age": {"type": "integer", "required": True, "empty": False},
        }
    )

    response = body_validator.validate(request.json)

    if response is False:
        raise HttpUnprocessableEntityError(body_validator.errors)
