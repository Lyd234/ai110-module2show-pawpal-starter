import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from pawpal_system import Pet, Task


def test_task_completion_marks_task_as_complete() -> None:
    task = Task(
        title="Feed breakfast",
        description="Feed the pet breakfast.",
        duration_minutes=15,
        priority="medium",
        category="feed",
    )

    assert not task.is_complete

    task.mark_complete()

    assert task.is_complete


def test_pet_add_task_increases_task_count() -> None:
    pet = Pet(name="Mochi", species="dog", age=4)
    initial_count = len(pet.tasks)

    task = Task(
        title="Morning walk",
        description="Walk for 30 minutes.",
        duration_minutes=30,
        priority="high",
        category="walk",
    )

    pet.add_task(task)

    assert len(pet.tasks) == initial_count + 1
    assert pet.tasks[0] is task
