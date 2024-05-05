""" Module for HttpUnprocessableEntityError custom error """


class HttpUnprocessableEntityError(Exception):
    """Class for UnprocessableEntity error."""

    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message
        self.name = "UnprocessableEntity"
        self.status_code = 422
