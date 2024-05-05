""" This module contains the user_finder_validator function. """

from cerberus import Validator
from src.errors.types import HttpUnprocessableEntityError


def user_finder_validator(request: any):
    """Function to validate the user finder request."""

    query_validator = Validator(
        {
            "first_name": {"type": "string", "required": True, "empty": False},
        }
    )

    response = query_validator.validate(request.args)

    if response is False:
        raise HttpUnprocessableEntityError(query_validator.errors)
