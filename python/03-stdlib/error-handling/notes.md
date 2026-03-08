# Python Error Handling

## try / except
*Catch and handle exceptions*

```python
# Basic
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")

# Multiple exceptions
try:
    value = int("abc")
except (ValueError, TypeError) as e:
    print(f"Error: {e}")

# Catch any exception
try:
    risky_operation()
except Exception as e:
    print(type(e).__name__, e)
```

---

## try / except / else / finally
*Full exception handling structure*

**`else`** – Runs if no exception occurred  
**`finally`** – Always runs (cleanup)

```python
try:
    file = open("data.txt")
    data = file.read()
except FileNotFoundError:
    print("File not found")
else:
    process(data)           # only if no exception
finally:
    file.close()            # always runs
```

---

## Raising Exceptions
*Throw exceptions manually*

```python
def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age

# Re-raise
try:
    risky()
except Exception:
    log_error()
    raise              # re-raise same exception

# Raise with context (preserves chain)
try:
    connect_db()
except ConnectionError as e:
    raise RuntimeError("DB unavailable") from e
```

---

## Custom Exceptions
*Define your own exception types*

```python
class AppError(Exception):
    pass

class ValidationError(AppError):
    def __init__(self, field, message):
        self.field = field
        super().__init__(f"{field}: {message}")

class NotFoundError(AppError):
    pass

# Usage
raise ValidationError("email", "Invalid format")

try:
    risky()
except ValidationError as e:
    print(e.field, str(e))
except AppError as e:
    print("App error:", e)
```

---

## Exception Hierarchy
*Built-in exception types*

```
BaseException
├── SystemExit
├── KeyboardInterrupt
└── Exception
    ├── ValueError        – wrong value
    ├── TypeError         – wrong type
    ├── KeyError          – missing dict key
    ├── IndexError        – index out of range
    ├── AttributeError    – missing attribute
    ├── NameError         – undefined variable
    ├── FileNotFoundError
    ├── ZeroDivisionError
    ├── RecursionError
    └── RuntimeError
```

---

## Context Managers for Cleanup
*Safer resource management*

```python
# with auto-closes resources even on exception
with open("file.txt") as f:
    data = f.read()

# Multiple contexts
with open("in.txt") as src, open("out.txt", "w") as dst:
    dst.write(src.read())
```

> See `file-io/notes.md` for full file I/O patterns.

---

## Best Practices

**Specificity** – Catch specific exceptions, never bare `except:`  
**Cleanup** – Use `finally` or `with` for resource release  
**Chaining** – Use `raise ... from e` to preserve exception context  
**Custom exceptions** – Inherit from `Exception`, not `BaseException`  
**Logging** – Log before swallowing exceptions
