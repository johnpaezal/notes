# JSON & YAML
*Data serialization formats*

## JSON
*JavaScript Object Notation*

**JSON** – Lightweight text format for data exchange  
**Types**: string, number, boolean, null, array, object  

```json
{
  "name": "Alice",
  "age": 30,
  "active": true,
  "score": null,
  "tags": ["admin", "user"],
  "address": {
    "city": "Bogotá",
    "zip": "111011"
  }
}
```

**Rules**: strings use double quotes, no trailing commas, no comments

---

## JSON in Python
*Parse and generate JSON*

```python
import json

# Parse JSON string → dict
data = json.loads('{"name": "Alice", "age": 30}')
print(data["name"])      # → Alice

# Convert dict → JSON string
user = {"name": "Bob", "age": 25}
print(json.dumps(user))                     # compact
print(json.dumps(user, indent=2))           # pretty

# Read/write file
with open("data.json") as f:
    data = json.load(f)

with open("output.json", "w") as f:
    json.dump(data, f, indent=2)
```

---

## YAML
*YAML Ain't Markup Language*

**YAML** – Human-readable config format; superset of JSON  
**Indent** – 2 spaces (tabs not allowed)  
**`---`** – Start of document separator  

```yaml
# Scalars
name: Alice
age: 30
active: true
score: null

# List
tags:
  - admin
  - user

# Nested object
address:
  city: Bogotá
  zip: "111011"   # quote to force string

# Multiline string
description: |
  First line
  Second line

# Inline (JSON-style)
colors: [red, green, blue]
point: {x: 1, y: 2}
```

---

## YAML in Python
*Parse config files*

```bash
pip install pyyaml
```

```python
import yaml

# Parse YAML string
text = """
name: Alice
tags:
  - admin
  - user
"""
data = yaml.safe_load(text)    # always use safe_load
print(data["tags"])            # → ['admin', 'user']

# Read YAML file
with open("config.yaml") as f:
    config = yaml.safe_load(f)

# Write YAML
with open("output.yaml", "w") as f:
    yaml.dump(data, f, default_flow_style=False)
```

---

## Comparison
*When to use each*

| | JSON | YAML |
|---|---|---|
| Comments | No | Yes (`# comment`) |
| Readability | Medium | High |
| Strictness | Strict | Lenient (can cause bugs) |
| Use case | APIs, data exchange | Config files, K8s, CI |
| Supported by | All languages | Most languages |

---

## YAML Gotchas
*Common mistakes*

```yaml
# Accidental boolean coercion (YAML 1.1)
country: NO          # parsed as false!  → quote it: "NO"
debug: on            # parsed as true!   → use true/false
version: 1.0         # parsed as float   → quote: "1.0"

# Fix
country: "NO"
debug: true
version: "1.0"
```
