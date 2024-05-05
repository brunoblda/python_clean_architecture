""" This module contains the routes for the user entity. """

from flask import Blueprint, request, jsonify

# Import adapters
from src.main.adapters.request_adapter import request_adapter

# Import composers
from src.main.composers.user_register_composer import user_register_composer
from src.main.composers.user_finder_composer import user_finder_composer

# Import Validators
from src.validators.user_register_validator import user_register_validator
from src.validators.user_finder_validator import user_finder_validator

# import error handler
from src.errors.error_handler import handle_error

user_route_bp = Blueprint("user_route", __name__)


@user_route_bp.route("/user/find", methods=["GET"])
def find_user():
    """Route for find user"""

    http_response = None

    try:
        user_finder_validator(request)
        http_response = request_adapter(request, user_finder_composer())
    except Exception as exception:
        http_response = handle_error(exception)

    return jsonify(http_response.body), http_response.status_code


@user_route_bp.route("/user", methods=["POST"])
def register_user():
    """Route for register user"""

    http_response = None

    try:
        user_register_validator(request)
        http_response = request_adapter(request, user_register_composer())
    except Exception as exception:
        http_response = handle_error(exception)

    return jsonify(http_response.body), http_response.status_code
