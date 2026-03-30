import streamlit as st
from pawpal_system import Owner, Pet, Task, Scheduler

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

st.title("🐾 PawPal+")



st.markdown(
    """
Welcome to the PawPal+ starter app.

This file is intentionally thin. It gives you a working Streamlit app so you can start quickly,
but **it does not implement the project logic**. Your job is to design the system and build it.

Use this app as your interactive demo once your backend classes/functions exist.
"""
)

with st.expander("Scenario", expanded=True):
    st.markdown(
        """
**PawPal+** is a pet care planning assistant. It helps a pet owner plan care tasks
for their pet(s) based on constraints like time, priority, and preferences.

You will design and implement the scheduling logic and connect it to this Streamlit UI.
"""
    )

with st.expander("What you need to build", expanded=True):
    st.markdown(
        """
At minimum, your system should:
- Represent pet care tasks (what needs to happen, how long it takes, priority)
- Represent the pet and the owner (basic info and preferences)
- Build a plan/schedule for a day that chooses and orders tasks based on constraints
- Explain the plan (why each task was chosen and when it happens)
"""
    )

st.divider()

if "owner" not in st.session_state:
    st.session_state.owner = Owner(name="Jordan", available_time=120)

owner = st.session_state.owner

st.subheader("Owner")
owner_name = st.text_input("Owner name", value=owner.name)
owner.name = owner_name

st.markdown("### Add a Pet")
with st.expander("Add a new pet", expanded=True):
    pet_name = st.text_input("Pet name", value="Mochi", key="new_pet_name")
    species = st.selectbox("Species", ["dog", "cat", "other"], index=0, key="new_pet_species")
    age = st.number_input("Age", min_value=0, max_value=30, value=2, key="new_pet_age")
    care_needs = st.multiselect("Care needs", ["walk", "feed", "play", "groom", "meds"], key="new_pet_care_needs")
    if st.button("Add pet"):
        new_pet = Pet(name=pet_name, species=species, age=age, care_needs=care_needs)
        owner.add_pet(new_pet)
        st.success(f"Added {pet_name} to {owner.name}")

if owner.get_all_pets():
    st.write("Current pets:")
    for pet in owner.get_all_pets():
        st.write(pet.describe())
else:
    st.info("Add a pet first to start scheduling tasks.")

st.markdown("### Tasks")
st.caption("Add a task to one of your pets.")

if owner.get_all_pets():
    pet_names = [pet.name for pet in owner.get_all_pets()]
    selected_pet_name = st.selectbox("Assign task to", pet_names, key="task_pet")
    selected_pet = next((pet for pet in owner.get_all_pets() if pet.name == selected_pet_name), None)

    col1, col2, col3 = st.columns(3)
    with col1:
        task_title = st.text_input("Task title", value="Morning walk", key="task_title")
    with col2:
        duration = st.number_input("Duration (minutes)", min_value=1, max_value=240, value=20, key="task_duration")
    with col3:
        priority = st.selectbox("Priority", ["low", "medium", "high"], index=2, key="task_priority")

    task_description = st.text_area("Task description", value="Describe the task.", key="task_description")
    category = st.selectbox("Category", ["walk", "feed", "play", "groom", "meds", "general"], index=0, key="task_category")

    if st.button("Add task"):
        new_task = Task(
            title=task_title,
            description=task_description,
            duration_minutes=int(duration),
            priority=priority,
            category=category,
        )
        selected_pet.add_task(new_task)
        st.success(f"Added task to {selected_pet.name}")

    all_tasks = []
    for pet in owner.get_all_pets():
        for task in pet.get_tasks():
            all_tasks.append(
                {
                    "pet": pet.name,
                    "title": task.title,
                    "duration_minutes": task.duration_minutes,
                    "priority": task.priority,
                    "category": task.category,
                    "status": "done" if task.is_complete else "pending",
                }
            )

    if all_tasks:
        st.write("Current tasks:")
        st.table(all_tasks)
else:
    st.info("Create a pet first, then add tasks to that pet.")

st.divider()

st.subheader("Build Schedule")
st.caption("This button should call your scheduling logic once you implement it.")

if st.button("Generate schedule"):
    st.warning(
        "Not implemented yet. Next step: create your scheduling logic (classes/functions) and call it here."
    )
    st.markdown(
        """
Suggested approach:
1. Design your UML (draft).
2. Create class stubs (no logic).
3. Implement scheduling behavior.
4. Connect your scheduler here and display results.
"""
    )
