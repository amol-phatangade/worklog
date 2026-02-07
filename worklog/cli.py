# worklog/cli.py
import argparse
from worklog.commands import (
    add,
    list_tasks,
    edit,
    delete,
    search,
    summary,
)
from worklog.ai import chatgpt


def main():
    parser = argparse.ArgumentParser(
        prog="worklog",
        description="Personal CLI tool to track daily work and generate summaries",
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    # -------- add --------
    add_parser = subparsers.add_parser(
        "add", help="Add a new work task"
    )
    add_parser.add_argument(
        "text", help="Task description"
    )
    add_parser.add_argument(
        "--date", help="Task date (YYYY-MM-DD). Defaults to today."
    )
    add_parser.set_defaults(func=add.run)

    # -------- list --------
    list_parser = subparsers.add_parser(
        "list", help="List tasks"
    )
    list_parser.add_argument(
        "--date", help="List tasks for a specific date"
    )
    list_parser.set_defaults(func=list_tasks.run)

    # -------- edit --------
    edit_parser = subparsers.add_parser(
        "edit", help="Edit an existing task"
    )
    edit_parser.add_argument("id", help="Task ID")
    edit_parser.set_defaults(func=edit.run)

    # -------- delete --------
    delete_parser = subparsers.add_parser(
        "delete", help="Delete a task"
    )
    delete_parser.add_argument("id", help="Task ID")
    delete_parser.set_defaults(func=delete.run)

    # -------- search --------
    search_parser = subparsers.add_parser(
        "search", help="Search tasks by keyword"
    )
    search_parser.add_argument("query", help="Search string")
    search_parser.add_argument(
        "--date", help="Search within a specific date or range"
    )
    search_parser.set_defaults(func=search.run)

    # -------- summary --------
    summary_parser = subparsers.add_parser(
        "summary", help="Generate summaries"
    )
    summary_parser.add_argument(
        "type",
        choices=["daily", "weekly", "last"],
        help="Summary type",
    )
    summary_parser.add_argument(
        "--days",
        type=int,
        help="Number of days (used with 'last')",
    )
    summary_parser.set_defaults(func=summary.run)

    # -------- AI --------
    ai_parser = subparsers.add_parser(
        "ai", help="AI-powered insights"
    )
    ai_sub = ai_parser.add_subparsers(dest="ai_command", required=True)

    ai_summary = ai_sub.add_parser(
        "summary", help="AI-generated summaries"
    )
    ai_summary.add_argument(
        "type", choices=["daily", "weekly", "last"]
    )
    ai_summary.add_argument(
        "--days", type=int
    )
    ai_summary.add_argument(
        "--show-prompt",
        action="store_true",
        help="Show the prompt sent to ChatGPT"
    )

    ai_summary.set_defaults(func=chatgpt.ai_summary)

    ai_analyze = ai_sub.add_parser(
        "analyze-time",
        help="Analyze where most time was spent"
    )

    ai_analyze.set_defaults(func=chatgpt.analyze_time)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
