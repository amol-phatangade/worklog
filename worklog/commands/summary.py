from datetime import date
from worklog.storage.json_store import load_tasks


def run(args):
    if args.type == "daily":
        tasks = load_tasks(date=date.today().isoformat())
        title = "Daily Summary"

    elif args.type == "weekly":
        tasks = load_tasks(last_days=7)
        title = "Weekly Summary"

    elif args.type == "last":
        if not args.days:
            print("❌ --days is required for 'last'")
            return
        tasks = load_tasks(last_days=args.days)
        title = f"Last {args.days} Days Summary"

    else:
        print("Invalid summary type")
        return

    print(f"\n📌 {title}")
    print("-" * 40)

    if not tasks:
        print("No tasks found.")
        return

    for t in tasks:
        print(f"- {t['date']}: {t['text']}")
