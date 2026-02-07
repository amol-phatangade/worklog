import pytest
from pathlib import Path

from worklog.storage import json_store


@pytest.fixture
def temp_store(tmp_path):
    data_dir = tmp_path / ".worklog"
    json_store.set_data_dir(data_dir)
    return data_dir


@pytest.fixture
def sample_tasks(temp_store):
    tasks = [
        {
            "id": "a1",
            "date": "2026-02-01",
            "timestamp": "2026-02-01T10:00:00",
            "text": "Review PR for auth",
        },
        {
            "id": "b2",
            "date": "2026-02-02",
            "timestamp": "2026-02-02T11:00:00",
            "text": "Help DevOps with CI",
        },
    ]
    json_store.save_all_tasks(tasks)
    return tasks
