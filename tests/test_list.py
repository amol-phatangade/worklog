from types import SimpleNamespace
from worklog.commands import list_tasks


def test_list_tasks(sample_tasks, capsys):
    args = SimpleNamespace(date=None)
    list_tasks.run(args)

    out = capsys.readouterr().out
    assert "Review PR" in out
    assert "Help DevOps" in out
