from __future__ import annotations

from bdd_orchestrator.evidence import FailureEvidence


def analyze_failure(evidence: FailureEvidence) -> str:
    """MVP analyzer.

    This provides deterministic, local analysis and serves as a drop-in
    replacement point for a real LLM-backed implementation.
    """
    lines = [
        "================ AI FAILURE ANALYSIS ================",
        f"Test: {evidence.test_id}",
        f"Failure Type: {evidence.exception_type}",
    ]

    msg = evidence.exception_message
    if "NoSuchElementException" in msg or "NoSuchElement" in msg:
        cause = "Target element was not found in the current DOM."
        fix = "Validate locator strategy, ensure waits, and confirm the page/iframe context."
    elif "TimeoutException" in msg or "timeout" in msg.lower():
        cause = "A UI or network operation exceeded the expected wait time."
        fix = "Increase explicit waits and validate expected conditions before interacting."
    else:
        cause = "Unhandled test failure; inspect stack trace and browser state."
        fix = "Review DOM and URL context, then re-check action order and assertions."

    lines.extend(
        [
            "",
            f"Probable Cause: {cause}",
            f"Suggested Fix: {fix}",
        ]
    )

    if evidence.url:
        lines.append(f"URL: {evidence.url}")
    if evidence.screenshot_path:
        lines.append(f"Screenshot: {evidence.screenshot_path}")
    if evidence.dom:
        lines.extend(["DOM Snippet:", evidence.dom[:500]])

    lines.append("====================================================")
    return "\n".join(lines)
