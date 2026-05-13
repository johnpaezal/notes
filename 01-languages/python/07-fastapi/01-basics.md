# FastAPI Basics
*Modern async Python framework for APIs*

## What is FastAPI
*High-performance API framework*

**FastAPI** – Python framework with automatic validation, Swagger docs, and async support  
**Pydantic** – Data validation library used internally by FastAPI  
**ASGI** – Async Server Gateway Interface; enables FastAPI's async model  
**Uvicorn** – ASGI server used to run FastAPI

**Strengths**: Auto validation, auto Swagger/ReDoc docs, native async, static typing

### FastAPI vs Flask vs Django

| | FastAPI | Flask | Django |
|---|---|---|---|
| Performance | High (async) | Medium | Medium |
| Auto validation | Yes (Pydantic) | No | Partial |
| Auto docs | Yes (Swagger + ReDoc) | No | No |
| Learning curve | Medium | Low | High |
| Best for | Modern APIs | Simple prototypes | Full-stack apps |

---

## Setup
*Install and run*

```bash
pip install fastapi uvicorn

# Development (auto-reload)
uvicorn main:app --reload

# Custom port
uvicorn main:app --reload --port 8080

# Auto docs available at:
# http://localhost:8000/docs   ← Swagger UI
# http://localhost:8000/redoc  ← ReDoc
```

---

## Hello World
*Minimal app structure*

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello World"}

# Usage
# uvicorn main:app --reload
```

---

## Routes and HTTP Methods
*Define endpoints with decorators*

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/users")
def get_users():
    return [{"id": 1, "name": "Alice"}]

@app.post("/users")
def create_user():
    return {"id": 2, "name": "Bob"}

@app.put("/users/{user_id}")
def update_user(user_id: int):
    return {"id": user_id, "updated": True}

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    return {"deleted": user_id}

# Usage
# GET    /users
# POST   /users
# PUT    /users/42
# DELETE /users/42
```

---

## Path Parameters
*URL parameters with automatic type conversion*

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/users/{user_id}")
def get_user(user_id: int):     # FastAPI converts and validates the type
    return {"id": user_id}

@app.get("/items/{item_name}")
def get_item(item_name: str):
    return {"item": item_name}

# Usage
# GET /users/42   → user_id = 42 (int)
# GET /users/abc  → 422 Unprocessable Entity (not an int)
```

---

## Query Parameters
*Optional URL parameters*

```python
from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get("/users")
def get_users(
    page: int = 1,
    limit: int = 10,
    active: Optional[bool] = None,
):
    return {"page": page, "limit": limit, "active": active}

# Usage
# GET /users                → page=1, limit=10, active=None
# GET /users?page=2&limit=5 → page=2, limit=5
# GET /users?active=true    → active=True
```
