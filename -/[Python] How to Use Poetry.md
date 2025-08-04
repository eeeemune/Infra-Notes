# 💚 How to Use Poetry

## 💛 What is Poetry?

Poetry is a Python dependency and packaging tool.

It manages your project's **virtual environment, dependencies, and publishing** in one place.

- Currently we use `poetry` in chartmetric-data-script, data-utils, enterprise-data

## 💛 Quick Start

### 🤍 1. Install Poetry

Follow the [official installer](https://python-poetry.org/docs/)

- How to verify

```bash
poetry --version
```

### 🤍 2. Create a New Project

```bash
poetry new my-project
cd my-project
```

This makes a folder with:

- `pyproject.toml` (config + dependencies)
- basic package structure

### 🤍 3. Add Dependencies

```bash
poetry add requests
```

This:

- Adds `requests` to your project
- Updates `pyproject.toml`
- Updates lock file (`poetry.lock`)

For dev-only dependency:

```bash
poetry add --dev black
```

### 🤍 4. Install Everything (existing project)

```bash
poetry install
```

Creates/uses an isolated virtual environment and installs locked versions.

### 🤍 5. Run Commands Inside Environment

```bash
poetry run python script.py
poetry run pytest
```

Or spawn a shell in the environment:

```bash
poetry shell
```

### 🤍 6. Update Dependencies

```bash
poetry update
```

This refreshes the lock file to the newest allowed versions.

### 🤍 7. Check Dependency Graph

```bash
poetry show --tree
```

### 🤍 8. Publish Your Package

Prepare version in `pyproject.toml`, then:

```bash
poetry publish --build
```

You can publish to PyPI or a private repository (requires config/auth).

## 💛 Useful Extras

- Inspect current environment:
    
    ```bash
    poetry env info
    ```
    
- Use a specific Python version when creating project:
    
    ```bash
    poetry env use python3.11
    ```
    
- Export dependencies (e.g., for Docker):
    
    ```bash
    poetry export -f requirements.txt --output requirements.txt --without-hashes
    ```
    

## 💛 Workflow Example

<aside>

1. `poetry new webapp`
2. `cd webapp`
3. `poetry add flask`
4. `poetry run python -c "import flask; print(flask.__version__)"`
5. `poetry add --dev black`
6. `poetry run black .`
7. `poetry publish --build` (when ready)
</aside>
