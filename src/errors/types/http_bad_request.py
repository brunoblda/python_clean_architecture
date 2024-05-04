""" This module contains the httpBadRequestError class. """


class HttpBadRequestError(Exception):
    """Class for BadRequest error."""

    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message
        self.name = "BadRequest"
        self.status_code = 400
