import json
from pathlib import Path
from datetime import date
from datetime import datetime, timedelta


DATA_DIR = Path.home() / ".worklog"
DATA_FILE = DATA_DIR / "tasks.json"


def set_data_dir(path: Path):
    global DATA_DIR, DATA_FILE
    DATA_DIR = path
    DATA_FILE = DATA_DIR / "tasks.json"

def ensure_data_dir():
    DATA_DIR.mkdir(parents=True, exist_ok=True)

def day_file(day: date) -> Path:
    return DATA_DIR / f"{day.isoformat()}.json"

def load_day(day: date) -> dict:
    ensure_data_dir()
    file = day_file(day)
    if not file.exists():
        return {"date": day.isoformat(), "tasks": []}
    return json.loads(file.read_text())

def save_day(day: date, data: dict):
    ensure_data_dir()
    day_file(day).write_text(json.dumps(data, indent=2))

def _ensure_store():
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    if not DATA_FILE.exists():
        DATA_FILE.write_text("[]")

def load_all_tasks():
    _ensure_store()
    with open(DATA_FILE, "r") as f:
        return json.load(f)


def save_all_tasks(tasks):
    _ensure_store()
    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f, indent=2)


def load_tasks(date=None, last_days=None):
    """
    Load tasks filtered by:
    - date (YYYY-MM-DD)
    - last_days (int)
    - default: last 7 days
    """
    tasks = load_all_tasks()

    if date:
        return [
            t for t in tasks
            if t["date"] == date
        ]

    if last_days:
        cutoff = datetime.now() - timedelta(days=last_days)
        return [
            t for t in tasks
            if datetime.fromisoformat(t["timestamp"]) >= cutoff
        ]

    # default → last week
    cutoff = datetime.now() - timedelta(days=7)
    return [
        t for t in tasks
        if datetime.fromisoformat(t["timestamp"]) >= cutoff
    ]