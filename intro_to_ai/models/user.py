from datetime import datetime, timezone
from uuid import uuid4

from werkzeug.security import check_password_hash, generate_password_hash

_users_by_id = {}
_users_by_email = {}


def create_user(username, email, password):
    if find_user_by_email(email):
        return None, "Email is already registered"

    if find_user_by_username(username):
        return None, "Username is already taken"

    user = {
        "id": str(uuid4()),
        "username": username,
        "email": email,
        "password_hash": generate_password_hash(password, method="pbkdf2:sha256"),
        "created_at": datetime.now(timezone.utc).isoformat(),
    }

    _users_by_id[user["id"]] = user
    _users_by_email[user["email"]] = user

    return user_to_public(user), None


def find_user_by_email(email):
    return _users_by_email.get(email)


def find_user_by_username(username):
    for user in _users_by_id.values():
        if user["username"] == username:
            return user
    return None


def validate_login(email, password):
    user = find_user_by_email(email)
    if not user or not check_password_hash(user["password_hash"], password):
        return None, "Invalid email or password"

    return user_to_public(user), None


def user_to_public(user):
    return {
        "id": user["id"],
        "username": user["username"],
        "email": user["email"],
        "created_at": user["created_at"],
    }
