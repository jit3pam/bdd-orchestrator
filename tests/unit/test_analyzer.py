from bdd_orchestrator.analyzer import analyze_failure
from bdd_orchestrator.evidence import FailureEvidence


def test_analyze_failure_reports_nosuchelement_guidance():
    evidence = FailureEvidence(
        test_id="tests/test_ui.py::test_login",
        phase="call",
        exception_type="NoSuchElementException",
        exception_message="NoSuchElementException: unable to locate element",
        url="https://example.test/login",
        dom="<button class='primary-login'>Sign in</button>",
    )

    result = analyze_failure(evidence)

    assert "AI FAILURE ANALYSIS" in result
    assert "NoSuchElementException" in result
    assert "Target element was not found" in result
    assert "primary-login" in result
