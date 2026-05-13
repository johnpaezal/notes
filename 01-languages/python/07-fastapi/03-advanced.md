# FastAPI Advanced Features
*Async, dependencies, routers, middleware*

## Async / Await
*Async endpoints for concurrent I/O*

```python
from fastapi import FastAPI
import httpx

app = FastAPI()

@app.get("/async-example")
async def async_example():
    async with httpx.AsyncClient() as client:
        response = await client.get("https://api.example.com/data")
    return response.json()

# Rule: async I/O (async DB, async HTTP) → use async def
#       sync code (classic SQLAlchemy, CPU ops) → use def
```

---

## Dependencies (Dependency Injection)
*Reuse logic across endpoints*

```python
from fastapi import FastAPI, Depends, HTTPException, Header
from typing import Optional

app = FastAPI()

def get_current_user(authorization: Optional[str] = Header(None)):
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Not authenticated")
    token = authorization.split(" ")[1]
    return {"user_id": 1, "token": token}

def pagination(page: int = 1, limit: int = 10):
    return {"skip": (page - 1) * limit, "limit": limit}

@app.get("/users")
def get_users(
    current_user: dict = Depends(get_current_user),
    pages: dict = Depends(pagination),
):
    return {"user": current_user, "pagination": pages}

# Usage
# GET /users?page=2&limit=5
# Headers: Authorization: Bearer mytoken
```

---

## Routers
*Split endpoints into separate modules*

```
project/
├── main.py
└── routers/
    ├── users.py
    └── products.py
```

```python
# routers/users.py
from fastapi import APIRouter

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/")
def get_users():
    return []

@router.get("/{user_id}")
def get_user(user_id: int):
    return {"id": user_id}
```

```python
# main.py
from fastapi import FastAPI
from routers import users, products

app = FastAPI()
app.include_router(users.router)
app.include_router(products.router)

# Usage
# GET /users/    → get_users
# GET /users/42  → get_user
```

---

## Middleware
*Run logic before/after every request*

```python
from fastapi import FastAPI, Request
import time

app = FastAPI()

@app.middleware("http")
async def add_process_time(request: Request, call_next):
    start = time.time()
    response = await call_next(request)
    duration = time.time() - start
    response.headers["X-Process-Time"] = str(duration)
    return response

# Usage
# Every response includes X-Process-Time header
```

---

## CORS
*Allow requests from other domains*

```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "https://myfrontend.com"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# allow_origins=["*"] for development only — never in production
```

---

## Background Tasks
*Run tasks after responding to the client*

```python
from fastapi import FastAPI, BackgroundTasks

app = FastAPI()

def send_email(email: str, message: str):
    print(f"Sending email to {email}: {message}")

@app.post("/users")
def create_user(email: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(send_email, email, "Welcome!")
    return {"message": "User created"}

# Usage
# POST /users?email=alice@example.com
# Responds immediately, sends email in the background
```
