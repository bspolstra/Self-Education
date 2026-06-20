from flask import Blueprint, request

from controllers.users_controller import login_user, signup_user

users_bp = Blueprint("users", __name__, url_prefix="/users")


@users_bp.route("/signup", methods=["POST"])
def signup():
    data = request.get_json(silent=True) or {}
    body, status = signup_user(data)
    return body, status


@users_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json(silent=True) or {}
    body, status = login_user(data)
    return body, status
