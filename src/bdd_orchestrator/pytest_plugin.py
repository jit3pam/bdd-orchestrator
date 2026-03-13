from __future__ import annotations

from pathlib import Path

import pytest

from bdd_orchestrator.analyzer import analyze_failure
from bdd_orchestrator.evidence import collect_failure_evidence


def pytest_addoption(parser: pytest.Parser) -> None:
    group = parser.getgroup("bdd-orchestrator")
    group.addoption(
        "--ai-debug",
        action="store_true",
        default=False,
        help="Enable AI-style failure diagnosis for failed Selenium/driver tests.",
    )
    group.addoption(
        "--ai-debug-dom-chars",
        action="store",
        default=3000,
        type=int,
        help="Maximum number of DOM characters to include in diagnosis output.",
    )
    group.addoption(
        "--ai-debug-screenshot-dir",
        action="store",
        default="reports/ai_debug",
        help="Directory where failure screenshots are stored when driver supports it.",
    )


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item: pytest.Item, call: pytest.CallInfo):
    outcome = yield
    report = outcome.get_result()

    if report.when != "call" or report.failed is False:
        return

    if not item.config.getoption("--ai-debug"):
        return

    screenshot_dir = item.config.getoption("--ai-debug-screenshot-dir")
    if screenshot_dir:
        Path(screenshot_dir).mkdir(parents=True, exist_ok=True)

    evidence = collect_failure_evidence(
        item,
        report,
        dom_char_limit=item.config.getoption("--ai-debug-dom-chars"),
        screenshot_dir=screenshot_dir,
    )

    diagnosis = analyze_failure(evidence)
    reporter = item.config.pluginmanager.get_plugin("terminalreporter")
    if reporter:
        reporter.write_line("\n" + diagnosis)
    else:
        print("\n" + diagnosis)
