from worklog.storage.json_store import load_all_tasks, save_all_tasks


def run(args):
    tasks = load_all_tasks()

    for t in tasks:
        if t["id"] == args.id:
            print(f"Old: {t['text']}")
            new_text = input("New text: ").strip()

            if not new_text:
                print("❌ Empty text, aborting.")
                return

            t["text"] = new_text
            save_all_tasks(tasks)
            print("✅ Task updated.")
            return

    print("❌ Task ID not found.")
