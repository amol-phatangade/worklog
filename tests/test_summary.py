from types import SimpleNamespace
from worklog.commands import summary


def test_weekly_summary(sample_tasks, capsys):
    args = SimpleNamespace(type="weekly", days=None)
    summary.run(args)

    out = capsys.readouterr().out
    assert "Weekly Summary" in out
    assert "Review PR" in out


def test_last_summary_requires_days(capsys):
    args = SimpleNamespace(type="last", days=None)
    summary.run(args)

    out = capsys.readouterr().out
    assert "--days" in out
