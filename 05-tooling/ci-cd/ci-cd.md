# CI/CD
*Continuous Integration and Continuous Delivery*

## Core Concepts
*Automate build, test, and deploy*

**CI (Continuous Integration)** – Automatically build and test on every push  
**CD (Continuous Delivery)** – Automatically deploy to staging; manual prod gate  
**CD (Continuous Deployment)** – Automatically deploy to production on every green build  
**Pipeline** – Sequence of automated stages (build → test → deploy)  
**Artifact** – Output of a build (Docker image, JAR, ZIP)  

---

## GitHub Actions
*CI/CD built into GitHub*

```yaml
# .github/workflows/ci.yml
name: CI

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: "3.11"

      - name: Install dependencies
        run: pip install -r requirements.txt

      - name: Run tests
        run: pytest --tb=short

      - name: Lint
        run: ruff check .
```

---

## Build and Push Docker Image
*Docker image pipeline*

```yaml
  build:
    needs: test
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - name: Log in to Docker Hub
        uses: docker/login-action@v3
        with:
          username: ${{ secrets.DOCKER_USER }}
          password: ${{ secrets.DOCKER_TOKEN }}

      - name: Build and push
        uses: docker/build-push-action@v5
        with:
          push: true
          tags: myuser/myapp:${{ github.sha }}
```

---

## Deploy to AWS ECS
*Deploy after successful build*

```yaml
  deploy:
    needs: build
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'

    steps:
      - name: Configure AWS credentials
        uses: aws-actions/configure-aws-credentials@v4
        with:
          aws-access-key-id: ${{ secrets.AWS_KEY }}
          aws-secret-access-key: ${{ secrets.AWS_SECRET }}
          aws-region: us-east-1

      - name: Update ECS service
        run: |
          aws ecs update-service \
            --cluster prod \
            --service api \
            --force-new-deployment
```

---

## Pipeline Stages
*Standard CI/CD flow*

```
Push → Lint → Unit Tests → Build Image → Integration Tests → Deploy Staging → Deploy Prod
         └── fail fast: stop pipeline on first error
```

**Best Practices**:
- Fail fast — cheapest checks first (lint → unit → integration → deploy)
- Never store secrets in code; use secrets manager or CI env vars
- Pin action versions (`@v4`) to avoid supply chain attacks
- Run tests in parallel to reduce pipeline duration

---

## Environment Variables and Secrets
*Pass config securely*

```yaml
# In GitHub: Settings → Secrets and variables → Actions
# Use in workflow:
env:
  APP_ENV: production
  DATABASE_URL: ${{ secrets.DATABASE_URL }}

# Or per step:
- name: Run migrations
  run: python manage.py migrate
  env:
    DATABASE_URL: ${{ secrets.DATABASE_URL }}
```
