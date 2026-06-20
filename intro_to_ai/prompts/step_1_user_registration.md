Prompt:
```
The app utilizes Flask framework. This REST API needs user authentication.
Users must be able to register (signup) and login.

Don't add any JWT code or anything like that, just generate User model (without using classes) in the models folder.

Also generate signup and login routes (e.g., /users/signup) in the routes folders.

Last but not least add the code for linking route and model to a users controller (controllers folder).
Don't add any code for storing user data in a database yet.
```

Bonus prompt: 
```
add the previous output to @intro_to_ai/prompts/step_1_user_registration.md under Output line. retain the markdown syntax
```

Plan Usage: 3% -> 11%

Output:

The Flask auth scaffolding is in place with a layered structure and no JWT or database code.

## Structure

```text
intro_to_ai/
├── app.py
├── models/
│   ├── __init__.py
│   └── user.py
├── controllers/
│   ├── __init__.py
│   └── users_controller.py
└── routes/
    ├── __init__.py
    └── users.py
```

## Layers

**Model** (`models/user.py`) — dict-based user records (no classes):

- `create_user()` — builds a user dict with hashed password
- `find_user_by_email()` / `find_user_by_username()` — lookups
- `validate_login()` — checks email/password
- `user_to_public()` — strips sensitive fields before returning

**Controller** (`controllers/users_controller.py`) — request validation and orchestration:

- `signup_user()` — validates input, calls the model, returns `(body, status)`
- `login_user()` — same pattern for login

**Routes** (`routes/users.py`) — HTTP endpoints wired to the controller:

- `POST /users/signup`
- `POST /users/login`

**App** (`app.py`) — creates the Flask app and registers the users blueprint.

## Endpoints

| Method | Path | Body | Success |
|--------|------|------|---------|
| POST | `/users/signup` | `{ "username", "email", "password" }` | 201 |
| POST | `/users/login` | `{ "email", "password" }` | 200 |

## Notes

- No JWT — login returns the user object directly.
- No database — users are kept in in-memory dicts in the model for now so signup/login can be tested. That can be swapped for PostgreSQL later without changing routes or the controller.
- Passwords are hashed with Werkzeug (`pbkdf2:sha256`), which ships with Flask.
- Flask was added to `pyproject.toml`.

Run the app:

```bash
cd intro_to_ai
python app.py
```

Example signup:

```bash
curl -X POST http://127.0.0.1:5000/users/signup \
  -H "Content-Type: application/json" \
  -d '{"username":"alice","email":"alice@example.com","password":"secret123"}'
```

