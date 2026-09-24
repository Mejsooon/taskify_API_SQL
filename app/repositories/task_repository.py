from app.core.database import execute
from app.models.models import Task


def row_to_task(row: dict) -> Task:
    return Task(
        id=row["id"],
        user_id=row["user_id"],
        difficulty=row["difficulty"],
        description=row["description"],
        additional_notes=row["additional_notes"],
        status=row["status"],
    )


def save(task: Task) -> Task:
    new_id = execute("INSERT INTO tasks (user_id, difficulty, description, additional_notes, status) VALUES (%s, %s, %s, %s, %s)",
        (
            task.user_id,
            task.difficulty,
            task.description,
            task.additional_notes,
            task.status,
        ),
    )

    return Task(
        id=int(new_id),
        user_id=task.user_id,
        difficulty=task.difficulty,
        description=task.description,
        additional_notes=task.additional_notes,
        status=task.status,
    )


def find_by_user_id_and_status(user_id: int, status: str, ) -> list[Task]:
    rows = execute("SELECT id, user_id, difficulty, description, additional_notes, status FROM tasks WHERE user_id = %s AND status = %s ORDER BY id",
                   (user_id, status), fetch="all",)

    return [row_to_task(row) for row in rows]


def find_by_id(task_id: int) -> Task | None:
    row = execute("SELECT id, user_id, difficulty, description, additional_notes, status FROM tasks WHERE id = %s", (task_id,), fetch="one",)

    if row is None:
        return None

    return row_to_task(row)


def mark_as_completed(task_id: int) -> None:
    execute("UPDATE tasks SET status = 'completed' WHERE id = %s",(task_id,),)