import streamlit as st
import json
from pathlib import Path

# File paths (works locally and on Streamlit Cloud)
DATA_FILE = Path("workout_data.json")
TEMPLATE_FILE = Path("templates.json")

def load_templates():
    if TEMPLATE_FILE.exists():
        try:
            with open(TEMPLATE_FILE, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return {}
    # Default template if none saved yet
    default = {
        "Default Template": {
            "Monday": ["Incline Barbell Press", "Overhead Press", "Skullcrushers"],
            "Tuesday": ["Pull-ups", "Barbell Rows", "EZ Bar Curls"],
            "Wednesday": ["Back Squat", "Leg Press", "Romanian Deadlifts"],
            "Thursday": ["EZ Bar Curl", "Triceps Pushdown", "Cable Hammer Curl"],
            "Friday": ["Lateral Raises", "Rear Delt Fly", "Wide Grip Pulldown"],
            "Saturday": ["Flat Dumbbell Press", "Overhead Cable Extension", "Preacher Curl"]
        }
    }
    save_templates(default)
    return default

def save_templates(templates):
    with open(TEMPLATE_FILE, "w") as f:
        json.dump(templates, f, indent=2)

def load_data():
    if DATA_FILE.exists():
        try:
            with open(DATA_FILE, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return {}
    return {}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

def template_manager(templates):
    st.header("Workout Template Manager")

    # Select or create template
    template_names = list(templates.keys())
    selected_template = st.selectbox("Select Template", template_names)

    new_template_name = st.text_input("Or create new template")
    if new_template_name:
        if new_template_name in templates:
            st.warning("Template with that name already exists.")
        elif st.button("Create Template"):
            templates[new_template_name] = {day: [] for day in ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday]()
