from sqlalchemy.orm import Session

from db import models


def get_workout(db: Session, workout_id: int):
    return db.query(models.Workout).filter(models.Workout.id == workout_id).first()


def get_workout_by_date(db: Session, date: str):
    return db.query(models.Workout).filter(models.Workout.date == date).first()


def get_workouts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Workout).offset(skip).limit(limit).all()
