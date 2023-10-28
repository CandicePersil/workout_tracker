from datetime import date

from db import workout as workout_db
from models import workout as workout_models


def _insert_workout(input_workout: workout_models.Workout) -> None:
    if input_workout.exercise.weight > 120:
        raise ValueError("Weight is too high!")
    workouts = workout_db.workouts
    workouts.append(input_workout)
