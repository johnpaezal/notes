# FastAPI Pydantic & Responses
*Request validation and response control*

## Request Body with Pydantic
*Validate and type the request body*

```python
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class UserCreate(BaseModel):
    name: str
    email: str
    age: Optional[int] = None

class UserResponse(BaseModel):
    id: int
    name: str
    email: str

@app.post("/users", response_model=UserResponse)
def create_user(user: UserCreate):
    return {"id": 1, "name": user.name, "email": user.email}

# Usage
# POST /users  Body: {"name": "Alice", "email": "alice@example.com"}
# Missing "name" → 422 automatic
```

---

## Pydantic Models
*Advanced data validation*

```python
from pydantic import BaseModel, field_validator
from typing import Optional

class UserCreate(BaseModel):
    name: str
    email: str
    age: Optional[int] = None

    @field_validator("age")
    @classmethod
    def age_must_be_positive(cls, v):
        if v is not None and v < 0:
            raise ValueError("age must be positive")
        return v

class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None

# Usage
user = UserCreate(name="Alice", email="alice@example.com", age=25)
user.model_dump()       # → dict
user.model_dump_json()  # → JSON string
```

---

## Response Models
*Control which fields are returned*

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class UserInDB(BaseModel):
    id: int
    name: str
    email: str
    password_hash: str      # internal — must not be exposed

class UserResponse(BaseModel):
    id: int
    name: str
    email: str              # no password_hash

@app.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int):
    user = {"id": user_id, "name": "Alice", "email": "a@a.com", "password_hash": "xxx"}
    return user  # FastAPI filters extra fields automatically

# Usage
# GET /users/1 → {"id": 1, "name": "Alice", "email": "a@a.com"}
```

---

## Status Codes
*Set HTTP status codes on responses*

```python
from fastapi import FastAPI, status
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str

@app.post("/users", status_code=status.HTTP_201_CREATED)
def create_user(user: User):
    return {"id": 1, **user.model_dump()}

@app.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int):
    return None

# Usage
# POST   /users    → 201 Created
# DELETE /users/1  → 204 No Content
```

---

## HTTPException
*Return HTTP errors*

```python
from fastapi import FastAPI, HTTPException, status

app = FastAPI()

users = {1: {"id": 1, "name": "Alice"}}

@app.get("/users/{user_id}")
def get_user(user_id: int):
    user = users.get(user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return user

# Usage
# GET /users/99 → {"detail": "User not found"} 404
```
