from src.presentation.http_types.http_response import HttpResponse
from .types import HttpBadRequestError, HttpNotFoundError


def handle_error(error: Exception) -> HttpResponse:
    """Handle error"""
    if isinstance(error, (HttpBadRequestError, HttpNotFoundError)):
        # Mandar mensagem para logger falando que teve esse erro!
        return HttpResponse(
            status_code=error.status_code,
            body={"errors": [{"title": error.name, "detail": error.message}]},
        )
    return HttpResponse(
        status_code=500,
        body={"errors": [{"title": "Internal Server Error", "detail": str(error)}]},
    )
