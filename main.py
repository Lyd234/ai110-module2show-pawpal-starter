from pawpal_system import Owner, Pet, Task, Scheduler


def main() -> None:
    owner = Owner(name="Jordan", available_time=90, preferences={"preferred_time": "morning"})

    mochi = Pet(name="Mochi", species="dog", age=4, care_needs=["walk", "feed"])
    piper = Pet(name="Piper", species="cat", age=2, care_needs=["feed", "play"])

    owner.add_pet(mochi)
    owner.add_pet(piper)

    morning_walk = Task(
        title="Morning walk",
        description="Take Mochi for a 30-minute walk around the block.",
        duration_minutes=30,
        frequency="daily",
        priority="high",
        category="walk",
    )

    breakfast = Task(
        title="Feed breakfast",
        description="Serve breakfast to both Mochi and Piper.",
        duration_minutes=15,
        frequency="daily",
        priority="medium",
        category="feed",
    )

    play_time = Task(
        title="Play session",
        description="Play with Piper using a laser toy and enrichment toys.",
        duration_minutes=25,
        frequency="daily",
        priority="low",
        category="play",
    )

    mochi.add_task(morning_walk)
    mochi.add_task(breakfast)
    piper.add_task(play_time)

    scheduler = Scheduler(owner)
    schedule = scheduler.generate_day_plan()

    print("Today's Schedule")
    print("-------------------")
    if not schedule:
        print("No tasks scheduled for today.")
        return

    for task in schedule:
        status = "Done" if task.is_complete else "Pending"
        print(f"- {task.title} ({task.duration_minutes}m) [{task.priority.capitalize()}] - {status}")

    print()
    print(scheduler.get_schedule_summary(schedule))


if __name__ == "__main__":
    main()
