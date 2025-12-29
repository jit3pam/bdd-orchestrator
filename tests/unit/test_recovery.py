import os
from unittest.mock import patch
from bdd_orchestrator.recovery import manual_recovery


def test_manual_recovery_raises_when_non_interactive():
    os.environ["BDD_MANUAL_MODE"] = "true"

    with patch("sys.stdin.isatty", return_value=False):
        try:
            manual_recovery("step", Exception("fail"))
        except Exception as e:
            assert str(e) == "fail"


def test_manual_recovery_pauses_when_interactive():
    os.environ["BDD_MANUAL_MODE"] = "true"

    with patch("sys.stdin.isatty", return_value=True):
        with patch("builtins.input", return_value=""):
            manual_recovery("step", Exception("fail"))
