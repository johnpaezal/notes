# Kubernetes Fundamentals
*Container orchestration core concepts*

## What is Kubernetes
*Automated container management at scale*

**Kubernetes (K8s)** – Open-source system to deploy, scale, and manage containers  
**Cluster** – Set of machines (nodes) running K8s  
**Node** – Single machine in the cluster (VM or physical)  
**Control Plane** – Master components that manage the cluster  
**Data Plane** – Worker nodes that run application workloads

**Why K8s**: Auto-healing, horizontal scaling, rolling updates, service discovery, load balancing

---

## Core Objects
*Building blocks of K8s*

**Pod** – Smallest unit; one or more containers sharing network/storage  
**ReplicaSet** – Maintains N running copies of a Pod  
**Deployment** – Manages ReplicaSets; enables rollouts and rollbacks  
**Service** – Stable network endpoint to reach a set of Pods  
**ConfigMap** – Non-secret config data (env vars, config files)  
**Secret** – Sensitive config data (passwords, tokens) — base64 encoded  
**Namespace** – Virtual cluster for isolation (`default`, `kube-system`)  
**Ingress** – HTTP routing rules into the cluster  

---

## Cluster Architecture
*Control plane vs worker nodes*

```
Control Plane:
  API Server    ← all requests go through here
  etcd          ← distributed key-value store (cluster state)
  Scheduler     ← assigns Pods to Nodes
  Controller Manager ← runs controllers (ReplicaSet, Deployment...)

Worker Node:
  kubelet       ← agent; ensures containers run as specified
  kube-proxy    ← maintains network rules on node
  Container Runtime ← containerd or Docker; runs containers
```

---

## Pod Lifecycle
*States a Pod goes through*

**Pending** – Accepted, not yet scheduled to a node  
**Running** – At least one container running  
**Succeeded** – All containers exited with code 0  
**Failed** – At least one container exited non-zero  
**CrashLoopBackOff** – Container keeps crashing, K8s retrying  

---

## Labels and Selectors
*How objects find each other*

```yaml
# Pod with label
metadata:
  labels:
    app: api
    env: production

# Service selecting those pods
selector:
  app: api
  env: production
```

**Label** – Key/value pair attached to any object  
**Selector** – Filter that matches objects by label  
**Annotation** – Non-identifying metadata (not used for selection)
