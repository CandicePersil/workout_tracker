from datetime import date

from db import workout as workout_db
from models import workout as workout_models


def find_workouts(date: date | None = None) -> list[workout_models.Workout]:
    # query the database
    workouts = workout_db.workouts
    if date:
        return [workout for workout in workouts if workout.date == date]
    return workouts
