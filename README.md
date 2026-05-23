# tiny‑todo‑cli

A super‑small command‑line todo list written in **Python 3**.

## Features
- Add, list, complete, and delete todo items.
- Persist data in a plain JSON file (`todo.json`) in the current directory.
- Zero‑dependency core (only `click` for the CLI, `pytest` & `flake8` for dev).

## Installation
```bash
# Clone the repo
git clone https://github.com/your‑org/tiny‑todo‑cli.git
cd tiny‑todo‑cli

# Install the CLI in an isolated environment
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

## Usage
```bash
# Add a new item
todo add "Buy milk"

# List all items
todo list

# Mark an item as done (by its index)
todo done 1

# Delete an item
todo delete 2
```

## Development
```bash
# Run the test suite
pytest

# Run linting
flake8 .
```

## CI/CD
The repository ships with a GitHub Actions workflow (`.github/workflows/ci.yml`) that:
- ✅ Runs on every push and pull‑request.
- 📦 Caches pip packages for fast builds.
- 🧪 Executes linting (`flake8`) and tests (`pytest`).
- 🔒 Uses full SHA pinning for all third‑party actions.
- 🛡️ Enforces least‑privilege permissions (read‑only `GITHUB_TOKEN`).

---
*Tiny project, big best‑practice footprint.*