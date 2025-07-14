import os
import pickle
from typing import List

DATA_FILE = "./app/data/personas.pkl"

# Save one profile
def save_persona(profile):
    data = load_all_personas()
    data.append(profile)
    with open(DATA_FILE, "wb") as f:
        pickle.dump(data, f)

# Load all saved profiles

def load_all_personas():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "rb") as f:
        return pickle.load(f)