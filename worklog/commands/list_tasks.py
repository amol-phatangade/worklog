from worklog.storage.json_store import load_tasks


def run(args):
    """
    List tasks.
    Default: last 7 days
    Optional: specific date
    """
    tasks = load_tasks(date=args.date)

    if not tasks:
        print("No tasks found.")
        return

    for t in tasks:
        print(
            f"[{t['id']}] "
            f"{t['date']} "
            f"{t['timestamp'].split('T')[1]}  "
            f"{t['text']}"
        )
