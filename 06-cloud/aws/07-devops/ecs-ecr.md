# AWS ECS & ECR
*Container deployment on AWS*

## ECR
*Elastic Container Registry — private Docker registry*

**ECR (Elastic Container Registry)** – AWS-managed Docker image registry  
**Repository** – Stores images for one app (`myapp`, `api`, `worker`)  
**Image** – Docker image identified by tag or digest  

```bash
# Authenticate Docker to ECR
aws ecr get-login-password --region us-east-1 \
  | docker login --username AWS --password-stdin \
    123456789.dkr.ecr.us-east-1.amazonaws.com

# Create repo
aws ecr create-repository --repository-name my-api

# Tag and push image
docker build -t my-api .
docker tag my-api:latest 123456789.dkr.ecr.us-east-1.amazonaws.com/my-api:latest
docker push 123456789.dkr.ecr.us-east-1.amazonaws.com/my-api:latest
```

---

## ECS Concepts
*Elastic Container Service — run containers at scale*

**ECS (Elastic Container Service)** – Managed container orchestration (no K8s needed)  
**Cluster** – Logical group of infrastructure running containers  
**Task Definition** – Blueprint: image, CPU, memory, env vars, ports  
**Task** – Running instance of a task definition (like a Pod in K8s)  
**Service** – Ensures N tasks always running; handles rolling deploys  

---

## Launch Types
*Where the containers run*

**EC2 Launch Type** – Containers run on EC2 instances you manage  
**Fargate Launch Type** – Serverless; AWS manages the underlying infrastructure  

**Use Fargate**: no EC2 capacity management, pay per task (CPU/memory), easier to start  
**Use EC2**: more control, specific instance types (GPU, large memory), cost optimization

---

## Task Definition
*Container config in JSON/YAML*

```json
{
  "family": "api-task",
  "networkMode": "awsvpc",
  "requiresCompatibilities": ["FARGATE"],
  "cpu": "256",
  "memory": "512",
  "containerDefinitions": [{
    "name": "api",
    "image": "123456789.dkr.ecr.us-east-1.amazonaws.com/my-api:latest",
    "portMappings": [{"containerPort": 8080}],
    "environment": [
      {"name": "APP_ENV", "value": "production"}
    ],
    "secrets": [
      {"name": "DB_URL", "valueFrom": "arn:aws:secretsmanager:..."}
    ],
    "logConfiguration": {
      "logDriver": "awslogs",
      "options": {
        "awslogs-group": "/ecs/api",
        "awslogs-region": "us-east-1",
        "awslogs-stream-prefix": "ecs"
      }
    }
  }]
}
```

---

## Deploy and Scale
*Update running service*

```bash
# Update service (force new deploy with latest image)
aws ecs update-service \
  --cluster prod \
  --service api-service \
  --force-new-deployment

# Scale service
aws ecs update-service \
  --cluster prod \
  --service api-service \
  --desired-count 4

# View running tasks
aws ecs list-tasks --cluster prod --service-name api-service
```

**Rolling Update** – ECS replaces tasks gradually based on `minimumHealthyPercent` / `maximumPercent`.
