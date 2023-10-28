from enum import Enum
from datetime import date
from pydantic import BaseModel


class SBDMovements(Enum):
    SQUAT = "squat"
    BENCH = "bench"
    DEADLIFT = "deadlift"


class MovementBase(BaseModel):
    name: str


class MovementCreate(MovementBase):
    pass


class Movement(MovementBase):
    id: int

    class Config:
        orm_mode = True


class ExerciseBase(BaseModel):
    movement_id: int
    reps: str
    weight: float
    workout_id: int


class ExerciseCreate(ExerciseBase):
    pass


class Exercise(ExerciseBase):
    id: int
    movement: Movement

    class Config:
        orm_mode = True


class WorkoutBase(BaseModel):
    date: date
    exercises: list[Exercise] = []


class WorkoutCreate(WorkoutBase):
    pass


class Workout(WorkoutBase):
    id: int

    class Config:
        orm_mode = True
