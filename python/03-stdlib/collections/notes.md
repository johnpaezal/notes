# Python Collections

## Overview
*Specialized container datatypes*

**`Counter`** – Count occurrences of elements
**`defaultdict`** – Dict with automatic default values
**`namedtuple`** – Tuple with named fields
**`deque`** – Double-ended queue (fast append/pop both ends)
**`OrderedDict`** – Dict that remembers insertion order (Python 3.7+ dicts do too)

---

## Counter
*Count elements in an iterable*

```python
from collections import Counter

words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
count = Counter(words)

count["apple"]          # 3
count["banana"]         # 2
count.most_common(2)    # [("apple", 3), ("banana", 2)]
count.total()           # 6

# Arithmetic
a = Counter(["a", "b", "a"])
b = Counter(["a", "c"])
a + b   # Counter({"a": 3, "b": 1, "c": 1})
a - b   # Counter({"a": 1, "b": 1})
```

---

## defaultdict
*Dict that never raises KeyError*

```python
from collections import defaultdict

# Automatic default value by type
word_count = defaultdict(int)
word_count["apple"] += 1    # no KeyError — starts at 0
word_count["apple"] += 1
word_count["apple"]         # 2

# Group items without manual init
groups = defaultdict(list)
for word in ["cat", "car", "bat", "bar", "can"]:
    groups[word[0]].append(word)

# groups → {"c": ["cat", "car", "can"], "b": ["bat", "bar"]}
```

---

## namedtuple
*Tuple with readable field names*

```python
from collections import namedtuple

Point  = namedtuple("Point",  ["x", "y"])
Person = namedtuple("Person", ["name", "age", "email"])

# Usage
p = Point(3, 4)
p.x         # 3
p.y         # 4
p[0]        # 3  (still indexable)
x, y = p   # still unpackable

person = Person("Alice", 25, "alice@example.com")
person.name     # "Alice"
person._asdict()  # {"name": "Alice", "age": 25, "email": "..."}
```

---

## deque
*Fast double-ended queue*

```python
from collections import deque

q = deque([1, 2, 3])

q.append(4)        # add right  → [1, 2, 3, 4]
q.appendleft(0)    # add left   → [0, 1, 2, 3, 4]
q.pop()            # remove right → 4
q.popleft()        # remove left  → 0

# Fixed-size buffer (keeps last n items)
log = deque(maxlen=3)
for i in range(5):
    log.append(i)
list(log)          # [2, 3, 4]

# Rotate
q = deque([1, 2, 3, 4, 5])
q.rotate(2)        # [4, 5, 1, 2, 3]
```

---

## ChainMap
*Combine multiple dicts into one view*

```python
from collections import ChainMap

defaults = {"color": "red",  "size": "M"}
overrides = {"color": "blue"}

config = ChainMap(overrides, defaults)
config["color"]   # "blue"   (from overrides)
config["size"]    # "M"      (from defaults)
```

---

## Best Practices

**`Counter`** – Use over manual dict counting; supports arithmetic and `most_common`  
**`defaultdict`** – Use over `if key not in d: d[key] = []` patterns  
**`namedtuple`** – Use for simple immutable data records; prefer `@dataclass` for mutability  
**`deque`** – Use over list when you need fast `appendleft` / `popleft` (O(1) vs O(n))  
**`ChainMap`** – Use for layered config (defaults → env → user overrides)  
