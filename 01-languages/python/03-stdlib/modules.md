# Python Modules & Packages

## Importing
*Load external code*

```python
import math                   # import module
import math as m              # with alias
from math import sqrt         # import specific
from math import sqrt, pi     # import multiple
from math import *            # import all (avoid)

# Usage
math.sqrt(16)   # 4.0
m.pi            # 3.14159...
sqrt(16)        # 4.0
```

---

## Creating Modules
*Reusable .py files*

```python
# utils.py
def add(a, b):
    return a + b

MAX = 100
```

```python
# main.py
import utils
from utils import add

# Usage
utils.add(2, 3)   # 5
utils.MAX         # 100
add(2, 3)         # 5
```

### `__name__ == "__main__"`
*Run code only when executed directly*

```python
# script.py
def main():
    print("Running...")

if __name__ == "__main__":
    main()   # skipped when imported
```

---

## Packages
*Directories of modules*

```
mypackage/
├── __init__.py       # makes it a package
├── utils.py
└── models.py
```

```python
# Usage
from mypackage import utils
from mypackage.utils import add
```

---

## Standard Library
*Built-in batteries included*

### os
*File system and environment access*

```python
import os

os.getcwd()                   # current directory
os.listdir(".")               # list files
os.path.join("dir", "file")  # path join
os.path.exists("file.txt")   # check exists
os.makedirs("new/dir")        # create dirs
os.remove("file.txt")         # delete file
os.environ.get("HOME")        # env variable
```

### sys
*Runtime system info*

```python
import sys

sys.argv     # command line arguments
sys.exit(0)  # exit program
sys.path     # module search paths
sys.version  # Python version
```

### json
*Serialize and deserialize JSON*

```python
import json

data = {"name": "Alice", "age": 25}

# Dict ↔ string
json_str = json.dumps(data, indent=2)
data     = json.loads(json_str)

# Dict ↔ file
with open("data.json", "w") as f:
    json.dump(data, f, indent=2)

with open("data.json") as f:
    data = json.load(f)
```

### math
*Mathematical functions*

```python
import math

math.sqrt(16)      # 4.0
math.floor(3.7)    # 3
math.ceil(3.2)     # 4
math.pow(2, 10)    # 1024.0
math.log(100, 10)  # 2.0
math.pi            # 3.14159...
math.inf           # infinity
```

### random
*Random number generation*

```python
import random

random.random()              # float [0.0, 1.0)
random.randint(1, 10)        # int [1, 10]
random.choice([1, 2, 3])     # random element
random.shuffle(my_list)      # in-place shuffle
random.sample(my_list, k=3)  # k unique elements
random.seed(42)              # reproducible results
```

### pathlib
*Object-oriented filesystem paths*

```python
from pathlib import Path

p = Path("folder/file.txt")

p.parent     # Path("folder")
p.name       # "file.txt"
p.stem       # "file"
p.suffix     # ".txt"
p.exists()
p.read_text(encoding="utf-8")
p.write_text("content", encoding="utf-8")
list(p.parent.glob("*.txt"))   # find files
```

> For dates and times see `03-stdlib/datetime/notes.md`.
> For virtual environments and packaging see `05-tooling/packaging/notes.md`.

---

## Best Practices

**Imports** – Group: stdlib → third-party → local (PEP 8)  
**`from x import *`** – Avoid; pollutes namespace and hides origins  
**`__name__`** – Always guard script entry point with `if __name__ == "__main__":`  
**pathlib** – Prefer over `os.path` for path operations  
**`os.environ.get`** – Use over `os.environ[key]` to avoid KeyError  
