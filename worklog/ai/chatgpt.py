from datetime import date

from worklog.ai.client import get_openai_client
from worklog.ai.usecases import build_prompt
from worklog.storage.json_store import load_tasks


MODEL = "gpt-4o-mini"  # fast + cheap; change anytime


def ai_summary(args):
    if args.type == "daily":
        tasks = load_tasks(date=date.today().isoformat())
        usecase = "daily_summary"

    elif args.type == "weekly":
        tasks = load_tasks(last_days=7)
        usecase = "weekly_summary"

    elif args.type == "last":
        tasks = load_tasks(last_days=args.days)
        usecase = "weekly_summary"

    else:
        raise ValueError("Invalid summary type")

    _run_ai(usecase, tasks, show_prompt=args.show_prompt)


def analyze_time(args):
    tasks = load_tasks(last_days=7)
    _run_ai("analyze_time", tasks)


def _run_ai(usecase: str, tasks: list[dict], show_prompt: bool = False):
    if not tasks:
        print("No tasks found for AI analysis.")
        return

    system_prompt, user_prompt = build_prompt(usecase, tasks)

    if show_prompt:
        print("\n🧠 System Prompt")
        print("-" * 60)
        print(system_prompt)
        print("\n👤 User Prompt")
        print("-" * 60)
        print(user_prompt)
        print("-" * 60)

    client = get_openai_client()

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        temperature=0.2,
        max_tokens=250,
    )

    print("\n🤖 AI Output")
    print("-" * 60)
    print(response.choices[0].message.content.strip())
