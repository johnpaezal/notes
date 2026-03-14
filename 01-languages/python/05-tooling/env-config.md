# Python Environment & Config

## Environment Variables
*Read config from the OS environment*

```python
import os

# Read
db_url = os.environ["DATABASE_URL"]          # raises if missing
db_url = os.environ.get("DATABASE_URL")      # None if missing
db_url = os.getenv("DATABASE_URL", "sqlite:///:memory:")  # with default

# Set (current process only)
os.environ["DEBUG"] = "true"
```

---

## .env Files
*Store secrets outside source code*

```bash
# .env
DATABASE_URL=postgresql://user:pass@localhost/mydb
SECRET_KEY=supersecret
DEBUG=true
PORT=8000
```

```python
from dotenv import load_dotenv
import os

load_dotenv()   # loads .env into os.environ

db_url = os.getenv("DATABASE_URL")
debug  = os.getenv("DEBUG") == "true"
port   = int(os.getenv("PORT", 8000))
```

```bash
pip install python-dotenv
```

---

## Config Classes
*Centralize and type config values*

```python
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///:memory:")
    SECRET_KEY: str   = os.environ["SECRET_KEY"]
    DEBUG: bool       = os.getenv("DEBUG", "false").lower() == "true"
    PORT: int         = int(os.getenv("PORT", 8000))

# Usage
print(Config.DATABASE_URL)
print(Config.DEBUG)
```

---

## pydantic-settings
*Validated settings with type coercion*

```python
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str
    secret_key: str
    debug: bool = False
    port: int = 8000

    class Config:
        env_file = ".env"

# Usage
settings = Settings()
settings.database_url   # auto-loaded from env / .env
settings.port           # int, not string
```

```bash
pip install pydantic-settings
```

---

## configparser (INI files)
*Read structured config files*

```ini
# config.ini
[database]
host = localhost
port = 5432
name = mydb

[server]
debug = true
```

```python
import configparser

config = configparser.ConfigParser()
config.read("config.ini")

host  = config["database"]["host"]       # "localhost"
port  = config.getint("database", "port")  # 5432
debug = config.getboolean("server", "debug")  # True
```

---

## Best Practices

**Never commit `.env`** – Add to `.gitignore` immediately  
**Default values** – Provide sensible defaults for non-sensitive config  
**Type coercion** – Don't use raw strings for booleans/ints from env  
**`pydantic-settings`** – Use for production apps needing validation  
**Secrets** – Use environment variables or secret managers, never hardcode  
