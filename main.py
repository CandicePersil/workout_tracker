from datetime import date
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from typing import Union, Any

from db import models
from shemas import workout as workout_shema
from domain import queries, operations

from db.database import SessionLocal, engine


models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def read_simple_root() -> dict[str, str]:
    return {"content": "Here is the simplest root ever!"}


@app.get("/movements/", response_model=list[workout_shema.Movement])
def get_movements(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    movements = queries.get_movements(db, skip=skip, limit=limit)
    return movements


@app.post("/movements/", response_model=workout_shema.Movement)
def create_movement(
    movement: workout_shema.MovementCreate, db: Session = Depends(get_db)
) -> dict[str, Any]:
    return operations.create_movement(db=db, movement=movement)


@app.get("/exercises/", response_model=list[workout_shema.Exercise])
def get_exercises(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    exercises = queries.get_exercises(db, skip=skip, limit=limit)
    return exercises


@app.post("/exercises/", response_model=workout_shema.Exercise)
def create_exercise(
    exercise: workout_shema.ExerciseCreate, db: Session = Depends(get_db)
) -> dict[str, Any]:
    return operations.create_exercise(db=db, exercise=exercise)


@app.get("/workouts/{date}", response_model=workout_shema.Workout)
def get_workout(date: Union[date, None] = None, db: Session = Depends(get_db)):
    db_workout = queries.get_workout_by_date(db=db, date=date)
    if not db_workout:
        raise HTTPException(
            status_code=404,
            detail="Workout not found",
        )
    return db_workout


@app.get("/workouts/", response_model=list[workout_shema.Workout])
def get_workouts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    workouts = queries.get_workouts(db, skip=skip, limit=limit)
    return workouts


@app.post("/workouts/", response_model=workout_shema.WorkoutCreate)
def create_workout(
    workout: workout_shema.WorkoutCreate, db: Session = Depends(get_db)
) -> dict[str, Any]:
    db_workout = queries.get_workout_by_date(db, date=workout.date)
    if db_workout:
        raise HTTPException(
            status_code=400,
            detail="Value error, workout already exists.",
        )
    return operations.create_workout(db=db, workout=workout)
