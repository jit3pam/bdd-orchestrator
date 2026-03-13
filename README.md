# BDD Orchestrator

Step-level orchestration and pytest plugin tooling for BDD workflows using pytest.

## Features
- Step-level retry via `run_step`
- Manual intervention on failure (controlled by `BDD_MANUAL_MODE`)
- Works with `pytest-bdd`
- Optional pytest plugin mode for AI-style failure diagnosis (`--ai-debug`)
- Generates Cucumber JSON & HTML reports

## Usage

### Step orchestrator in tests

```bash
export BDD_MANUAL_MODE=true
pytest tests/bdd --cucumberjson=reports/cucumber/results.json
```

### Plugin mode: AI-style failure diagnosis

```bash
pytest --ai-debug
```

Optional flags:

```bash
pytest --ai-debug \
  --ai-debug-dom-chars=3000 \
  --ai-debug-screenshot-dir=reports/ai_debug
```

When a test fails and a `driver` fixture is present, the plugin gathers exception details,
URL, DOM snippet, and an optional screenshot, then prints an AI-style diagnosis in terminal output.

## Example HTML results
https://jit3pam.github.io/bdd-orchestrator/
