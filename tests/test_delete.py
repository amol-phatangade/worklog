from types import SimpleNamespace
from worklog.commands import delete
from worklog.storage.json_store import load_all_tasks


def test_delete_task(sample_tasks):
    args = SimpleNamespace(id="a1")
    delete.run(args)

    tasks = load_all_tasks()
    assert len(tasks) == 1
    assert tasks[0]["id"] == "b2"


def test_delete_invalid_id(sample_tasks, capsys):
    args = SimpleNamespace(id="x")
    delete.run(args)

    out = capsys.readouterr().out
    assert "not found" in out.lower()
