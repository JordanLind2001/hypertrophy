import streamlit as st
import json
from pathlib import Path

# File paths (Streamlit Cloud writes to /app)
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
    with open(TEMPLATE_F_
