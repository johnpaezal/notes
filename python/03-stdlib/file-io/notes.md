# Python File I/O

## Reading Files
*Load file contents*

```python
# Entire file
with open("file.txt") as f:
    content = f.read()

# Line by line (memory efficient)
with open("file.txt") as f:
    for line in f:
        print(line.strip())

# All lines as list
with open("file.txt") as f:
    lines = f.readlines()    # ["line1\n", "line2\n"]

# Single line
with open("file.txt") as f:
    first = f.readline()
```

---

## Writing Files
*Save data to files*

```python
# Write (overwrites existing)
with open("file.txt", "w") as f:
    f.write("Hello\n")
    f.write("World\n")

# Append (keeps existing content)
with open("file.txt", "a") as f:
    f.write("New line\n")

# Multiple lines
lines = ["line1\n", "line2\n", "line3\n"]
with open("file.txt", "w") as f:
    f.writelines(lines)
```

---

## File Modes
*How to open a file*

| Mode | Description |
|------|-------------|
| `"r"` | Read (default) |
| `"w"` | Write (overwrite) |
| `"a"` | Append |
| `"x"` | Create (fails if exists) |
| `"rb"` | Read binary |
| `"wb"` | Write binary |
| `"r+"` | Read + write |

---

## Encoding
*Handle text with special characters*

```python
with open("file.txt", encoding="utf-8") as f:
    content = f.read()

with open("file.txt", "w", encoding="utf-8") as f:
    f.write("texto con acentos: é, ñ, ü")
```

---

## JSON Files
*Read and write structured data*

```python
import json

data = {"name": "Alice", "age": 25, "scores": [90, 85]}

# Write
with open("data.json", "w") as f:
    json.dump(data, f, indent=2)

# Read
with open("data.json") as f:
    data = json.load(f)

# Usage
print(data["name"])    # "Alice"
```

---

## CSV Files
*Read and write tabular data*

```python
import csv

# Write
rows = [["name", "age"], ["Alice", 25], ["Bob", 30]]
with open("data.csv", "w", newline="") as f:
    csv.writer(f).writerows(rows)

# Read (row as list)
with open("data.csv") as f:
    for row in csv.reader(f):
        print(row)

# Read (row as dict)
with open("data.csv") as f:
    for row in csv.DictReader(f):
        print(row["name"], row["age"])
```

---

## Path Operations
*Navigate the filesystem*

```python
from pathlib import Path

p = Path("folder") / "subfolder" / "file.txt"

# Info
p.exists()
p.is_file()
p.is_dir()
p.parent    # Path("folder/subfolder")
p.name      # "file.txt"
p.stem      # "file"
p.suffix    # ".txt"

# Read / write
content = p.read_text(encoding="utf-8")
p.write_text("hello", encoding="utf-8")

# Create / delete
p.parent.mkdir(parents=True, exist_ok=True)
p.unlink()              # delete file
p.rename("new.txt")

# Find files
list(Path(".").glob("*.txt"))    # current dir
list(Path(".").rglob("*.py"))    # recursive
```

---

## Binary Files
*Images, PDFs, and other raw data*

```python
with open("image.png", "rb") as src:
    data = src.read()

with open("copy.png", "wb") as dst:
    dst.write(data)
```

---

## Best Practices

**Always use `with`** – Guarantees file is closed even on exception  
**Encoding** – Always specify `encoding="utf-8"` for text files  
**pathlib** – Prefer `Path` over string concatenation for paths  
**JSON** – Use `json.dump/load` for structured data, not raw text  
**newline=""** – Required in `open()` when writing CSV on Windows
