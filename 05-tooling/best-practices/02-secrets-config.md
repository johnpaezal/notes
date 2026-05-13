# Secrets & Config

## Never Hardcode Secrets
*Use env vars or secrets manager*

**Hardcoded secret** – Credential written directly in source code  
**Secret leak** – Committed credential exposed in git history forever  
**Rule** – Any value that differs between environments must come from outside the code  

```python
# BAD — never do this
db = connect("postgres://admin:SuperSecret123@prod-db:5432/mydb")

# GOOD — read from environment
import os
db = connect(os.getenv("DATABASE_URL"))

# Usage: set DATABASE_URL in .env or environment before running
```

---

## 12-Factor App Config
*Store config in environment*

**12-factor principle III** – Strict separation of config from code  
**Config** – Anything that varies between environments (dev, staging, prod)  
**Rule** – If you can't open-source the code without leaking credentials, config is in code  

**What counts as config**: DB URLs, API keys, ports, feature flags, external service URLs  
**What is NOT config**: Internal logic, static strings, code constants  

---

## Python: python-dotenv & Pydantic Settings
*Load env vars cleanly*

**`python-dotenv`** – Loads `.env` file into `os.environ` at startup  
**`BaseSettings`** – Pydantic class that reads env vars with type validation  

```python
# python-dotenv approach
from dotenv import load_dotenv
import os

load_dotenv()  # reads .env into os.environ
db_url = os.getenv("DATABASE_URL", "sqlite:///default.db")

# Pydantic BaseSettings approach (preferred)
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str
    secret_key: str
    debug: bool = False

    class Config:
        env_file = ".env"

settings = Settings()  # auto-reads env vars + .env

# Usage: pip install pydantic-settings python-dotenv
```

---

## Java/Spring Boot: Config Injection
*Read env vars in Spring*

**`@Value`** – Injects a single property into a field  
**`application.yml`** – Main config file, supports `${ENV_VAR}` placeholders  
**Spring Cloud Config** – Centralized config server for multi-service environments  

```yaml
# application.yml
spring:
  datasource:
    url: ${DATABASE_URL}
    username: ${DB_USER}
    password: ${DB_PASSWORD}
server:
  port: ${PORT:8080}

# Usage: set env vars before running, or use .env with spring-dotenv
```

```java
// @Value injection
@Service
public class PaymentService {
    @Value("${stripe.api.key}")
    private String stripeKey;
}
```

---

## AWS: Secrets Manager vs Parameter Store
*Right tool for each secret type*

**Secrets Manager** – For DB credentials, API keys; supports automatic rotation  
**Parameter Store** – For non-secret config (feature flags, URLs, ports); cheaper  
**Rule** – Secrets Manager for anything sensitive; Parameter Store for plain config  

**Automatic rotation** – Secrets Manager can rotate DB passwords on a schedule using a Lambda  

```python
import boto3, json

def get_secret(secret_name: str) -> dict:
    client = boto3.client("secretsmanager")
    response = client.get_secret_value(SecretId=secret_name)
    return json.loads(response["SecretString"])

# Usage: call at app startup, not per-request (cache the value)
creds = get_secret("prod/myapp/db")
```

---

## Config Hierarchy
*Higher source wins*

**Priority order (lowest to highest)**:

1. **Defaults** – Hardcoded fallbacks in code  
2. **`.env` file** – Local developer overrides  
3. **Environment variables** – Set by CI/CD or runtime platform  
4. **AWS Secrets Manager** – Authoritative production secrets  

Higher-priority sources always override lower ones. Application reads in order and the last write wins.
