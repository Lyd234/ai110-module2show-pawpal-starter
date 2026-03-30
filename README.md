# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints (time available, priority, owner preferences)
- Produce a daily plan and explain why it chose that plan

Your job is to design the system first (UML), then implement the logic in Python, then connect it to the Streamlit UI.

## What you will build

Your final app should:

- Let a user enter basic owner + pet info
- Let a user add/edit tasks (duration + priority at minimum)
- Generate a daily schedule/plan based on constraints and priorities
- Display the plan clearly (and ideally explain the reasoning)
- Include tests for the most important scheduling behaviors



## Getting started

### Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Suggested workflow

1. Read the scenario carefully and identify requirements and edge cases.
2. Draft a UML diagram (classes, attributes, methods, relationships).
3. Convert UML into Python class stubs (no logic yet).
4. Implement scheduling logic in small increments.
5. Add tests to verify key behaviors.
6. Connect your logic to the Streamlit UI in `app.py`.
7. Refine UML so it matches what you actually built.
##  Smarter Scheduling 

- `Task` now includes a `time` field so tasks can be ordered by clock time.
- `Scheduler.sort_tasks_by_time()` sorts tasks using their `HH:MM` time values.
- `Scheduler.detect_time_conflicts()` finds same-time task collisions and returns warnings instead of crashing.
- `main.py` now demonstrates out-of-order task input and verifies sorting plus conflict detection in the terminal.
- `app.py` now uses `Owner`, `Pet`, `Task`, and `Scheduler` methods instead of remaining as UI-only placeholders.



# 🐾 PawPal+

A pet care planning assistant that helps owners schedule daily care tasks across multiple pets — respecting time constraints, task priorities, and recurring care routines.
---
### Install dependencies

```bash
pip install streamlit pytest
```
### Run the Streamlit app
```bash
streamlit run app.py
```
### Run the CLI demo

```bash
python main.py
```
---
## Testing PawPal+
### Run the test suite

```bash
python -m pytest test_pawpal.py -v
```
To run a specific test class only:

```bash
python -m pytest test_pawpal.py::TestConflictDetection -v
```
To stop at the first failure:
```bash
python -m pytest test_pawpal.py -x
```
---

### What the tests cover

The suite contains **47 tests** across five areas:

**Sorting correctness** — `TestSortByTime`, `TestSortByPriority`
Verifies that `sort_tasks_by_time` returns tasks in strict chronological (HH:MM) order, including edge cases like midnight boundaries and single-item lists. Also confirms that `sort_tasks_by_priority` produces the correct high → medium → low ordering, handles ties without crashing, and gracefully falls back when an unrecognised priority string (e.g. `"urgent"`) is encountered.

**Recurrence logic** — `TestRecurrence`
Confirms that marking a `daily` task complete creates a new pending task with a due date exactly one day later, and that a `weekly` task produces a follow-up one week out. Verifies that `once` tasks produce no next occurrence. Also checks that the spawned task inherits all metadata (priority, category, duration) from its parent, and documents a confirmed bug where double-completing a recurring task can spawn a duplicate (see bugs section below).

**Conflict detection** — `TestConflictDetection`
Verifies that `detect_time_conflicts` returns no warnings when all task times are distinct, and flags exactly one grouped warning per shared HH:MM slot when duplicates exist. Confirms that already-completed tasks are excluded from the check and that three tasks at the same time produce one warning (not three).

**Happy paths** — `TestHappyPaths`
End-to-end scheduling: tasks that collectively fit within available time are all selected; the plan is returned in priority order; completed tasks are excluded from the plan; and `get_schedule_summary` reports the correct task count and total minutes.

**Edge and boundary cases** — `TestEdgeCases`
Covers zero available time (empty plan), negative available time (clamped to 0), a task whose duration exactly equals remaining time (should be included, not excluded), one-minute-over exclusion, pets and owners with no tasks, removing nonexistent pets or tasks, duplicate pet-object prevention, and helper method behaviour (`can_schedule`, `toggle_completion`, `is_high_priority`).

---

### Known bugs found by the suite

| # | Severity | Location | Description | Fix |
|---|---|---|---|---|
| 1 | **Medium** | `Scheduler.complete_task` | Matches tasks by title only, not completion status. Double-calling completes the newly spawned recurrence, creating a third task. | Add `and not task.is_complete` to the inner loop condition. |
| 2 | Low | `Task.summary()` | Priority is omitted from the summary string. | Include `self.priority` in the formatted output. |
---
### Confidence level
```
Reliability: ★★★★☆  (4 / 5)
```
The core scheduling logic — priority ordering, time-based sorting, conflict detection, and recurrence — all behave correctly under normal use and across the tested edge cases. The 46/47 pass rate reflects a well-structured system rather than a fragile one.

The one-star deduction reflects two real gaps: the double-complete bug in `Scheduler.complete_task` (a medium-severity correctness issue in a user-facing workflow) and the fact that `Task.summary()` silently drops the priority field. Neither breaks the scheduler's primary function, but both would surface in production. The fixes are each a single line. Once applied, this system would warrant a full 5-star rating within its current feature scope.
---
## System Overview

### Classes

| Class | Responsibility |
|---|---|
| `Task` | A single care action with title, duration, priority, category, time, and recurrence frequency |
| `Pet` | Holds a list of tasks; filters by completion status; validates tasks against care needs |
| `Owner` | Manages a list of pets, tracks available daily time, and stores preferences |
| `Scheduler` | Generates day plans, sorts and groups tasks, detects time conflicts, marks tasks complete |

### Scheduling algorithm

`generate_day_plan` uses a greedy priority-first strategy: it sorts all pending tasks by priority (high → medium → low), then walks the list adding each task that fits within remaining available time. This is not globally optimal but is predictable, fast, and easy to reason about.
