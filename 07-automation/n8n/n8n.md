# n8n
*Low-code workflow automation platform*

## What is n8n
*Visual workflow builder with code when needed*

**n8n** – Open-source workflow automation tool; connect apps, APIs, and databases  
**Workflow** – Directed graph of nodes executed in sequence  
**Node** – Single action: trigger, transform, or integration  
**Trigger Node** – Starts the workflow (webhook, schedule, event)  
**Action Node** – Does something (HTTP request, DB query, email send)  
**Expression** – Dynamic values using `{{ $json.field }}` or JS  

---

## Run Locally
*Self-hosted via Docker*

```bash
# Docker (simplest)
docker run -it --rm \
  -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n \
  n8nio/n8n

# Docker Compose (persistent)
# docker-compose.yml:
# services:
#   n8n:
#     image: n8nio/n8n
#     ports: ["5678:5678"]
#     volumes: ["./.n8n:/home/node/.n8n"]
#     environment:
#       - N8N_BASIC_AUTH_ACTIVE=true
#       - N8N_BASIC_AUTH_USER=admin
#       - N8N_BASIC_AUTH_PASSWORD=secret

# Access at http://localhost:5678
```

---

## Common Nodes
*Frequently used integrations*

**Webhook** – Receive HTTP requests (trigger external events)  
**Schedule Trigger** – Cron-based execution (`0 9 * * 1` = every Monday 9am)  
**HTTP Request** – Call any REST API  
**Code** – Write JavaScript or Python for custom logic  
**Set** – Create/transform fields  
**IF** – Conditional branching  
**Loop Over Items** – Iterate over array  
**Postgres / MySQL** – Direct database queries  
**Gmail / Slack / Discord** – Pre-built integrations  

---

## Expressions
*Reference data from previous nodes*

```javascript
// Access current item's JSON
{{ $json.email }}
{{ $json.user.name }}

// Access specific node's output
{{ $node["HTTP Request"].json.id }}

// JavaScript in expressions
{{ $json.price * 1.19 }}
{{ $json.name.toLowerCase() }}
{{ new Date().toISOString() }}

// All items from previous node
{{ $items("HTTP Request") }}
```

---

## Typical Use Cases
*What n8n is good at*

**API Integrations** – Connect two services that have no native integration  
**Data Sync** – Periodically sync records between databases or CRMs  
**Notifications** – Send Slack/email alerts when conditions are met  
**ETL Pipelines** – Extract data from API → transform → load into DB  
**Webhook Processing** – Receive Stripe/GitHub/Shopify webhooks, process and forward  

```
Example: New GitHub PR → post to Slack channel
GitHub Webhook → IF (action = opened) → Slack Message
```

---

## Error Handling
*Handle failures in workflows*

```
- Enable "Continue on Fail" on a node → workflow continues even if node fails
- Use "Error Workflow" setting → trigger another workflow on failure
- Try/Catch pattern: Code node with try { } catch { } block
- Retry on Fail: available on most nodes (max retries, wait time)
```
