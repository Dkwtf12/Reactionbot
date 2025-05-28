import json
import os

DATA_FILE = "users.json"

if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump({}, f)

def get_user_data(user_id):
    with open(DATA_FILE, "r") as f:
        data = json.load(f)
    return data.get(str(user_id), {"verified": False, "reactions": {}})

def update_user_data(user_id, key, value):
    with open(DATA_FILE, "r") as f:
        data = json.load(f)
    user_id = str(user_id)
    if user_id not in data:
        data[user_id] = {"verified": False, "reactions": {}}
    data[user_id][key] = value
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

def increment_reaction(user_id, emoji, count):
    with open(DATA_FILE, "r") as f:
        data = json.load(f)
    user_id = str(user_id)
    if user_id not in data:
        data[user_id] = {"verified": False, "reactions": {}}
    reactions = data[user_id].get("reactions", {})
    reactions[emoji] = reactions.get(emoji, 0) + count
    data[user_id]["reactions"] = reactions
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)
