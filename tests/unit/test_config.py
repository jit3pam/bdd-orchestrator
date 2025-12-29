import os
from bdd_orchestrator.config import manual_mode_enabled


def test_manual_mode_disabled_by_default():
    os.environ.pop("BDD_MANUAL_MODE", None)
    assert manual_mode_enabled() is False


def test_manual_mode_enabled():
    os.environ["BDD_MANUAL_MODE"] = "true"
    assert manual_mode_enabled() is True
