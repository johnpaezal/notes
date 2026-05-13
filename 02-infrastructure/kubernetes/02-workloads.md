# Kubernetes Workloads
*Deploying and managing applications*

## Deployment
*Declarative app rollout and management*

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: api
spec:
  replicas: 3
  selector:
    matchLabels:
      app: api
  template:
    metadata:
      labels:
        app: api
    spec:
      containers:
        - name: api
          image: myapp:1.0
          ports:
            - containerPort: 8080
          env:
            - name: PORT
              value: "8080"
          resources:
            requests:
              cpu: "100m"
              memory: "128Mi"
            limits:
              cpu: "500m"
              memory: "512Mi"
```

---

## Service Types
*Exposing Pods on the network*

**ClusterIP** – Internal-only; default; reachable within cluster  
**NodePort** – Exposes on `<NodeIP>:<port>` externally  
**LoadBalancer** – Provisions cloud load balancer (AWS ELB, GCP LB)  
**ExternalName** – DNS alias to external service  

```yaml
apiVersion: v1
kind: Service
metadata:
  name: api-svc
spec:
  selector:
    app: api
  ports:
    - port: 80
      targetPort: 8080
  type: ClusterIP
```

---

## ConfigMap and Secret
*Inject config into containers*

```yaml
# ConfigMap
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
data:
  LOG_LEVEL: "info"
  APP_ENV: "production"

---
# Secret (values must be base64 encoded)
apiVersion: v1
kind: Secret
metadata:
  name: db-secret
type: Opaque
data:
  DB_PASSWORD: cGFzc3dvcmQ=   # echo -n "password" | base64

---
# Use in Pod
envFrom:
  - configMapRef:
      name: app-config
  - secretRef:
      name: db-secret
```

---

## Scaling and Updates
*Horizontal scaling and rollouts*

```bash
# Scale
kubectl scale deployment api --replicas=5

# Rolling update (change image)
kubectl set image deployment/api api=myapp:2.0

# Check rollout status
kubectl rollout status deployment/api

# Rollback
kubectl rollout undo deployment/api
kubectl rollout undo deployment/api --to-revision=2
```

**Rolling Update** – Replaces old Pods gradually, zero downtime  
**`maxSurge`** – Extra Pods allowed during update (default 25%)  
**`maxUnavailable`** – Pods that can be down during update (default 25%)  

---

## Resource Requests and Limits
*CPU and memory constraints*

**Request** – Minimum guaranteed; used by Scheduler to pick a node  
**Limit** – Maximum allowed; container killed if memory exceeds  

| Unit | CPU | Memory |
|------|-----|--------|
| Small | `100m` (0.1 core) | `128Mi` |
| Medium | `500m` (0.5 core) | `512Mi` |
| Large | `1` (1 core) | `1Gi` |

Always set both requests and limits in production.
