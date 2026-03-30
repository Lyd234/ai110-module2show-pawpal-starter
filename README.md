PawPal+
A pet care planning assistant that helps owners schedule daily care tasks across multiple pets — respecting available time, task priorities, and recurring care routines.

Overview
PawPal+ models pet care as a small, testable scheduling system. The app represents owners, pets, and tasks, and exposes a scheduler that builds a daily plan by selecting and ordering pending tasks according to priority, time, and the owner’s available minutes. The Streamlit UI provides a lightweight front end for entering owner/pet/task data and viewing the generated plan.

Features
Core scheduling features

Task model with scheduling metadata — Tasks include title, description, duration_minutes, time (HH:MM), due_date, frequency (once, daily, weekly), priority, category, and is_complete. These fields enable time‑aware sorting, recurrence, and conflict detection.

Sorting by time — Scheduler.sort_tasks_by_time() orders tasks by their HH:MM value to produce a stable chronological timeline.

Priority-based selection — Scheduler.sort_tasks_by_priority() ranks tasks high → medium → low. The planner uses this ordering to prefer higher-priority work when time is limited.

Greedy daily planner — Scheduler.generate_day_plan(available_minutes) implements a deterministic greedy algorithm: sort pending tasks by priority, then include each task if its duration fits the remaining time. This approach is fast, predictable, and easy to test.

Conflict warnings — Scheduler.detect_time_conflicts() groups pending tasks by time and returns a single warning per shared HH:MM slot listing colliding task titles. Completed tasks are excluded from conflict checks.

Daily recurrence handling — Task.mark_complete() and Task.create_next_occurrence() support recurring tasks. Marking a daily or weekly task complete spawns a new Task instance with the next due date while preserving metadata.

Task lifecycle operations — Helper methods let the UI and tests safely manage tasks: complete(), reopen(), toggle_completion(), set_duration(), and set_frequency().

Owner and Pet integration

Owner aggregation of pets — Owner manages multiple Pet objects and exposes get_all_tasks() and get_pending_tasks() so the scheduler can operate across all pets.

Pet composition of tasks — Pet owns its Task list and provides helpers (add_task, remove_task, pending_tasks, is_valid_task) to validate and manage tasks in the context of pet care needs.

UX and reporting

Human‑readable plan explanation — Scheduler.explain_plan() builds a readable explanation of selected tasks for display in the UI.

Schedule summary — Scheduler.get_schedule_summary() returns a concise summary string (number of selected tasks and total minutes) suitable for status banners or test assertions.

Getting Started and Usage
Prerequisites
Python 3.8+

Recommended: create an isolated virtual environment.

Install dependencies
bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
# or at minimum
pip install streamlit pytest
Run the Streamlit app
From the project root (where app.py lives):

bash
streamlit run app.py
Streamlit will start a local server and open the app in your browser. If the browser does not open automatically, paste the local URL shown in the terminal (for example http://localhost:8501) into your browser.

CLI demo
To run the command-line demonstration:

bash
python main.py
Testing and Known Issues
Run the test suite
bash
python -m pytest test_pawpal.py -v
Run a single test class:

bash
python -m pytest test_pawpal.py::TestConflictDetection -v
Stop at first failure:

bash
python -m pytest test_pawpal.py -x
What the tests cover
Sorting correctness — chronological ordering and priority ordering.

Recurrence logic — daily and weekly recurrence spawn follow-up tasks with correct metadata.

Conflict detection — grouped warnings for tasks sharing the same HH:MM slot.

Happy paths — end-to-end scheduling behavior and summary reporting.

Edge cases — zero/negative available time, exact-fit durations, duplicate pets, and helper method behavior.

Known issues
Double-complete bug in Scheduler.complete_task — completing a recurring task can match the newly spawned recurrence if the inner loop does not check not task.is_complete. Fix: ensure the completion condition includes and not task.is_complete.

Minor formatting omission in Task.summary() — priority is omitted from the summary string; include self.priority in the formatted output.

Both issues are small, well-scoped fixes and are documented in the test suite.