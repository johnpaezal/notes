# Docker Images & Containers

## Core Concepts
*What Docker is and does*

**Docker** – Tool to build and run isolated containerized apps  
**Image** – Read-only template used to create containers  
**Container** – Running instance of an image  
**Dockerfile** – Script with instructions to build an image  
**Layer** – Each Dockerfile instruction adds a cached filesystem layer  
**Registry** – Storage for images (Docker Hub, ECR, GCR)  
**Docker Hub** – Default public registry at hub.docker.com  

---

## Basic Commands
*Pull, run, inspect, remove*

```bash
# Images
docker pull nginx:latest          # download image from registry
docker images                     # list local images
docker rmi nginx                  # remove image

# Containers
docker run nginx                  # create and start container
docker run -d nginx               # detached (background)
docker run --name web nginx       # named container
docker ps                         # list running containers
docker ps -a                      # all containers (including stopped)
docker stop web                   # stop gracefully
docker rm web                     # remove stopped container
```

---

## Run Options
*Port mapping, volumes, env vars*

```bash
# Port mapping  -p host:container
docker run -p 8080:80 nginx

# Volume mount  -v host_path:container_path
docker run -v $(pwd)/data:/app/data myapp

# Environment variable
docker run -e DB_URL=postgres://localhost/mydb myapp

# Combine options
docker run -d --name api -p 8000:8000 -e ENV=prod myapp:1.0
```

**`-p 8080:80`** – Host port 8080 maps to container port 80  
**`-v`** – Bind mount: host directory linked into container  
**`-e`** – Set env var inside the container  
**`-d`** – Run in background, print container ID  
**`--name`** – Assign a name instead of a random one  

---

## Dockerfile
*Instructions to build an image*

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "main.py"]
```

### Key Instructions
*One instruction per layer*

**FROM** – Base image (always first)  
**WORKDIR** – Set working directory inside the image  
**COPY** – Copy files from host into image  
**RUN** – Execute command at build time (creates a layer)  
**EXPOSE** – Document which port the app listens on  
**CMD** – Default command when container starts (overridable)  
**ENTRYPOINT** – Fixed command; CMD becomes its arguments  

**CMD vs ENTRYPOINT**:

```dockerfile
# CMD alone — fully overridable at runtime
CMD ["python", "main.py"]
# docker run myapp python other.py  ← replaces CMD

# ENTRYPOINT + CMD — entrypoint is fixed, CMD is default arg
ENTRYPOINT ["python"]
CMD ["main.py"]
# docker run myapp other.py  ← runs: python other.py
```

---

## .dockerignore
*Exclude files from build context*

```
__pycache__/
*.pyc
.env
.git
node_modules/
*.log
tests/
```

Prevents secrets and unnecessary files from entering the image.

---

## Build & Push
*Create and publish images*

```bash
# Build image tagged name:version from current directory
docker build -t myapp:1.0 .

# Add an alias tag
docker tag myapp:1.0 myapp:latest

# Push to Docker Hub (login first)
docker login
docker push myuser/myapp:1.0
```

---

## Best Practices

- Use slim base images: `python:3.11-slim`, `node:20-alpine`
- Copy `requirements.txt` before source code to maximize layer cache
- Use `.dockerignore` to keep build context small
- Pin image versions — never rely on `latest` in production
- Use `COPY` over `ADD` unless you need tar extraction
