from worklog.storage.json_store import load_tasks


def run(args):
    tasks = load_tasks(date=args.date)

    matches = [
        t for t in tasks
        if args.query.lower() in t["text"].lower()
    ]

    if not matches:
        print("No matching tasks found.")
        return

    for t in matches:
        time = t["timestamp"].split("T")[1]
        print(f"[{t['id']}] {t['date']} {time}  {t['text']}")
