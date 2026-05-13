# Docker Multi-Stage Builds

## Why Multi-Stage
*Smaller, leaner final images*

A multi-stage build uses multiple `FROM` instructions in one Dockerfile. Early stages do heavy work (install compilers, build artifacts). The final stage copies only what the app needs to run — no build tools, no dev dependencies.

**Result**: smaller images, fewer vulnerabilities, cleaner layers.

---

## Python Example
*Build deps, copy only result*

```dockerfile
# Stage 1: install dependencies
FROM python:3.11-slim AS builder

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# Stage 2: production image
FROM python:3.11-slim AS production

WORKDIR /app
COPY --from=builder /install /usr/local
COPY . .

EXPOSE 8000
CMD ["python", "main.py"]
```

**`AS builder`** – Name the stage for reference  
**`COPY --from=builder`** – Copy files from a previous stage  

---

## Java / Maven Example
*Compile then minimal runtime*

```dockerfile
FROM maven:3.9-eclipse-temurin-17 AS build

WORKDIR /app
COPY pom.xml .
RUN mvn dependency:go-offline
COPY src ./src
RUN mvn package -DskipTests

FROM eclipse-temurin:17-jre-alpine AS production

WORKDIR /app
COPY --from=build /app/target/app.jar app.jar

EXPOSE 8080
CMD ["java", "-jar", "app.jar"]
```

Maven and JDK stay in the `build` stage — the final image has only the JRE and the JAR.

---

## Security & Hardening
*Run as non-root user*

```dockerfile
FROM python:3.11-slim AS production

WORKDIR /app
COPY --from=builder /install /usr/local
COPY . .

# Create non-root user
RUN useradd -r -u 1001 appuser
USER appuser

EXPOSE 8000
HEALTHCHECK --interval=30s --timeout=5s CMD curl -f http://localhost:8000/health || exit 1
CMD ["python", "main.py"]
```

---

## Best Practices

- Pin base image versions: `python:3.11-slim`, not `python:latest`
- Name every stage with `AS <name>` for clarity
- Use `.dockerignore` to keep build context minimal
- One process per container
- Add `HEALTHCHECK` so orchestrators know when a container is ready
- Run as non-root: `RUN useradd -r appuser` + `USER appuser`
