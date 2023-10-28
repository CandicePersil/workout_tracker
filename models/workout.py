from enum import Enum
from datetime import date
from pydantic import BaseModel


class Mouvment(Enum):
    SQUAT = "squat"
    BENCH = "bench"
    DEADLIFT = "deadlift"


class Exercise(BaseModel):
    mouvment: Mouvment
    reps: list[int]
    weight: float


class Workout(BaseModel):
    exercise: Exercise
    date: date
