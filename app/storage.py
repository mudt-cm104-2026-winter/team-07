"""Where the entries are kept.

For now: a Python list in memory. Simple, and it forgets everything when
the app restarts. That is fine for this stage.

The rest of the app only uses the functions below. Later in the semester
this file can be replaced by one that keeps the entries somewhere else.
As long as the function names stay the same, main.py does not change.
"""

import json

DATA_FILE = "data.json"


def save_score(new_score: int) -> int:
    """Saves a new score, updates data.json, and returns the current high score."""
    # 1. Load existing data or create default structure if file is missing
    try:
        with open(DATA_FILE, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {"scores": [], "high_score": 0}

    # 2. Add the new score to the list
    data["scores"].append(new_score)

    # 3. Calculate the new high score
    current_high = max(data["scores"])
    data["high_score"] = current_high

    # 4. Save back to data.json
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

    return current_high


def get_high_score() -> int:
    """Returns just the high score to display on the result page."""
    try:
        with open(DATA_FILE, "r") as file:
            data = json.load(file)
            return data.get("high_score", 0)
    except FileNotFoundError:
        return 0
