# Python Data Structures

## List
*Ordered, mutable, allows duplicates*

```python
nums = [1, 2, 3]
nums = list(range(5))    # [0, 1, 2, 3, 4]

# Access & Slicing
nums[0]       # 1
nums[-1]      # last
nums[1:3]     # [2, 3]
nums[::2]     # every 2nd
nums[::-1]    # reversed

# Modify
nums.append(4)           # add to end
nums.insert(0, 99)       # insert at index
nums.extend([5, 6])      # add multiple
nums.remove(2)           # remove first match
nums.pop()               # remove & return last
nums.pop(0)              # remove & return at index

# Info
len(nums)                # size
nums.index(3)            # find index of value
nums.count(2)            # count occurrences
3 in nums                # True/False

# Sort
nums.sort()              # in-place ascending
sorted(nums)             # returns new sorted list
nums.reverse()           # reverse in-place
```

---

## Tuple
*Ordered, immutable, allows duplicates*

```python
point = (3, 4)
single = (1,)        # trailing comma required
coords = 1, 2, 3     # parentheses optional

# Usage
point[0]       # 3
x, y = point   # unpacking

# Named tuple
from collections import namedtuple
Point = namedtuple("Point", ["x", "y"])
p = Point(3, 4)
p.x   # 3
p.y   # 4
```

---

## Dictionary
*Key-value pairs, ordered (3.7+), mutable*

```python
user = {"name": "Alice", "age": 25}
user = dict(name="Alice", age=25)

# Access
user["name"]              # "Alice"
user.get("email")         # None (no KeyError)
user.get("email", "N/A")  # default value

# Modify
user["age"] = 26
user["email"] = "a@b.com"
del user["age"]
user.pop("email")         # remove & return

# Iteration
for key in user:
for value in user.values():
for key, value in user.items():

# Useful
user.update({"age": 30})
user.setdefault("score", 0)  # set only if not exists
merged = d1 | d2             # merge (Python 3.9+)
```

---

## Set
*Unordered, unique elements, mutable*

```python
colors = {"red", "green", "blue"}
colors = set(["red", "red", "blue"])  # {"red", "blue"}
empty  = set()                         # NOT {} (that's dict)

# Modify
colors.add("yellow")
colors.remove("red")    # KeyError if not found
colors.discard("red")   # no error if not found

# Set operations
a = {1, 2, 3}
b = {2, 3, 4}

a | b   # {1,2,3,4}  union
a & b   # {2,3}      intersection
a - b   # {1}        difference
a ^ b   # {1,4}      symmetric difference

a.issubset(b)    # a <= b
a.issuperset(b)  # a >= b
a.isdisjoint(b)  # no common elements

# Frozenset (immutable)
fs = frozenset([1, 2, 3])
```

---

## Comprehensions
*Concise collection creation*

```python
# List
squares = [x**2 for x in range(10)]
evens   = [x for x in range(10) if x % 2 == 0]
flat    = [x for row in matrix for x in row]

# Dict
lengths  = {word: len(word) for word in ["hi", "hello"]}
inverted = {v: k for k, v in original.items()}

# Set
unique_lengths = {len(word) for word in words}

# Generator expression (lazy, no memory overhead)
total = sum(x**2 for x in range(1000))
```

---

## Collections Module
*Specialized data structures*

```python
from collections import Counter, defaultdict, deque

# Counter – count occurrences
c = Counter("hello")      # {'l':2, 'h':1, 'e':1, 'o':1}
c.most_common(2)          # [('l', 2), ('h', 1)]

# defaultdict – auto-create missing keys
d = defaultdict(list)
d["key"].append(1)        # no KeyError

d = defaultdict(int)
for word in words:
    d[word] += 1          # count words

# deque – efficient double-ended queue
q = deque([1, 2, 3])
q.appendleft(0)           # add to front
q.popleft()               # remove from front
q.append(4)               # add to end
```

---

## Sorting
*Sort collections*

```python
nums = [3, 1, 4, 1, 5]

sorted(nums)                    # new list ascending
sorted(nums, reverse=True)      # descending
nums.sort()                     # in-place

# Sort by key
words = ["banana", "apple", "kiwi"]
sorted(words, key=len)          # by length
sorted(words, key=str.lower)    # case-insensitive

# Sort objects
users = [{"name": "Bob", "age": 30}, {"name": "Alice", "age": 25}]
sorted(users, key=lambda u: u["age"])
sorted(users, key=lambda u: (u["age"], u["name"]))  # multiple keys
```

---

## Best Practices

**List vs Tuple** – Use tuple for fixed data, list for mutable sequences  
**Dict access** – Use `.get(key, default)` to avoid `KeyError`  
**Set** – Use for membership checks (`in`) — O(1) vs O(n) for lists  
**Comprehensions** – Prefer over `map()`/`filter()` for readability  
**defaultdict** – Use over manual `if key not in d:` checks
