from datetime import date
from fastapi import FastAPI, HTTPException
from typing import Union, Any


from models import workout as workout_models
from domain import queries, operations

app = FastAPI()


@app.get("/")
def read_simple_root() -> dict[str, str]:
    return {"content": "Here is the simplest root ever!"}


@app.get("/workouts", response_model=list[workout_models.Workout])
def get_workout(date: Union[date, None] = None):
    return queries.find_workouts(date=date)


@app.post("/workouts/", response_model=workout_models.Workout)
def create_workout(workout: workout_models.Workout) -> dict[str, Any]:
    try:
        operations.insert_workout(input_workout=workout)
    except ValueError as err:
        raise HTTPException(
            status_code=400,
            detail="Value error, workout could not be inserted. " + str(err),
        ) from err
    return workout
