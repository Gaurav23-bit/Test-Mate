import json
import os

def load_history():
    if not os.path.exists("api_history.json"):
        return []
    with open("api_history.json", "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_to_history(method, url, status):
    history = load_history()
    entry = {"method": method, "url": url, "status": status}
    history.insert(0, entry)
    history = history[:10]
    with open("api_history.json", "w") as f:
        json.dump(history, f)