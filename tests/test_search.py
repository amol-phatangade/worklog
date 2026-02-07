from types import SimpleNamespace
from worklog.commands import search


def test_search_match(sample_tasks, capsys):
    args = SimpleNamespace(query="devops", date=None)
    search.run(args)

    out = capsys.readouterr().out
    assert "DevOps" in out


def test_search_no_match(sample_tasks, capsys):
    args = SimpleNamespace(query="nothing", date=None)
    search.run(args)

    out = capsys.readouterr().out
    assert "no matching" in out.lower()
