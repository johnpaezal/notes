# Project Structure

## .env Pattern
*Separate secrets from code*

**`.env`** – Local file with real secrets, never committed  
**`.env.example`** – Committed template with placeholder values  
**`.gitignore`** – Must include `.env` to prevent leaks  

```bash
# .env.example (committed)
DATABASE_URL=postgres://user:password@localhost:5432/mydb
SECRET_KEY=your-secret-key-here
AWS_ACCESS_KEY_ID=AKIAIOSFODNN7EXAMPLE
AWS_REGION=us-east-1

# Usage: cp .env.example .env  then fill real values
```

---

## .gitignore Essentials
*Files that must never commit*

```gitignore
# Secrets
.env

# Python
__pycache__/
*.pyc
.venv/
*.egg-info/

# Node
node_modules/

# OS
.DS_Store

# Logs & build
*.log
dist/
build/

# Terraform
.terraform/
*.tfstate
*.tfstate.backup

# Usage: place at repo root, commit it
```

---

## Python Project Structure
*Src layout vs flat layout*

**Src layout** – Package under `src/`, prevents accidental imports from root  
**Flat layout** – Package at root, simpler but riskier for large projects  
**`pyproject.toml`** – Modern standard, replaces `setup.py`, includes build metadata  
**`requirements.txt`** – Pinned production deps (`pip freeze > requirements.txt`)  
**`requirements-dev.txt`** – Dev-only deps (pytest, black, mypy, ruff)  

```
# Src layout (recommended)
my-project/
├── src/
│   └── my_package/
│       ├── __init__.py
│       ├── main.py
│       └── config.py
├── tests/
│   └── test_main.py
├── pyproject.toml
├── requirements.txt
├── requirements-dev.txt
└── .env.example

# Usage: pip install -e ".[dev]"  (editable install with dev extras)
```

---

## Java/Spring Boot Project Structure
*Standard Maven layout*

**`src/main/java`** – Application source code  
**`src/main/resources`** – Config files (`application.yml`, static assets)  
**`src/test/java`** – Unit and integration tests  

```
my-service/
├── src/
│   ├── main/
│   │   ├── java/com/example/myservice/
│   │   │   ├── MyServiceApplication.java
│   │   │   ├── controller/
│   │   │   ├── service/
│   │   │   ├── repository/
│   │   │   └── dto/
│   │   └── resources/
│   │       ├── application.yml
│   │       └── application-prod.yml
│   └── test/java/com/example/myservice/
├── pom.xml
└── .env.example

# Usage: mvn spring-boot:run
```

---

## README.md Anatomy
*Minimal viable documentation*

**Project name + one-line description** – What it does, at the top  
**Prerequisites** – Runtime versions (Python 3.11+, Java 17+, Docker)  
**Install** – Exact commands to set up from scratch  
**Run** – Commands for dev and prod modes  
**Env vars table** – Variable, description, required/optional, example value  
**API endpoints summary** – Method, path, description (short table)  
**Deploy notes** – Platform, branch strategy, CI trigger  

```markdown
# my-service
One-line description of what this does.

## Prerequisites
- Python 3.11+
- PostgreSQL 15

## Install
cp .env.example .env
pip install -r requirements-dev.txt

## Run
uvicorn src.main:app --reload

## Environment Variables
| Variable     | Description        | Required |
|--------------|--------------------|----------|
| DATABASE_URL | PostgreSQL conn URL | Yes      |
| SECRET_KEY   | JWT signing key     | Yes      |

# Usage: keep README.md at repo root, always up to date
```
