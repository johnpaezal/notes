# Docker Registries & Networking

## ECR Push Workflow
*Authenticate, tag, push*

> For full ECR/ECS detail see `06-cloud/aws/07-devops/ecs-ecr.md`.

```bash
# Authenticate Docker to ECR
aws ecr get-login-password --region us-east-1 \
  | docker login --username AWS --password-stdin <account_id>.dkr.ecr.us-east-1.amazonaws.com

# Tag local image for ECR
docker tag myapp:1.0 <account_id>.dkr.ecr.us-east-1.amazonaws.com/myapp:1.0

# Push
docker push <account_id>.dkr.ecr.us-east-1.amazonaws.com/myapp:1.0
```

---

## Networking Modes
*How containers connect to the world*

**bridge** – Default; containers on same network communicate by container name  
**host** – Container shares the host's network stack (Linux only)  
**none** – No network interface; fully isolated  
**overlay** – Multi-host networking for Docker Swarm clusters  

### Network Commands

```bash
docker network ls                      # list all networks
docker network inspect bridge          # details, IPs, containers
docker network create mynet            # create custom bridge network
docker run --network mynet myapp       # attach container to network
```

### Compose Service Names as Hostnames
*Service name resolves automatically*

Within a Compose network, each service is reachable by its service name:

```yaml
services:
  api:
    environment:
      - DB_HOST=db      # "db" resolves to the db container
  db:
    image: postgres:15
```

---

## Volumes vs Bind Mounts
*Persistent data strategies*

| | Named Volume | Bind Mount |
|---|---|---|
| Managed by | Docker | Host OS |
| Path | Docker internal | Explicit host path |
| Portability | High | Host-dependent |
| Best for | Databases, state | Dev: live code reload |
| Syntax | `-v pgdata:/data` | `-v $(pwd):/app` |

### Volume Commands

```bash
docker volume ls                    # list volumes
docker volume inspect pgdata        # details and mount point
docker volume prune                 # remove all unused volumes
```

---

## Debugging
*Inspect running containers*

```bash
docker logs -f <name>              # stream container logs
docker exec -it <name> bash        # open interactive shell
docker inspect <name>              # full JSON metadata
docker stats                       # live CPU/memory usage
docker system prune                # remove stopped containers, unused images, networks
```
