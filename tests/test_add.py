from types import SimpleNamespace
from worklog.commands import add
from worklog.storage.json_store import load_all_tasks


def test_add_task(temp_store):
    args = SimpleNamespace(
        text="Write unit tests",
        date=None,
    )

    add.run(args)

    tasks = load_all_tasks()
    assert len(tasks) == 1
    assert tasks[0]["text"] == "Write unit tests"
