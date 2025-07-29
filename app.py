import streamlit as st
import json
from pathlib import Path

# File paths
DATA_FILE = Path("workout_data.json")
TEMPLATE_FILE = Path("templates.json")

# Load or initialize templates
def load_templates():
    if TEMPLATE_FILE.exists():
        with open(TEMPLATE_FILE, "r") as f:
            return json.load(f)
    # Default template
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

# Load or initialize workout data
def load_data():
    if DATA_FILE.exists():
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

def main():
    st.title("Personalized Hypertrophy Training Tracker")

    # Load data
    workout_data = load_data()
    templates = load_templates()

    # Sidebar for mode
    mode = st.sidebar.selectbox("Select Mode", ["Workout Tracker", "Template Manager"])

    if mode == "Template Manager":
        st.header("Workout Template Manager")
        # Template selection and management
        template_names = list(templates.keys())
        selected_template = st.selectbox("Select Template", template_names)

        # Option to add new template
        new_template_name = st.text_input("Or create new template", value="")
        if new_template_name:
            if new_template_name in templates:
                st.warning("Template name already exists.")
            elif st.button("Create New Template"):
                templates[new_template_name] = {day: [] for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]}
                save_templates(templates)
                st.success(f"Template '{new_template_name}' created!")
                selected_template = new_template_name

        # Edit selected template
