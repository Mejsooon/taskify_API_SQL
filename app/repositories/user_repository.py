from app.core.database import execute
from app.models.models import User


def row_to_user(row: dict) -> User:
    return User(
        id=row["id"],
        name=row["name"],
        username=row["username"],
        password_hash=row["password_hash"],
    )


def find_by_username(username: str) -> User | None:
    row = execute("SELECT id, name, username, password_hash FROM users WHERE username = %s",
                 (username,), fetch="one",)

    if row is None:
        return None

    return row_to_user(row)


def find_by_id(user_id: int) -> User | None:
    row = execute("SELECT id, name, username, password_hash FROM users WHERE id = %s", (user_id,), fetch="one",)

    if row is None:
        return None

    return row_to_user(row)


def save(user: User) -> User:
    new_id = execute("INSERT INTO users (name, username, password_hash) VALUES (%s, %s, %s)",
        (
            user.name,
            user.username,
            user.password_hash,
        ),
    )

    return User(
        id=int(new_id),
        name=user.name,
        username=user.username,
        password_hash=user.password_hash,
    )