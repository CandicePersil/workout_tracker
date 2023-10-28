# workout_tracker

## Description
The goal of this repository is to propose an api able to create and
get workouts in order to follow your evolution in time.

## How to run the API
```uvicorn main:app --reload```

## What is a workout
* workout
    * exercises
    * date
* exercise
    * movement (enum)
    * list of rep
    * weight

## Available roots
* root to post a workout
* root to get workouts

## Load data from excel
How to parse excels ?