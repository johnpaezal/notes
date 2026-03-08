# Python Stdlib Utils

## Context Managers
*Custom `with` statement support*

### Class-based
*Implement `__enter__` and `__exit__`*

```python
class DatabaseConnection:
    def __enter__(self):
        self.conn = connect_db()
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()
        return False        # don't suppress exceptions

# Usage
with DatabaseConnection() as conn:
    conn.query("SELECT * FROM users")
```

### Function-based
*Use `@contextmanager` for simpler syntax*

```python
from contextlib import contextmanager

@contextmanager
def timer():
    import time
    start = time.time()
    yield
    print(f"Elapsed: {time.time() - start:.2f}s")

# Usage
with timer():
    do_work()
```

---

## Iterators
*Custom iterable objects*

```python
class CountDown:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.n <= 0:
            raise StopIteration
        self.n -= 1
        return self.n + 1

# Usage
for i in CountDown(5):
    print(i)            # 5, 4, 3, 2, 1

it = iter([1, 2, 3])
next(it)                # 1
next(it, "done")        # default if exhausted
```

---

## functools
*Higher-order function utilities*

```python
from functools import lru_cache, partial, reduce

# lru_cache – memoize expensive calls
@lru_cache(maxsize=128)
def fibonacci(n):
    if n < 2: return n
    return fibonacci(n-1) + fibonacci(n-2)

# partial – fix some arguments
def power(base, exp): return base ** exp

square = partial(power, exp=2)
cube   = partial(power, exp=3)

# reduce – accumulate values
total = reduce(lambda acc, x: acc + x, [1, 2, 3, 4])  # 10

# Usage
fibonacci(100)  # fast, cached
square(5)       # 25
cube(3)         # 27
```

---

## itertools
*Efficient iteration tools*

```python
import itertools

itertools.chain([1,2], [3,4])              # [1,2,3,4]
itertools.combinations([1,2,3], 2)         # [(1,2),(1,3),(2,3)]
itertools.permutations([1,2,3], 2)         # all ordered pairs
itertools.product("AB", [1,2])             # cartesian product
itertools.repeat(0, 3)                     # [0, 0, 0]
itertools.islice(range(100), 5)            # [0,1,2,3,4]

# groupby — group consecutive equal elements
data = [("a", 1), ("a", 2), ("b", 3)]
for key, group in itertools.groupby(data, key=lambda x: x[0]):
    print(key, list(group))
```

---

## Async / Await
*Concurrent I/O without threads*

```python
import asyncio

async def fetch(url):
    await asyncio.sleep(1)      # simulate I/O
    return f"data from {url}"

async def main():
    # Sequential
    result = await fetch("https://example.com")

    # Concurrent
    results = await asyncio.gather(
        fetch("https://a.com"),
        fetch("https://b.com"),
    )

asyncio.run(main())
```

```python
# Async context manager / iterator
async with aiofiles.open("file.txt") as f:
    content = await f.read()

async for item in async_generator():
    process(item)
```

> See `04-advanced/concurrency/notes.md` for threading and multiprocessing.

---

## Best Practices

**`@contextmanager`** – Prefer over class-based for simple context managers  
**`lru_cache`** – Use for pure functions called repeatedly with same args  
**`partial`** – Use to create specialized versions of general functions  
**`itertools`** – Always check before writing a custom loop; it's likely there  
**`async/await`** – Use for I/O-bound concurrency; not for CPU-bound tasks  
