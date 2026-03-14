# Python Testing

## pytest Basics
*Run and discover tests automatically*

```python
# test_math.py
def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5

def test_add_negative():
    assert add(-1, 1) == 0
```

```bash
pytest              # run all tests
pytest test_math.py # run specific file
pytest -v           # verbose output
pytest -k "add"     # run tests matching name
```

---

## Assertions
*Verify expected behavior*

```python
def test_examples():
    assert 1 + 1 == 2
    assert "hello".upper() == "HELLO"
    assert [1, 2, 3] == [1, 2, 3]
    assert "py" in "python"

def test_raises():
    import pytest
    with pytest.raises(ZeroDivisionError):
        1 / 0

    with pytest.raises(ValueError, match="invalid"):
        int("abc")
```

---

## Fixtures
*Reusable setup for tests*

```python
import pytest

@pytest.fixture
def user():
    return {"name": "Alice", "age": 25}

@pytest.fixture
def db():
    conn = connect_db()
    yield conn          # setup
    conn.close()        # teardown (after yield)

# Usage
def test_user_name(user):
    assert user["name"] == "Alice"

def test_query(db):
    result = db.query("SELECT 1")
    assert result is not None
```

---

## Parametrize
*Run one test with multiple inputs*

```python
import pytest

@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (0, 0, 0),
    (-1, 1, 0),
])
def test_add(a, b, expected):
    assert a + b == expected
```

---

## Mocking
*Replace real dependencies with fakes*

```python
from unittest.mock import MagicMock, patch

# Mock an object
def test_send_email():
    email_service = MagicMock()
    email_service.send("user@example.com", "Hello")
    email_service.send.assert_called_once()

# Patch a module-level function
def get_price():
    return fetch_from_api()   # real API call

def test_get_price():
    with patch("mymodule.fetch_from_api", return_value=99.9):
        assert get_price() == 99.9
```

---

## Markers
*Tag and control test execution*

```python
import pytest

@pytest.mark.skip(reason="not ready")
def test_wip():
    pass

@pytest.mark.skipif(sys.platform == "win32", reason="unix only")
def test_unix():
    pass

@pytest.mark.slow
def test_heavy_computation():
    pass
```

```bash
pytest -m slow          # run only "slow" tests
pytest -m "not slow"    # skip "slow" tests
```

---

## Best Practices

**Name tests clearly** – `test_user_login_with_invalid_password`  
**One assertion per test** – easier to diagnose failures  
**Fixtures** – use for setup/teardown, not global state  
**`patch`** – always patch at the import location, not the source  
**Parametrize** – use instead of duplicating test logic  
