from pathlib import Path
import json

CONFIG_DIR = Path.home() / ".config" / "worklog"
CONFIG_FILE = CONFIG_DIR / "config.json"
AI_USECASES_FILE = CONFIG_DIR / "ai_usecases.json"

def ensure_config():
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    if not CONFIG_FILE.exists():
        CONFIG_FILE.write_text(json.dumps({}, indent=2))
    if not AI_USECASES_FILE.exists():
        AI_USECASES_FILE.write_text(json.dumps({}, indent=2))

