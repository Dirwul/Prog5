from enum import Enum
from pydantic import BaseModel

class Status(Enum):
    to_do = "to do"
    in_progress = "in progress"
    done = "done"

class TaskBase(BaseModel):
    title: str
    description: str = None
    status: str


class Task(TaskBase):
    id: int

    # для FastAPI и бд, дабы метчить модель
    class Config:
        from_attributes = True

class TaskCreate(TaskBase):
    pass
