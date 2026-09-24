from pydantic import BaseModel, Field

class TaskCreate(BaseModel):
    difficulty: int = Field(ge=1, le=10)
    description: str = Field(min_length=1)
    additional_notes: str | None = None


class TaskResponse(BaseModel):
    id: int
    user_id: int
    difficulty: int
    description: str
    additional_notes: str | None
    status: str