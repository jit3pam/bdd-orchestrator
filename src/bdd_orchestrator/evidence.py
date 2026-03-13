from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass
class FailureEvidence:
    test_id: str
    phase: str
    exception_type: str
    exception_message: str
    url: str | None = None
    dom: str | None = None
    screenshot_path: str | None = None


def _safe_getattr(obj: Any, attr: str, default: Any = None) -> Any:
    try:
        return getattr(obj, attr)
    except Exception:
        return default


def collect_failure_evidence(
    item: Any,
    report: Any,
    *,
    dom_char_limit: int = 3000,
    screenshot_dir: str | None = None,
) -> FailureEvidence:
    exc = report.longreprtext if hasattr(report, "longreprtext") else str(report.longrepr)
    exc_type = "UnknownError"
    if hasattr(report, "longrepr") and hasattr(report.longrepr, "reprcrash"):
        exc_type = str(report.longrepr.reprcrash.message).split(":", 1)[0]

    driver = item.funcargs.get("driver") if hasattr(item, "funcargs") else None
    url = _safe_getattr(driver, "current_url") if driver is not None else None
    dom = _safe_getattr(driver, "page_source") if driver is not None else None
    if isinstance(dom, str):
        dom = dom[:dom_char_limit]

    screenshot_path = None
    if driver is not None and screenshot_dir:
        nodeid_slug = item.nodeid.replace("/", "_").replace("::", "__")
        screenshot_path = f"{screenshot_dir}/{nodeid_slug}.png"
        save_screenshot = _safe_getattr(driver, "save_screenshot")
        if callable(save_screenshot):
            try:
                save_screenshot(screenshot_path)
            except Exception:
                screenshot_path = None

    return FailureEvidence(
        test_id=getattr(item, "nodeid", "unknown"),
        phase=getattr(report, "when", "call"),
        exception_type=exc_type,
        exception_message=str(exc),
        url=url,
        dom=dom,
        screenshot_path=screenshot_path,
    )
