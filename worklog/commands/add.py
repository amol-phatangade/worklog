from datetime import datetime, date
from uuid import uuid4

from worklog.storage.json_store import load_all_tasks, save_all_tasks


def run(args):
    task_date = args.date or date.today().isoformat()

    task = {
        "id": str(uuid4())[:8],
        "date": task_date,
        "timestamp": datetime.now().isoformat(timespec="seconds"),
        "text": args.text,
    }

    tasks = load_all_tasks()
    tasks.append(task)
    save_all_tasks(tasks)

    print(f"✅ Added task [{task['id']}] {task['text']}")
