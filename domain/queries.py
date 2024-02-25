from sqlalchemy.orm import Session

from db import models


# Movement queries
def get_movements(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Movement).offset(skip).limit(limit).all()


def get_movement_by_name(db: Session, name: str):
    return db.query(models.Movement).filter(models.Movement.name == name).first()


# Exercise queries
def get_exercises(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Exercise).offset(skip).limit(limit).all()


def get_exercices_by_mouvement_name(db: Session, name: str):
    return (
        db.query(models.Exercise)
        .join(models.Movement, models.Exercise.movement_id == models.Movement.id)
        .filter(models.Movement.name == name)
    )


# Workout queries
def get_workout(db: Session, workout_id: int):
    return db.query(models.Workout).filter(models.Workout.id == workout_id).first()


def get_workout_by_date(db: Session, date: str):
    return db.query(models.Workout).filter(models.Workout.date == date).first()


def get_workouts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Workout).offset(skip).limit(limit).all()
