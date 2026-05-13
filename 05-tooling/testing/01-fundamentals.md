# Testing Fundamentals
*Test types, strategy, and terminology*

## Test Types
*Levels of the testing pyramid*

**Unit Test** – Tests a single function/class in isolation; no I/O  
**Integration Test** – Tests how multiple units work together (DB, services)  
**E2E Test** – Tests full user flow from browser to database  
**Smoke Test** – Quick sanity check after deploy  
**Contract Test** – Verifies API contract between producer and consumer  

```
          /\
         /E2E\          slow, expensive, few
        /------\
       / Integr \       moderate
      /----------\
     /    Unit    \     fast, cheap, many
    /______________\
```

**Rule**: 70% unit / 20% integration / 10% E2E

---

## Test Structure (AAA)
*Arrange, Act, Assert pattern*

```python
def test_calculate_total():
    # Arrange — set up inputs
    items = [{"price": 10}, {"price": 20}]

    # Act — call the unit under test
    result = calculate_total(items)

    # Assert — verify the output
    assert result == 30
```

---

## Pytest Basics
*Python testing framework*

```bash
pip install pytest
pytest                    # run all tests
pytest tests/             # specific directory
pytest -k "test_user"     # filter by name
pytest -v                 # verbose output
pytest -x                 # stop on first failure
pytest --tb=short         # shorter tracebacks
```

```python
# test_users.py
import pytest

def test_create_user_success():
    user = create_user(name="Alice", email="a@a.com")
    assert user.id is not None
    assert user.name == "Alice"

def test_create_user_empty_name():
    with pytest.raises(ValueError):
        create_user(name="", email="a@a.com")

@pytest.mark.parametrize("name,expected", [
    ("alice", "Alice"),
    ("BOB", "Bob"),
])
def test_normalize_name(name, expected):
    assert normalize_name(name) == expected
```

---

## Fixtures
*Reusable test setup and teardown*

```python
import pytest

@pytest.fixture
def db():
    conn = create_test_db()
    yield conn          # provide to test
    conn.close()        # teardown after test

@pytest.fixture
def user(db):
    return db.insert(User(name="Alice"))

def test_get_user(db, user):
    result = db.find(user.id)
    assert result.name == "Alice"
```

---

## Mocking
*Replace dependencies with test doubles*

```python
from unittest.mock import MagicMock, patch

# Mock an object
email_service = MagicMock()
email_service.send.return_value = True

user_service = UserService(email_service=email_service)
user_service.register("alice@a.com")

email_service.send.assert_called_once_with("alice@a.com")

# Patch with context manager
with patch("myapp.services.send_email") as mock_send:
    mock_send.return_value = True
    register_user("alice@a.com")
    mock_send.assert_called_once()
```

**Mock** – Fake object; records calls and returns configured values  
**Patch** – Replaces a real import with a mock during the test  
**Spy** – Wraps real object; records calls without changing behavior  
