# Python Logging

## Log Levels
*Severity hierarchy for messages*

**DEBUG** – Detailed diagnostic info
**INFO** – Confirm things work as expected
**WARNING** – Something unexpected, still working
**ERROR** – Serious problem, function failed
**CRITICAL** – Program may not continue

```python
import logging

logging.debug("Query executed")
logging.info("Server started")
logging.warning("Disk space low")
logging.error("Failed to connect")
logging.critical("System crash")
```

---

## Basic Configuration
*Set up logging output*

```python
import logging

# Log to console
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s",
)

# Log to file
logging.basicConfig(
    filename="app.log",
    level=logging.WARNING,
    format="%(asctime)s [%(levelname)s] %(message)s",
)

# Usage
logging.info("App started")
```

---

## Named Loggers
*Separate logs per module*

```python
import logging

logger = logging.getLogger(__name__)   # e.g. "myapp.services.user"

def create_user(name):
    logger.info(f"Creating user: {name}")
    try:
        # ...
        logger.debug("User saved to DB")
    except Exception as e:
        logger.error(f"Failed to create user: {e}", exc_info=True)

# Usage
create_user("Alice")
```

---

## Handlers & Formatters
*Route logs to different destinations*

```python
import logging

logger = logging.getLogger("myapp")
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")

# Console handler
console = logging.StreamHandler()
console.setLevel(logging.INFO)
console.setFormatter(formatter)

# File handler
file_handler = logging.FileHandler("app.log")
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

logger.addHandler(console)
logger.addHandler(file_handler)
```

---

## Exception Logging
*Capture full tracebacks*

```python
import logging

logger = logging.getLogger(__name__)

try:
    result = 10 / 0
except ZeroDivisionError:
    logger.exception("Division failed")      # logs message + traceback
    # same as: logger.error("...", exc_info=True)
```

---

## Log Format Variables
*Common format placeholders*

| Placeholder | Description |
|-------------|-------------|
| `%(asctime)s` | Timestamp |
| `%(levelname)s` | Level name (DEBUG, INFO...) |
| `%(name)s` | Logger name |
| `%(message)s` | Log message |
| `%(filename)s` | Source file |
| `%(lineno)d` | Line number |

---

## Best Practices

**Use `__name__`** – Always name loggers with `getLogger(__name__)`  
**Never `print()`** – Use logging in production code, not print  
**`exc_info=True`** – Always log tracebacks on exceptions  
**Level discipline** – DEBUG for dev, WARNING+ for production  
**One `basicConfig`** – Call it once at app entry point only  
