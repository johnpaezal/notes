# API Testing
*Testing HTTP endpoints with FastAPI and pytest*

## FastAPI TestClient
*In-process HTTP testing*

```python
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_users():
    response = client.get("/users")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_user():
    payload = {"name": "Alice", "email": "alice@example.com"}
    response = client.post("/users", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Alice"

def test_user_not_found():
    response = client.get("/users/99999")
    assert response.status_code == 404
    assert response.json()["detail"] == "User not found"
```

---

## Database Setup with Fixtures
*Isolated test database per test*

```python
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient
from main import app
from database import Base, get_db

TEST_DB = "sqlite:///./test.db"

@pytest.fixture(scope="function")
def db():
    engine = create_engine(TEST_DB, connect_args={"check_same_thread": False})
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()
    Base.metadata.drop_all(bind=engine)

@pytest.fixture
def client(db):
    app.dependency_overrides[get_db] = lambda: db
    yield TestClient(app)
    app.dependency_overrides.clear()
```

---

## Auth Testing
*Test protected endpoints*

```python
@pytest.fixture
def auth_headers(client):
    response = client.post("/token", data={
        "username": "alice",
        "password": "secret"
    })
    token = response.json()["access_token"]
    return {"Authorization": f"Bearer {token}"}

def test_get_me_authenticated(client, auth_headers):
    response = client.get("/me", headers=auth_headers)
    assert response.status_code == 200

def test_get_me_unauthenticated(client):
    response = client.get("/me")
    assert response.status_code == 401
```

---

## Best Practices
*Keep tests reliable and fast*

**Test one thing per test** – Single assertion per test function when possible  
**Descriptive names** – `test_create_user_returns_201`, not `test_1`  
**Isolate state** – Each test gets a fresh database; never share state  
**Test edge cases** – Empty inputs, missing fields, duplicates, not found  
**Don't test the framework** – Test your logic, not FastAPI internals  

```python
# Good: focused and clear
def test_delete_user_removes_from_db(client, db, existing_user):
    client.delete(f"/users/{existing_user.id}")
    assert db.query(User).filter_by(id=existing_user.id).first() is None

# Bad: testing multiple things at once
def test_user_crud(client):
    # create, get, update, delete all in one test
    ...
```
