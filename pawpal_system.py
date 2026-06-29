"""
pawpal_system.py
PawPal+ – Pet care scheduling system.

Classes
-------
Owner    : stores owner info and manages a list of pets
Pet      : dataclass representing a pet
Task     : dataclass representing a single care task
Schedule : organises tasks, detects conflicts, shows daily view
"""
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date as _today


# ──────────────────────────────────────────────
# Owner
# ──────────────────────────────────────────────

class Owner:
    """Stores owner information and manages a collection of pets."""

    def __init__(self, name: str, contact: str) -> None:
        self.name: str = name
        self.contact: str = contact
        self.pets: list[Pet] = []

    def add_pet(self, pet: Pet) -> None:
        """Append *pet* to this owner's pet list."""
        pass

    def get_pets(self) -> list[Pet]:
        """Return all pets belonging to this owner."""
        pass

    def __str__(self) -> str:
        return f"Owner({self.name})"


# ──────────────────────────────────────────────
# Pet  (dataclass)
# ──────────────────────────────────────────────

@dataclass
class Pet:
    """Represents a pet that belongs to an owner."""

    name: str
    age: int
    species: str
    owner: Owner | None = field(default=None, repr=False)

    def get_info(self) -> str:
        """Return a human-readable summary of this pet."""
        pass

    def __str__(self) -> str:
        return f"{self.name} ({self.species}, age {self.age})"


# ──────────────────────────────────────────────
# Task  (dataclass)
# ──────────────────────────────────────────────

@dataclass
class Task:
    """Represents a single pet care task."""

    task_type: str          # e.g. "walk" | "feeding" | "medicine" | "grooming"
    pet: Pet
    date: str               # "YYYY-MM-DD"
    time: str               # "HH:MM"
    status: str = "pending" # "pending" | "done"

    def complete(self) -> None:
        """Mark this task as done."""
        pass

    def reschedule(self, date: str, time: str) -> None:
        """Update the task's date and time."""
        pass

    def __str__(self) -> str:
        return (
            f"[{self.status.upper()}] {self.task_type} "
            f"for {self.pet.name} on {self.date} at {self.time}"
        )


# ──────────────────────────────────────────────
# Schedule
# ──────────────────────────────────────────────

class Schedule:
    """Organises tasks by day, detects conflicts, and surfaces today's plan."""

    def __init__(self) -> None:
        self.tasks: list[Task] = []

    def add_task(self, task: Task) -> None:
        """Add a task to the schedule."""
        pass

    def detect_conflicts(self) -> list[tuple[Task, Task]]:
        """Return pairs of tasks that share the same date and time slot."""
        pass

    def show_today_tasks(self) -> list[Task]:
        """Return all tasks whose date matches today."""
        pass

    def get_tasks_by_day(self, date: str) -> list[Task]:
        """Return all tasks scheduled for *date* (format 'YYYY-MM-DD')."""
        pass

    def __str__(self) -> str:
        return f"Schedule({len(self.tasks)} tasks)"
