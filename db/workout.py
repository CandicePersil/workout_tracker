from datetime import date

from models import workout

workouts: list[workout.Workout] = [
    workout.Workout(
        exercises=[
            workout.Exercise(
                mouvment=workout.Mouvment.SQUAT,
                reps=[9, 8, 8],
                weight=67.5,
            ),
            workout.Exercise(
                mouvment=workout.Mouvment.DEADLIFT,
                reps=[4, 4, 3],
                weight=102.5,
            ),
        ],
        date=date(year=2023, month=10, day=25),
    ),
    workout.Workout(
        exercises=[
            workout.Exercise(
                mouvment=workout.Mouvment.BENCH,
                reps=[12, 11, 10],
                weight=35.0,
            )
        ],
        date=date(year=2023, month=8, day=2),
    ),
]
