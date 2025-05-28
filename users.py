import json
import os

DATA_FILE = "users.json"

# Load or initialize data
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump({}, f)

def load_data():
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

def get_user_data(user_id):
    data = load_data()
    return data.get(str(user_id), {"reactions_used": 0})

def update_user_data(user_id, user_data):
    data = load_data()
    data[str(user_id)] = user_data
    save_data(data)

def increment_reaction(user_id):
    data = load_data()
    user_data = data.get(str(user_id), {"reactions_used": 0})
    user_data["reactions_used"] += 1
    data[str(user_id)] = user_data
    save_data(data)
