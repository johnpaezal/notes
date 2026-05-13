# Docker Compose

## Core Concepts
*Multi-container apps in one file*

**docker-compose** – Tool to define and run multi-container apps via YAML  
**service** – One container definition (image, ports, env, volumes)  
**network** – Virtual network connecting services  
**named volume** – Docker-managed persistent storage shared across services  

---

## Full Example
*Web app + database + cache*

```yaml
# docker-compose.yml
services:
  web:
    build: .
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgresql://user:pass@db:5432/mydb
      - REDIS_URL=redis://cache:6379
    depends_on:
      - db
      - cache
    networks:
      - backend

  db:
    image: postgres:15
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: pass
      POSTGRES_DB: mydb
    volumes:
      - pgdata:/var/lib/postgresql/data
    networks:
      - backend

  cache:
    image: redis:7-alpine
    networks:
      - backend

volumes:
  pgdata:

networks:
  backend:
```

**`build: .`** – Build image from Dockerfile in current directory  
**`depends_on`** – Start order only; does not wait for readiness  
**`volumes: pgdata:`** – Declares a named volume at the top level  

---

## Common Commands
*Manage compose services*

```bash
docker compose up -d          # start all services in background
docker compose down           # stop and remove containers
docker compose down -v        # also remove named volumes
docker compose logs -f web    # stream logs from a service
docker compose exec web bash  # open shell in running service
docker compose ps             # status of all services
docker compose build          # rebuild images
```

---

## Networking
*Container-to-container communication*

By default, Compose creates a **bridge network** for all services. Each service is reachable by its **service name** as hostname.

```yaml
# web can connect to db at hostname "db", port 5432
DATABASE_URL=postgresql://user:pass@db:5432/mydb
```

### Custom Network
*Isolate groups of services*

```yaml
networks:
  backend:        # internal services
  frontend:       # public-facing services

services:
  web:
    networks: [frontend, backend]
  db:
    networks: [backend]   # not reachable from frontend
```

**bridge** – Default; containers communicate by service name  
**host** – Container shares host network (Linux only, no port mapping)  
**none** – No networking  
**overlay** – Multi-host networking (Docker Swarm)  

---

## Best Practices

- Use `.env` file for secrets; reference with `${VAR}` in compose
- Always declare named volumes for databases
- Use `depends_on` with health checks for readiness in production
- Separate compose files for dev and prod (`docker-compose.override.yml`)
