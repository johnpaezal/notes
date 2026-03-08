# Python Language Features

## Type Hints
*Static type annotations (Python 3.5+)*

```python
# Variables
name: str = "Alice"
age:  int = 25

# Functions
def greet(name: str) -> str:
    return f"Hello, {name}"

def divide(a: float, b: float) -> float | None:
    return a / b if b != 0 else None

# Collections (Python 3.9+)
def find(items: list[str], key: str) -> str | None: ...
def process(data: dict[str, int]) -> list[int]: ...

# Legacy (< 3.9)
from typing import Optional, List, Dict
def get_user(id: int) -> Optional[dict]: ...
```

---

## Walrus Operator `:=`
*Assign and use in one expression (Python 3.8+)*

```python
# In while loop
while chunk := f.read(8192):
    process(chunk)

# In if condition
if match := pattern.search(text):
    print(match.group())

# In comprehension (avoid redundant computation)
results = [y for x in data if (y := transform(x)) is not None]
```

---

## Packing / Unpacking
*Flexible assignment patterns*

```python
a, b, c = [1, 2, 3]

# Star unpacking
first, *rest = [1, 2, 3, 4]    # first=1, rest=[2,3,4]
*init, last  = [1, 2, 3, 4]    # init=[1,2,3], last=4
a, *mid, z   = [1, 2, 3, 4, 5] # a=1, mid=[2,3,4], z=5

# Swap
a, b = b, a

# Ignore values
_, important, *_ = [1, 2, 3, 4, 5]
```

---

## String Formatting
*Power f-string features*

```python
name  = "Alice"
value = 3.14159
num   = 1000000

f"{name!r}"       # "'Alice'"    repr
f"{value:.2f}"    # "3.14"       float precision
f"{num:,}"        # "1,000,000"  thousands separator
f"{num:0>8}"      # "01000000"   zero-padded, right-aligned

# join (efficient concatenation)
", ".join(["a", "b", "c"])          # "a, b, c"

# partition
"user@email.com".partition("@")     # ("user", "@", "email.com")
```

---

## Best Practices

**Type hints** – Use in all function signatures; helps IDEs and catches bugs early  
**Walrus `:=`** – Use to avoid double computation, not just to shorten code  
**Star unpacking** – Use `_` and `*_` to discard values you don't need  
**f-strings** – Always prefer over `.format()` or `%` formatting  
