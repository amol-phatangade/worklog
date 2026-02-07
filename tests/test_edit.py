from types import SimpleNamespace
from worklog.commands import edit
from worklog.storage.json_store import load_all_tasks


def test_edit_task(sample_tasks, monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "Updated task")

    args = SimpleNamespace(id="a1")
    edit.run(args)

    tasks = load_all_tasks()
    assert tasks[0]["text"] == "Updated task"


def test_edit_invalid_id(sample_tasks, capsys):
    args = SimpleNamespace(id="invalid")
    edit.run(args)

    out = capsys.readouterr().out
    assert "not found" in out.lower()
