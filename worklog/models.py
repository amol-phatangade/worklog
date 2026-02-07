from dataclasses import dataclass
from datetime import datetime

@dataclass
class Task:
    id: str
    time: str
    timestamp: str
    text: str

    @staticmethod
    def create(task_id: str, text: str, dt: datetime):
        return Task(
            id=task_id,
            time=dt.strftime("%H:%M"),
            timestamp=dt.isoformat(),
            text=text,
        )

