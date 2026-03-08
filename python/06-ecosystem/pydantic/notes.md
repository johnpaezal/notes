# Python Pydantic

## Models
*Define and validate data with type hints*

```bash
pip install pydantic
```

```python
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    email: str
    age: int = 18       # default value

# Usage
user = User(id=1, name="Alice", email="alice@example.com")
user.name       # "Alice"
user.model_dump()   # {"id": 1, "name": "Alice", ...}

# From dict / JSON
user = User.model_validate({"id": 1, "name": "Alice", "email": "a@b.com"})
user = User.model_validate_json('{"id": 1, "name": "Alice", "email": "a@b.com"}')
```

---

## Type Coercion
*Pydantic converts types automatically*

```python
from pydantic import BaseModel

class Item(BaseModel):
    price: float
    quantity: int
    active: bool

# Usage
item = Item(price="9.99", quantity="3", active="true")
item.price      # 9.99   (float, not str)
item.quantity   # 3      (int, not str)
item.active     # True   (bool, not str)
```

---

## Validation
*Built-in and custom field validators*

```python
from pydantic import BaseModel, EmailStr, Field, field_validator

class User(BaseModel):
    name: str    = Field(min_length=2, max_length=50)
    age: int     = Field(ge=0, le=120)      # ge=≥, le=≤
    email: EmailStr                          # pip install pydantic[email]

    @field_validator("name")
    @classmethod
    def name_must_not_be_blank(cls, v):
        if not v.strip():
            raise ValueError("Name cannot be blank")
        return v.title()

# Usage
User(name="alice", age=25, email="alice@example.com")
# name → "Alice" (transformed)

User(name="a", age=25, email="alice@example.com")
# ValidationError: name must be at least 2 chars
```

---

## Nested Models
*Compose models within models*

```python
from pydantic import BaseModel
from typing import list

class Address(BaseModel):
    street: str
    city: str
    country: str = "US"

class User(BaseModel):
    name: str
    address: Address
    tags: list[str] = []

# Usage
user = User(
    name="Alice",
    address={"street": "123 Main St", "city": "NYC"},
    tags=["admin", "user"],
)
user.address.city   # "NYC"
```

---

## Optional & Union Types
*Handle nullable and multi-type fields*

```python
from pydantic import BaseModel

class Product(BaseModel):
    name: str
    description: str | None = None      # optional field
    price: float | int                  # accepts both

# Usage
Product(name="Laptop", price=999)           # description=None
Product(name="Laptop", description="Good")  # price required
```

---

## Serialization
*Export models to dict and JSON*

```python
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    password: str

user = User(id=1, name="Alice", password="secret")

user.model_dump()                           # all fields as dict
user.model_dump(exclude={"password"})       # {"id": 1, "name": "Alice"}
user.model_dump(include={"id", "name"})     # same result
user.model_dump_json()                      # JSON string
```

---

## Best Practices

**Inherit `BaseModel`** – Always use it as the base for data classes  
**`Field`** – Use for constraints, descriptions, and aliases  
**`model_dump(exclude=...)`** – Always exclude sensitive fields when serializing  
**Nested models** – Pass dicts directly; Pydantic auto-converts them  
**`pydantic-settings`** – Use `BaseSettings` for env/config (see `env-config/notes.md`)  
