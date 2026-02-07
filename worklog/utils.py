from datetime import datetime, timedelta, date
import uuid

def generate_id() -> str:
    return uuid.uuid4().hex[:6]

def parse_date(d: str) -> date:
    return datetime.strptime(d, "%Y-%m-%d").date()

def daterange(days: int):
    today = date.today()
    return [today - timedelta(days=i) for i in range(days)]

