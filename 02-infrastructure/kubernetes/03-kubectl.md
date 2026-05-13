# kubectl
*Command-line tool for Kubernetes*

## Cluster and Context
*Switch between clusters and namespaces*

```bash
kubectl config get-contexts          # list all contexts
kubectl config current-context       # show active context
kubectl config use-context prod      # switch to prod cluster

kubectl cluster-info                 # cluster addresses
kubectl get nodes                    # list cluster nodes
kubectl get nodes -o wide            # with IPs and OS
```

---

## Get Resources
*Inspect objects in the cluster*

```bash
kubectl get pods                         # all pods in default ns
kubectl get pods -n kube-system          # specific namespace
kubectl get pods -A                      # all namespaces
kubectl get pods -l app=api              # filter by label

kubectl get deployment,svc,cm            # multiple types
kubectl get all                          # everything in namespace

kubectl describe pod my-pod              # detailed info + events
kubectl describe node my-node
```

---

## Apply and Delete
*Manage resources declaratively*

```bash
kubectl apply -f deployment.yaml         # create or update
kubectl apply -f manifests/              # apply whole directory

kubectl delete -f deployment.yaml        # delete from file
kubectl delete pod my-pod                # delete by name
kubectl delete pod my-pod --force        # force delete stuck pod

kubectl diff -f deployment.yaml          # preview changes
```

---

## Debugging
*Inspect running containers*

```bash
kubectl logs my-pod                      # container logs
kubectl logs my-pod -c container-name    # specific container
kubectl logs my-pod -f                   # follow (tail)
kubectl logs my-pod --previous           # logs of crashed pod

kubectl exec -it my-pod -- bash          # interactive shell
kubectl exec my-pod -- env               # print env vars

kubectl port-forward svc/api 8080:80     # local→cluster tunnel
kubectl port-forward pod/my-pod 5432:5432

kubectl top pods                         # CPU/memory usage
kubectl top nodes
```

---

## Namespace Operations
*Organize and isolate resources*

```bash
kubectl create namespace staging
kubectl get ns                           # list namespaces

# Set default namespace (avoid -n on every command)
kubectl config set-context --current --namespace=staging

# Usage
kubectl apply -f app.yaml -n staging
kubectl get pods -n staging
```

---

## Useful Flags
*Common output options*

```bash
kubectl get pods -o wide         # extra columns (IP, node)
kubectl get pods -o yaml         # full YAML output
kubectl get pods -o json         # JSON output
kubectl get pods -o jsonpath='{.items[*].metadata.name}'  # extract fields

kubectl explain deployment.spec  # inline API docs
kubectl api-resources            # list all resource types
```
