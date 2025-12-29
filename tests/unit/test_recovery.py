import os
from unittest.mock import patch
import pytest
from bdd_orchestrator.recovery import manual_recovery


def test_manual_recovery_raises_when_disabled():
    os.environ["BDD_MANUAL_MODE"] = "false"
    with pytest.raises(Exception):
        manual_recovery("step", Exception("fail"))

def test_manual_recovery_pauses_when_enabled():
    os.environ["BDD_MANUAL_MODE"] = "true"

    with patch("builtins.input", return_value=""):
        manual_recovery("step", Exception("fail"))