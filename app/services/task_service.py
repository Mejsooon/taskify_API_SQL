from app.models.models import Task
from app.repositories import task_repository
from app.schemas.task import TaskCreate


class TaskNotFoundError(Exception):
    pass


class TaskNotOwnedError(Exception):
    pass


class TaskAlreadyCompletedError(Exception):
    pass


def create_task(user_id: int, task_data: TaskCreate) -> Task:
    task = Task(
        id=None,
        user_id=user_id,
        difficulty=task_data.difficulty,
        description=task_data.description,
        additional_notes=task_data.additional_notes,
        status="active",
    )

    return task_repository.save(task)


def find_active_tasks(user_id: int) -> list[Task]:
    return task_repository.find_by_user_id_and_status(
        user_id=user_id,
        status="active",
    )


def find_completed_tasks(user_id: int) -> list[Task]:
    return task_repository.find_by_user_id_and_status(
        user_id=user_id,
        status="completed",
    )


def complete_task(user_id: int, task_id: int) -> Task:
    task = task_repository.find_by_id(task_id)

    if task is None:
        raise TaskNotFoundError("Zadanie nie istnieje.")

    if task.user_id != user_id:
        raise TaskNotOwnedError(
            "Nie masz uprawnień do tego zadania."
        )

    if task.status == "completed":
        raise TaskAlreadyCompletedError(
            "Zadanie jest już oznaczone jako wykonane."
        )

    task_repository.mark_as_completed(task.id)

    task.status = "completed"

    return task