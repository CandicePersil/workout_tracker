from sqlalchemy.orm import Session

from db import models
from shemas import workout as workout_schema


class InsertWorkoutException(Exception):
    pass


def create_workout(db: Session, workout: workout_schema.WorkoutCreate):
    db_workout = models.Workout(**workout.model_dump())
    db.add(db_workout)
    db.commit()
    db.refresh(db_workout)
    return db_workout
