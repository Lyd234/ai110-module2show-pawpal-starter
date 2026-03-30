from pawpal_system import Owner, Pet, Task, Scheduler


def main() -> None:
    owner = Owner(name="Jordan", available_time=90, preferences={"preferred_time": "morning"})

    mochi = Pet(name="Mochi", species="dog", age=4, care_needs=["walk", "feed"])
    piper = Pet(name="Piper", species="cat", age=2, care_needs=["feed", "play"])

    owner.add_pet(mochi)
    owner.add_pet(piper)

    # Add tasks out of time order, including a conflict at 09:45
    evening_snack = Task(
        title="Evening snack",
        description="Give Piper a small evening snack.",
        duration_minutes=10,
        time="19:30",
        priority="low",
        category="feed",
    )

    lunch = Task(
        title="Lunchtime feeding",
        description="Feed Mochi and Piper lunch together.",
        duration_minutes=20,
        time="12:15",
        priority="medium",
        category="feed",
    )

    morning_walk = Task(
        title="Morning walk",
        description="Take Mochi for a 30-minute walk around the block.",
        duration_minutes=30,
        time="09:45",
        priority="high",
        category="walk",
    )

    play_time = Task(
        title="Play session",
        description="Play with Piper using a laser toy and enrichment toys.",
        duration_minutes=25,
        time="09:45",
        priority="medium",
        category="play",
    )

    mochi.add_task(lunch)
    mochi.add_task(morning_walk)
    piper.add_task(evening_snack)
    piper.add_task(play_time)

    scheduler = Scheduler(owner)

    print("All pending tasks (unsorted):")
    pending_tasks = scheduler.retrieve_pending_tasks()
    for task in pending_tasks:
        print(f"- {task.title} at {task.time} [{task.priority}]")

    print("\nPending tasks sorted by time:")
    sorted_by_time = scheduler.sort_tasks_by_time(pending_tasks)
    for task in sorted_by_time:
        print(f"- {task.title} at {task.time} [{task.priority}]")

    print("\nConflict warnings:")
    conflict_warnings = scheduler.detect_time_conflicts(pending_tasks)
    if conflict_warnings:
        for warning in conflict_warnings:
            print(f"WARNING: {warning}")
    else:
        print("No conflicts detected.")

    print("\nPending tasks sorted by priority:")
    sorted_by_priority = scheduler.sort_tasks_by_priority(pending_tasks)
    for task in sorted_by_priority:
        print(f"- {task.title} ({task.duration_minutes}m) [{task.priority}]")

    print("\nSchedule summary using generate_day_plan():")
    schedule = scheduler.generate_day_plan()
    if not schedule:
        print("No tasks scheduled for today.")
    else:
        for task in schedule:
            print(f"- {task.title} at {task.time} ({task.duration_minutes}m) [{task.priority}]")
        print(scheduler.get_schedule_summary(schedule))


if __name__ == "__main__":
    main()
