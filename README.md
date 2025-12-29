# BDD Orchestrator

Step-level orchestration for BDD workflows using pytest.

## Features
- Step-level retry
- Manual intervention on failure (controlled by BDD_MANUAL_MODE)
- Works with pytest-bdd
- Generates Cucumber JSON & HTML reports

## Configure Pip configuration

[global]
extra-index-url = https://pip.pkg.github.com/jit3pam

## Usage

```bash
export BDD_MANUAL_MODE=true
pytest tests/bdd --cucumberjson=reports/cucumber/results.json
