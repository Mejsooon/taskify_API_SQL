from fastapi import APIRouter, HTTPException, status

from app.schemas.task import TaskCreate, TaskResponse
from app.services import task_service


router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"],
)


@router.post(
    "",
    response_model=TaskResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_task(
    user_id: int,
    task_data: TaskCreate,
):
    return task_service.create_task(
        user_id=user_id,
        task_data=task_data,
    )


@router.get(
    "/active",
    response_model=list[TaskResponse],
)
def get_active_tasks(user_id: int):
    return task_service.find_active_tasks(user_id)


@router.get(
    "/completed",
    response_model=list[TaskResponse],
)
def get_completed_tasks(user_id: int):
    return task_service.find_completed_tasks(user_id)


@router.post(
    "/{task_id}/complete",
    response_model=TaskResponse,
)
def complete_task(
    task_id: int,
    user_id: int,
):
    try:
        return task_service.complete_task(
            user_id=user_id,
            task_id=task_id,
        )

    except task_service.TaskNotFoundError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        )

    except task_service.TaskNotOwnedError as exc:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=str(exc),
        )

    except task_service.TaskAlreadyCompletedError as exc:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(exc),
        )