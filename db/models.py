from typing import List

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from db.database import Base


class Movement(Base):
    __tablename__ = "movement"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(unique=True, index=True)
    type: Mapped[str] = mapped_column(unique=False, index=True)


class Exercise(Base):
    __tablename__ = "exercise"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    movement_id: Mapped[int] = mapped_column(ForeignKey("movement.id"))
    reps: Mapped[str] = mapped_column(default="[10,10,10]")
    weight: Mapped[float] = mapped_column(default=10.0)

    workout_id: Mapped[int] = mapped_column(ForeignKey("workout.id"))
    workout: Mapped["Workout"] = relationship(back_populates="exercises")


class Workout(Base):
    __tablename__ = "workout"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    date: Mapped[str] = mapped_column()

    exercises: Mapped[List["Exercise"]] = relationship(back_populates="workout")
