from enum import Enum
from datetime import date
from pydantic import BaseModel


class SBDMovements(Enum):
    SQUAT = "squat"
    BENCH = "bench"
    DEADLIFT = "deadlift"


class MovementType(Enum):
    PECTORALS = "pectorals"
    BACK = "back"
    BISEPS = "biseps"
    TRISEPS = "triseps"
    SHOULDERS = "shoulders"
    ABDOMINAUX = "abdominals"
    QUADRICEPS = "quadriceps"
    ISCHIOS = "ischios"
    CALVES = "calves"
    FOREARMS = "forearms"
    ARMS = "arms"
    LEGS = "legs"


class MovementBase(BaseModel):
    name: str
    type: str


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


class ExerciseCreate(BaseModel):
    movement_name: str
    reps: str
    weight: float
    workout_id: int


class Exercise(ExerciseBase):
    id: int

    class Config:
        orm_mode = True


class WorkoutBase(BaseModel):
    date: date


class WorkoutCreate(WorkoutBase):
    pass


class Workout(WorkoutBase):
    exercises: list[Exercise] = []
    id: int

    class Config:
        orm_mode = True
