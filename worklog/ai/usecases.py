USECASES = {
    "daily_summary": {
        "system": (
            "You are a staff software engineer assistant.\n"
            "Create a SHORT but COMPLETE daily work summary.\n\n"
            "Rules:\n"
            "- Use bullet points\n"
            "- Each bullet: 1 concise sentence\n"
            "- Focus on impact and collaboration\n"
            "- No filler text\n"
            "- No greetings\n"
        )
    },

    "weekly_summary": {
        "system": (
            "You are a staff software engineer assistant.\n"
            "Create a concise weekly status report.\n\n"
            "Format:\n"
            "Highlights:\n"
            "- 3–5 bullets\n\n"
            "Focus Areas:\n"
            "- 2–3 bullets\n\n"
            "Rules:\n"
            "- Short, clear bullets\n"
            "- Management-readable\n"
            "- No repetition\n"
        )
    },

    "analyze_time": {
        "system": (
            "You are a staff software engineer assistant.\n"
            "Analyze where time was spent.\n\n"
            "Output:\n"
            "- Top 3 categories with % estimate\n"
            "- 2 insights\n"
            "- 1 improvement suggestion\n"
        )
    },
}



def build_prompt(usecase_name: str, tasks: list[dict]) -> tuple[str, str]:
    if usecase_name not in USECASES:
        raise ValueError(f"Unknown AI usecase: {usecase_name}")

    system_prompt = USECASES[usecase_name]["system"]

    task_lines = [
        f"- {t['date']} {t['text']}"
        for t in tasks
    ]

    user_prompt = (
        "Here are my tasks:\n\n"
        + "\n".join(task_lines)
    )

    return system_prompt, user_prompt
