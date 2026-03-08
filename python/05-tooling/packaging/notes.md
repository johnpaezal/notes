# Python Packaging

## Virtual Environments
*Isolate project dependencies*

```bash
# Create
python -m venv .venv

# Activate
source .venv/bin/activate    # Linux/macOS
.venv\Scripts\activate       # Windows

# Deactivate
deactivate
```

---

## pip
*Install and manage packages*

```bash
pip install requests              # install
pip install requests==2.31.0      # specific version
pip install -r requirements.txt   # from file
pip uninstall requests
pip list                          # show installed
pip freeze > requirements.txt     # export
pip show requests                 # package info
```

---

## pyproject.toml
*Modern project configuration*

```toml
[build-system]
requires = ["setuptools>=68"]
build-backend = "setuptools.backends.legacy:build"

[project]
name = "myapp"
version = "1.0.0"
description = "My Python app"
requires-python = ">=3.11"
dependencies = [
    "requests>=2.31",
    "pydantic>=2.0",
]

[project.optional-dependencies]
dev = ["pytest", "ruff"]

[project.scripts]
myapp = "myapp.cli:main"
```

---

## Project Structure
*Standard layout for a Python package*

```
myapp/
├── src/
│   └── myapp/
│       ├── __init__.py
│       ├── main.py
│       └── utils.py
├── tests/
│   └── test_main.py
├── pyproject.toml
├── README.md
└── .gitignore
```

---

## Build & Publish
*Create and upload a package*

```bash
# Install build tools
pip install build twine

# Build distribution
python -m build          # creates dist/*.whl and dist/*.tar.gz

# Upload to PyPI
twine upload dist/*

# Upload to Test PyPI
twine upload --repository testpypi dist/*
```

---

## uv (Modern Tool)
*Fast Python package manager*

```bash
# Install uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# Create project
uv init myapp
uv venv
uv add requests          # add dependency
uv add --dev pytest      # dev dependency
uv run pytest            # run in venv
uv sync                  # install all from lockfile
```

---

## Best Practices

**Virtual env** – Always use one per project; never install globally  
**`pyproject.toml`** – Prefer over `setup.py` for new projects  
**Pin versions** – Use exact versions in `requirements.txt` for deployments  
**`src/` layout** – Prevents import confusion during development  
**`uv`** – Use for new projects; significantly faster than pip  
