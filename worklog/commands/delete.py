from worklog.storage.json_store import load_all_tasks, save_all_tasks


def run(args):
    tasks = load_all_tasks()
    new_tasks = [t for t in tasks if t["id"] != args.id]

    if len(tasks) == len(new_tasks):
        print("❌ Task ID not found.")
        return

    save_all_tasks(new_tasks)
    print(f"🗑️ Deleted task {args.id}")
