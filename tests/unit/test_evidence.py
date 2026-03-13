from types import SimpleNamespace

from bdd_orchestrator.evidence import collect_failure_evidence


class DummyDriver:
    current_url = "https://example.test/login"
    page_source = "<html><body><button id='login-btn'>Login</button></body></html>"

    def __init__(self):
        self.saved_paths = []

    def save_screenshot(self, path):
        self.saved_paths.append(path)
        return True


def test_collect_failure_evidence_with_driver_and_screenshot_dir(tmp_path):
    driver = DummyDriver()
    item = SimpleNamespace(nodeid="tests/test_login.py::test_login", funcargs={"driver": driver})
    report = SimpleNamespace(
        when="call",
        longreprtext="NoSuchElementException: fail",
        longrepr=SimpleNamespace(
            reprcrash=SimpleNamespace(message="NoSuchElementException: fail")
        ),
    )

    evidence = collect_failure_evidence(
        item,
        report,
        dom_char_limit=20,
        screenshot_dir=str(tmp_path),
    )

    assert evidence.test_id == "tests/test_login.py::test_login"
    assert evidence.url == "https://example.test/login"
    assert evidence.dom == "<html><body><button "
    assert evidence.screenshot_path is not None
    assert driver.saved_paths
