import json
import os

def save_memory(messages, filename="memory.json"):
    with open(filename, "w") as f:
        json.dump(messages, f)

def load_memory(filename="memory.json"):
    if os.path.exists(filename):
        with open(filename, "r") as f:
            return json.load(f)
    return []
