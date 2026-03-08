# Python Concurrency

## Overview
*When to use each approach*

**threading** – I/O-bound tasks (network, disk); limited by GIL
**multiprocessing** – CPU-bound tasks; bypasses GIL with separate processes
**asyncio** – I/O-bound with many concurrent tasks; single thread

---

## Threading
*Run I/O tasks concurrently*

```python
import threading
import time

def download(url):
    print(f"Downloading {url}")
    time.sleep(2)               # simulate I/O
    print(f"Done: {url}")

# Usage
urls = ["a.com", "b.com", "c.com"]
threads = [threading.Thread(target=download, args=(url,)) for url in urls]

for t in threads:
    t.start()

for t in threads:
    t.join()    # wait for all to finish
```

### Thread-Safe Shared State
*Prevent race conditions with locks*

```python
import threading

counter = 0
lock = threading.Lock()

def increment():
    global counter
    with lock:
        counter += 1

threads = [threading.Thread(target=increment) for _ in range(100)]
for t in threads: t.start()
for t in threads: t.join()

print(counter)  # 100
```

---

## Multiprocessing
*Parallelize CPU-bound work*

```python
from multiprocessing import Pool
import os

def compute(n):
    return n ** 2

# Usage
with Pool(processes=os.cpu_count()) as pool:
    results = pool.map(compute, range(10))

print(results)  # [0, 1, 4, 9, ..., 81]
```

### Process vs Thread
*Choose the right tool*

| | Threading | Multiprocessing |
|--|-----------|-----------------|
| GIL | Limited by it | Bypasses it |
| Memory | Shared | Separate |
| Overhead | Low | Higher |
| Best for | I/O-bound | CPU-bound |

---

## concurrent.futures
*High-level thread/process pool API*

```python
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

def fetch(url):
    return f"data from {url}"

urls = ["a.com", "b.com", "c.com"]

# Threads (I/O-bound)
with ThreadPoolExecutor(max_workers=5) as executor:
    results = list(executor.map(fetch, urls))

# Processes (CPU-bound)
with ProcessPoolExecutor() as executor:
    results = list(executor.map(compute, range(10)))
```

---

## asyncio
*Concurrent I/O on a single thread*

> See `advanced/notes.md` for full async/await patterns.

```python
import asyncio

async def fetch(url):
    await asyncio.sleep(1)      # non-blocking I/O
    return f"data from {url}"

async def main():
    results = await asyncio.gather(
        fetch("a.com"),
        fetch("b.com"),
        fetch("c.com"),
    )
    print(results)

asyncio.run(main())
```

---

## Best Practices

**GIL** – Use `multiprocessing` for CPU-bound, `threading` for I/O-bound  
**`concurrent.futures`** – Prefer over raw `threading` for simpler code  
**Locks** – Always use `with lock:` to prevent deadlocks  
**`asyncio`** – Best for many concurrent I/O tasks (e.g. web servers)  
**Avoid shared state** – Pass data via queues or return values instead  
