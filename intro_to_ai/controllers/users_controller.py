from models import create_user, validate_login


def signup_user(data):
    username = data.get("username", "").strip()
    email = data.get("email", "").strip()
    password = data.get("password", "")

    if not username or not email or not password:
        return {"error": "username, email, and password are required"}, 400

    user, error = create_user(username, email, password)
    if error:
        return {"error": error}, 409

    return {"message": "User registered successfully", "user": user}, 201


def login_user(data):
    email = data.get("email", "").strip()
    password = data.get("password", "")

    if not email or not password:
        return {"error": "email and password are required"}, 400

    user, error = validate_login(email, password)
    if error:
        return {"error": error}, 401

    return {"message": "Login successful", "user": user}, 200
