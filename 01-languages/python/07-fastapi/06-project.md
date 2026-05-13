# FastAPI Project Setup
*Structure, config, and production deploy*

## Environment Variables
*Config with Pydantic Settings*

```bash
pip install pydantic-settings
```

```python
# config.py
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str
    secret_key: str
    debug: bool = False

    class Config:
        env_file = ".env"

settings = Settings()

# Usage
# .env file:
# DATABASE_URL=postgresql://user:pass@localhost/mydb
# SECRET_KEY=mysecret
# settings.database_url → loaded automatically
```

---

## Project Structure
*Recommended layout for a real API*

```
my-api/
├── main.py              ← app = FastAPI(), include routers
├── config.py            ← Settings (pydantic-settings)
├── database.py          ← engine, SessionLocal, Base, get_db
├── models/
│   └── user.py          ← SQLAlchemy models
├── schemas/
│   └── user.py          ← Pydantic schemas (request/response)
├── routers/
│   └── users.py         ← APIRouter per resource
├── dependencies.py      ← reusable Depends (auth, pagination)
├── requirements.txt
└── .env
```

**Rule** – `models/` for DB shape, `schemas/` for API shape — never mix them.

---

## Production Deploy
*Run with Gunicorn + Uvicorn workers*

```bash
pip install gunicorn uvicorn

# Recommended: Gunicorn managing Uvicorn workers
gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker -b 0.0.0.0:8000

# Uvicorn only (simpler, fewer workers)
uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4
```

**Never use `--reload` in production.**
