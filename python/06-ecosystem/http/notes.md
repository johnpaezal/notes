# Python HTTP

## requests
*Make HTTP calls simply*

```bash
pip install requests
```

```python
import requests

# GET
response = requests.get("https://api.example.com/users")
response.status_code     # 200
response.json()          # parsed JSON body
response.text            # raw string body
response.headers         # dict of headers

# POST
response = requests.post(
    "https://api.example.com/users",
    json={"name": "Alice", "age": 25},
)

# With headers and params
response = requests.get(
    "https://api.example.com/users",
    params={"page": 1, "limit": 10},
    headers={"Authorization": "Bearer my-token"},
)
```

---

## Error Handling
*Detect and handle failures*

```python
import requests
from requests.exceptions import HTTPError, Timeout, ConnectionError

try:
    response = requests.get("https://api.example.com/data", timeout=5)
    response.raise_for_status()     # raises on 4xx / 5xx
    data = response.json()
except HTTPError as e:
    print(f"HTTP error {e.response.status_code}: {e}")
except Timeout:
    print("Request timed out")
except ConnectionError:
    print("No connection")
```

---

## Sessions
*Reuse connections and shared config*

```python
import requests

with requests.Session() as session:
    session.headers["Authorization"] = "Bearer my-token"
    session.headers["Accept"] = "application/json"

    # All requests share the session config
    users    = session.get("https://api.example.com/users").json()
    products = session.get("https://api.example.com/products").json()
```

---

## httpx (Async)
*HTTP client with async support*

```bash
pip install httpx
```

```python
import httpx

# Sync (same API as requests)
with httpx.Client() as client:
    response = client.get("https://api.example.com/users")
    data = response.json()

# Async
import asyncio

async def fetch_all():
    async with httpx.AsyncClient() as client:
        results = await asyncio.gather(
            client.get("https://api.example.com/users"),
            client.get("https://api.example.com/products"),
        )
    return [r.json() for r in results]

asyncio.run(fetch_all())
```

---

## Common Patterns
*Frequently used HTTP patterns*

```python
import requests

BASE_URL = "https://api.example.com"

# CRUD
requests.get(f"{BASE_URL}/users")              # list
requests.get(f"{BASE_URL}/users/1")            # get one
requests.post(f"{BASE_URL}/users", json=data)  # create
requests.put(f"{BASE_URL}/users/1", json=data) # replace
requests.patch(f"{BASE_URL}/users/1", json=data) # partial update
requests.delete(f"{BASE_URL}/users/1")         # delete

# Upload file
with open("image.png", "rb") as f:
    requests.post(f"{BASE_URL}/upload", files={"file": f})
```

---

## Best Practices

**Always set `timeout`** – Never leave requests without a timeout  
**`raise_for_status()`** – Call after every request to catch HTTP errors  
**Sessions** – Use for multiple requests to the same host  
**`httpx`** – Prefer over `requests` when using async code  
**`BASE_URL` constant** – Never repeat the host string across calls  
