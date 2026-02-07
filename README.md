# worklog

`worklog` is a **local-first, command-line work tracking tool** designed for engineers who want:
- Zero cloud exposure
- Fast daily task capture
- Grep-like search over work history
- Clean daily / weekly summaries
- Optional AI-generated summaries (opt-in)

It behaves like a personal, private version of Airtable — but runs entirely on your machine.

---

## ✨ Features

- ✅ Day-wise task storage (JSON, human-readable)
- ✅ Automatic timestamps
- ✅ Add tasks for **today or past dates**
- ✅ Edit / delete logged tasks
- ✅ Grep-like search (default: last 7 days)
- ✅ Daily & weekly summaries
- ✅ CLI-first, scriptable
- ✅ No database, no server, no vendor lock-in
- 🚧 AI summaries (pluggable, opt-in)

---

## 🧠 Design Philosophy

- **Local first**: all data stored on your machine
- **Explicit AI usage**: nothing sent unless you ask
- **Unix-style CLI**: composable, predictable
- **Simple storage**: one JSON file per day
- **Clean code structure**: easy to extend

---

## 📦 Project Structure

worklog/
├── worklog/ # Python package
├── pyproject.toml
├── README.md


Runtime data:


~/.worklog/
├── 2026-02-01.json
├── 2026-02-02.json


Config:


~/.config/worklog/
├── config.json
├── ai_usecases.json


---

## 🔧 Requirements

- Python **3.10+**
- macOS or Linux
- pip

Check:
```bash
python3 --version

🚀 Build & Install (Local Machine)
1️⃣ Clone the repository
git clone <repo-url>
cd worklog

2️⃣ Create a virtual environment (recommended)
python3 -m venv .venv
source .venv/bin/activate

3️⃣ Install the tool locally
pip uninstall worklog -y
pip install -e .


This installs worklog as a system command:

worklog --help


You can now use it like:

worklog add "Reviewed PR"

4️⃣ (Optional) Global install without venv

If you prefer a global command:

pip install .


or with user scope:

pip install --user .


Make sure ~/.local/bin is in your PATH.

🧪 Verify Installation
which worklog
worklog --version

📘 Usage Guide
➕ Add a Task (Today)
worklog add "Help DevOps with XYZ deployment issue"


Automatically:

Uses today’s date

Records current time

➕ Add Task for Past Date
worklog add "Reviewed legacy PR" --date 2026-02-01 --time 11:30

📋 List Tasks (Specific Day)
worklog list --date 2026-02-01


Output:

7f9a 11:30  Reviewed legacy PR
8a2d 15:10  Helped DevOps with deployment issue

✏️ Edit a Task
worklog edit 7f9a "Reviewed and approved legacy PR" --date 2026-02-01

🗑 Delete a Task
worklog delete 7f9a --date 2026-02-01

🔍 Search Tasks (Grep-like)
Default (last 7 days)
worklog search DevOps

Last N days
worklog search RPM --days 14

Specific date
worklog search PR --date 2026-02-02


Output:

2026-02-02 14:10 [8a2d] Reviewed PR for installer

📊 Daily Summary
worklog summary-daily


Output:

Daily Summary – 2026-02-06

- Helped DevOps with deployment issue
- Reviewed PR for feature ABC

📅 Weekly Summary
worklog summary-weekly


Output:

Weekly Summary

- Supported DevOps on deployment tasks
- Reviewed multiple PRs
- Investigated RPM conflicts

Data Format

Each day is stored as one JSON file:

{
  "date": "2026-02-06",
  "tasks": [
    {
      "id": "8a2d",
      "time": "14:10",
      "timestamp": "2026-02-06T14:10:03",
      "text": "Reviewed PR for feature ABC"
    }
  ]
}


You can:

Open it

Edit it manually

Commit it to Git (optional)

🔐 Privacy & Security

No network calls by default

No telemetry

AI usage is explicit (future feature)

API keys stored locally only

🧹 Uninstall
pip uninstall worklog


Remove data:

rm -rf ~/.worklog ~/.config/worklog

🛣 Roadmap

AI summaries (daily / weekly / last N days)

Custom AI use cases

Prompt preview (--dry-run)

Local LLM support (Ollama)

SQLite backend (optional)

Export to Markdown / Email

🧑‍💻 Author Notes

This tool is designed for individual engineers who value:

Focus

Privacy

Minimal overhead

Long-term personal leverage

Contributions welcome — but it’s also perfectly fine as a personal internal tool.


---

## ✅ What’s Next

Next steps we can do **incrementally and cleanly**:

1️⃣ Add **AI use-case system + ChatGPT integration**  
2️⃣ Add **last N days summary**  
3️⃣ Add **prompt dry-run & preview**  
4️⃣ Polish CLI UX (colors, grouping, tags)

Just say:

> **Next: AI summaries**

and we’ll extend the code properly without breaking anything.


## some commands
worklog -h
worklog add "Manual test task"
worklog list
worklog search Manual
worklog summary weekly

worklog ai summary daily
worklog ai summary weekly
worklog ai summary last --days 10
worklog ai analyze-time


Keep AI instructions customizable, will add later:
worklog ai summary weekly --usecase staff-weekly

alias wa='worklog add'
alias we='worklog edit'
alias wd='worklog delete'
alias wl='worklog list'
alias ws='worklog ai summary daily'
alias ww='worklog ai summary weekly'
alias wt='worklog ai analyze-time'

