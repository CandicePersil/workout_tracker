from sqlalchemy.orm import Session

from db import models
from shemas import workout as workout_schema
from domain import queries


class InsertWorkoutException(Exception):
    pass


class CreateMovementException(Exception):
    pass


def create_movement(db: Session, movement: workout_schema.MovementCreate):
    movement_input = movement.model_dump()
    try:
        workout_schema.MovementType(movement_input.get("type"))
    except ValueError:
        raise CreateMovementException("Wrong movement type!")
    db_movement = models.Movement(**movement_input)
    db.add(db_movement)
    db.commit()
    db.refresh(db_movement)
    return db_movement


def create_exercise(db: Session, exercise: workout_schema.ExerciseCreate):
    exercise_input = exercise.model_dump()
    movement = queries.get_movement_by_name(db, exercise_input.pop("movement_name"))
    db_exercise = models.Exercise(**exercise_input, movement_id=movement.id)
    db.add(db_exercise)
    db.commit()
    db.refresh(db_exercise)
    return db_exercise


def create_workout(db: Session, workout: workout_schema.WorkoutCreate):
    db_workout = models.Workout(**workout.model_dump())
    db.add(db_workout)
    db.commit()
    db.refresh(db_workout)
    return db_workout
