# Python Functions

## Defining Functions
*Reusable blocks of code*

```python
def greet(name):
    return f"Hello, {name}"

# Usage
result = greet("Alice")  # "Hello, Alice"
```

---

## Parameters
*How functions receive data*

### Types of Parameters
*Positional, keyword, and special markers*

```python
def example(pos, /, normal, *, kw_only):
    pass

# Positional-only  (before /)
# Normal           (positional or keyword)
# Keyword-only     (after *)
```

### Default Values
*Fallback when argument is omitted*

```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}"

# Usage
greet("Alice")       # "Hello, Alice"
greet("Bob", "Hi")   # "Hi, Bob"
```

### *args and **kwargs
*Variable number of arguments*

```python
# *args – variable positional (tuple)
def sum_all(*args):
    return sum(args)

# **kwargs – variable keyword (dict)
def show_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Usage
sum_all(1, 2, 3, 4)             # 10
show_info(name="Alice", age=25)
```

### Unpacking at Call Site
*Spread iterable/dict as arguments*

```python
nums = [1, 2, 3]
print(*nums)              # print(1, 2, 3)

data = {"sep": "-", "end": "\n"}
print("a", "b", **data)  # a-b
```

---

## Return Values
*What a function gives back*

```python
def divide(a, b):
    if b == 0:
        return None
    return a / b

# Multiple return values (tuple)
def min_max(nums):
    return min(nums), max(nums)

# Usage
low, high = min_max([3, 1, 4, 1, 5])
```

---

## Lambda Functions
*Anonymous single-expression functions*

```python
square = lambda x: x ** 2

# Usage
square(5)    # 25

users = [{"name": "Bob", "age": 30}, {"name": "Alice", "age": 25}]
users.sort(key=lambda u: u["age"])

nums = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, nums))       # [2,4,6,8,10]
evens   = list(filter(lambda x: x % 2 == 0, nums)) # [2,4]
```

---

## Closures
*Function that captures surrounding variables*

```python
def make_counter(start=0):
    count = start
    def increment():
        nonlocal count
        count += 1
        return count
    return increment

# Usage
counter = make_counter()
counter()  # 1
counter()  # 2
```

---

## Decorators
*Wrap functions to add behavior*

```python
from functools import wraps

def log(func):
    @wraps(func)            # preserve original metadata
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print("Done")
        return result
    return wrapper

# Usage
@log
def add(a, b):
    return a + b

add(2, 3)
# Calling add
# Done
```

### Decorator with Arguments
*Parametrize the decorator itself*

```python
def repeat(n):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

# Usage
@repeat(3)
def say_hi():
    print("Hi")

say_hi()  # prints "Hi" 3 times
```

---

## Generators
*Lazy sequences with yield*

**`yield`** – Pause function, produce value, resume later

```python
def count_up(n):
    for i in range(n):
        yield i

# Usage
gen = count_up(3)
next(gen)   # 0
next(gen)   # 1

for val in count_up(5):
    print(val)

# Generator expression (lazy)
squares = (x**2 for x in range(10))
```

### When to Use Generators
*Use over lists for large or infinite data*

- Large datasets (don't load all in memory)
- Infinite sequences
- Pipelines

```python
def integers():
    n = 0
    while True:
        yield n
        n += 1

# Usage
gen = integers()
next(gen)   # 0
next(gen)   # 1
```

---

## Scope
*Where variables are accessible*

**LEGB Rule**: Local → Enclosing → Global → Built-in

```python
x = "global"

def outer():
    x = "enclosing"
    def inner():
        x = "local"
        print(x)    # "local"
    inner()
    print(x)        # "enclosing"

outer()
print(x)            # "global"

# Modify outer scope
def modify():
    global x
    x = "modified"

def outer2():
    y = 10
    def inner2():
        nonlocal y
        y += 1
    inner2()
    print(y)  # 11
```

---

## Best Practices

**Lambda** – Use only for simple one-liners; use `def` for anything complex  
**Generators** – Prefer over lists when iterating large sequences once  
**Decorators** – Always use `@wraps(func)` to preserve metadata  
**`*args/**kwargs`** – Use when the number of arguments is genuinely variable  
**Closures** – Use `nonlocal` to modify enclosing scope variables
