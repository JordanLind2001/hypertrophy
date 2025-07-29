import streamlit as st
import json
import os
from datetime import datetime

TEMPLATE_FILE = "workout_templates.json"
LOG_FILE = "workout_logs.json"

# Initialize templates file if it doesn't exist
if not os.path.exists(TEMPLATE_FILE):
    with open(TEMPLATE_FILE, "w") as f:
        json.dump({
            "Default": {
                "Monday": ["Incline Barbell Press", "Triceps Pushdown", "Barbell Curl"],
                "Tuesday": ["Barbell Row", "Face Pull", "Dumbbell Curl"],
                "Wednesday": ["Squat", "Leg Press", "Calf Raise"],
                "Thursday": ["Overhead Press", "Lateral Raise", "Skullcrusher"],
                "Friday": ["Deadlift", "Pull-Up", "Cable Curl"],
                "Saturday": ["Flat Dumbbell Press", "Overhead Cable Extension", "Preacher Curl"]
            }
        }, f)

# Initialize log file if it doesn't exist
if not os.path.exists(LOG_FILE):
    with open(LOG_FILE, "w") as f:
        json.dump({}, f)

# Load templates
def load_templates():
    with open(TEMPLATE_FILE, "r") as f:
        return json.load(f)

# Save templates
def save_templates(templates):
    with open(TEMPLATE_FILE, "w") as f:
        json.dump(templates, f)

# Load logs
def load_logs():
    with open(LOG_FILE, "r") as f:
        return json.load(f)

# Save logs
def save_logs(logs):
    with open(LOG_FILE, "w") as f:
        json.dump(logs, f)

st.set_page_config(page_title="Hypertrophy App", layout="wide")
st.title("🏋️ Hypertrophy Training App")

templates = load_templates()
logs = load_logs()

# Template selection and creation
template_names = list(templates.keys())
selected_template = st.selectbox("Choose a workout template", template_names)

with st.expander("➕ Create a New Template"):
    new_template_name = st.text_input("New Template Name")
    if st.button("Create Template") and new_template_name:
        if new_template_name not in templates:
            templates[new_template_name] = {day: [] for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]}
            save_templates(templates)
            st.success("Template created. Refresh to use it.")
        else:
            st.warning("Template already exists.")

# Day selection
selected_day = st.selectbox("Select day", list(templates[selected_template].keys()))
day_exercises = templates[selected_template][selected_day]

st.subheader(f"💪 {selected_day}'s Exercises")

# Workout Logging
today = datetime.now().strftime("%Y-%m-%d")
entry_key = f"{today}_{selected_day}"
day_data = logs.get(entry_key, {})

for ex in day_exercises:
    sets = st.number_input(f"Sets - {ex}", min_value=0, max_value=10, value=day_data.get(ex, {}).get("sets", 3), key=f"{ex}_sets")
    reps = st.number_input(f"Reps - {ex}", min_value=0, max_value=50, value=day_data.get(ex, {}).get("reps", 10), key=f"{ex}_reps")
    weight = st.number_input(f"Weight (lbs) - {ex}", min_value=0, max_value=1000, value=day_data.get(ex, {}).get("weight", 100), key=f"{ex}_weight")
    if entry_key not in logs:
        logs[entry_key] = {}
    logs[entry_key][ex] = {"sets": sets, "reps": reps, "weight": weight}

if st.button("💾 Save Workout"):
    save_logs(logs)
    st.success("Workout saved successfully!")

# History viewer
with st.expander("📜 View Previous Logs"):
    for key in sorted(logs.keys(), reverse=True):
        st.write(f"### {key}")
        for ex, details in logs[key].items():
            st.write(f"- **{ex}**: {details['sets']} sets x {details['reps']} reps @ {details['weight']} lbs")
