# Python Debugging

## print Debugging
*Quick inspection of values*

```python
# Basic
print(f"value = {value!r}")     # !r shows type info
print(f"type  = {type(value)}")

# Debug print with context
def debug(label, value):
    print(f"[DEBUG] {label}: {value!r}")

# Usage
debug("user", user)
debug("result", result)
```

---

## breakpoint()
*Drop into interactive debugger*

```python
def process_order(order):
    total = sum(item["price"] for item in order["items"])
    breakpoint()        # execution pauses here → pdb prompt
    return apply_tax(total)
```

### pdb Commands
*Navigate the debugger*

| Command | Action |
|---------|--------|
| `n` | Next line (step over) |
| `s` | Step into function |
| `c` | Continue to next breakpoint |
| `p expr` | Print expression |
| `pp expr` | Pretty-print expression |
| `l` | Show current code |
| `bt` | Show call stack |
| `q` | Quit debugger |

---

## Logging for Debugging
*Structured debug output*

```python
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def fetch_user(user_id):
    logger.debug(f"Fetching user {user_id}")
    user = db.get(user_id)
    logger.debug(f"Found: {user!r}")
    return user
```

> See `logging/notes.md` for full logging setup.

---

## traceback
*Inspect and format exceptions*

```python
import traceback

try:
    risky_operation()
except Exception:
    traceback.print_exc()           # print to stderr
    tb = traceback.format_exc()     # get as string
    logger.error(tb)
```

---

## Profiling
*Find performance bottlenecks*

```python
import cProfile

# Profile entire script
cProfile.run("my_function()")

# Profile with output file
cProfile.run("my_function()", "output.prof")
```

```bash
# View profile results
python -m pstats output.prof
# or
snakeviz output.prof     # pip install snakeviz
```

### timeit
*Measure execution time of small snippets*

```python
import timeit

timeit.timeit("'-'.join(str(n) for n in range(100))", number=10000)

# In shell
# python -m timeit "'-'.join(str(n) for n in range(100))"
```

---

## assert
*Catch unexpected state during development*

```python
def set_age(age):
    assert isinstance(age, int), f"Expected int, got {type(age)}"
    assert age >= 0, f"Age must be non-negative, got {age}"
    return age

# Usage
set_age(25)     # ok
set_age(-1)     # AssertionError: Age must be non-negative, got -1
```

> Run with `python -O` to disable all asserts in production.

---

## Best Practices

**`breakpoint()`** – Prefer over `import pdb; pdb.set_trace()`  
**`!r` in f-strings** – Always use for debugging; shows type and value clearly  
**Logging** – Prefer over print for any code beyond quick scripts  
**`assert`** – Use only for internal invariants, never for user input validation  
**Profile before optimizing** – Always measure first; don't guess bottlenecks  
