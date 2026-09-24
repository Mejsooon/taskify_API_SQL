from dataclasses import dataclass

@dataclass
class User:
    id: int | None
    name: str
    username: str
    password_hash: str


@dataclass
class Task:
    id: int | None
    user_id: int
    difficulty: int
    description: str
    additional_notes: str | None = None
    status: str = "active"