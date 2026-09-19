import json
import os

HIGHSCORE_FILE = "highscores.json"

def load_highscores():
    if not os.path.exists(HIGHSCORE_FILE):
        return {}
    with open(HIGHSCORE_FILE, "r") as f:
        return json.load(f)

def save_highscores(scores):
    with open(HIGHSCORE_FILE, "w") as f:
        json.dump(scores, f)