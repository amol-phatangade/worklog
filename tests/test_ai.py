from types import SimpleNamespace
from worklog.ai import chatgpt


def test_ai_summary(sample_tasks, capsys):
    args = SimpleNamespace(type="weekly", days=None)
    chatgpt.ai_summary(args)

    out = capsys.readouterr().out
    assert "AI Prompt" in out


def test_ai_analyze_time(sample_tasks, capsys):
    args = SimpleNamespace()
    chatgpt.analyze_time(args)

    out = capsys.readouterr().out
    assert "Analyze" in out
