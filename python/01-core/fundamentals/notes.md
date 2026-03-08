# Python Fundamentals

## Variables and Types
*Basic data and how to store it*

**int** – Whole numbers  
**float** – Decimal numbers  
**str** – Text (single or double quotes)  
**bool** – `True` / `False`  
**None** – Absence of value

```python
age = 25
price = 9.99
name = "Alice"
active = True
data = None

# Multiple assignment
x = y = z = 0
a, b, c = 1, 2, 3

# Usage
type(age)            # <class 'int'>
isinstance(age, int) # True
```

---

## Type Conversion
*Convert between data types*

```python
int("42")     # 42
float("3.14") # 3.14
str(100)      # "100"
bool(0)       # False
bool("hello") # True

# Falsy: 0, 0.0, "", [], {}, None, False
# Truthy: everything else
```

---

## Operators
*Perform operations on values*

### Arithmetic
*Math operations on numbers*

```python
10 + 3   # 13   addition
10 - 3   # 7    subtraction
10 * 3   # 30   multiplication
10 / 3   # 3.33 division (always float)
10 // 3  # 3    floor division
10 % 3   # 1    modulo (remainder)
10 ** 3  # 1000 exponentiation
```

### Comparison
*Compare values, return bool*

```python
x == y   # equal
x != y   # not equal
x > y    # greater than
x < y    # less than
x >= y   # greater or equal
x <= y   # less or equal
```

### Logical
*Combine boolean expressions*

```python
True and False  # False
True or False   # True
not True        # False
```

### Assignment
*Update variable in place*

```python
x += 5   # x = x + 5
x -= 5   # x = x - 5
x *= 2   # x = x * 2
x //= 2  # x = x // 2
x **= 2  # x = x ** 2
```

### Bitwise
*Operate on bits*

```python
5 & 3   # 1   AND
5 | 3   # 7   OR
5 ^ 3   # 6   XOR
~5      # -6  NOT
5 << 1  # 10  left shift
5 >> 1  # 2   right shift
```

---

## Strings
*Text manipulation and formatting*

### Access and Slicing
*Navigate characters in a string*

```python
s = "Hello, World"

# Usage
s[0]     # "H"
s[-1]    # "d"
s[0:5]   # "Hello"
s[7:]    # "World"
s[::2]   # every 2nd char
s[::-1]  # reversed
```

### Common Methods
*Built-in string operations*

```python
s = "Hello, World"

# Usage
s.upper()            # "HELLO, WORLD"
s.lower()            # "hello, world"
s.strip()            # remove leading/trailing whitespace
s.split(", ")        # ["Hello", "World"]
s.replace("o", "0")  # "Hell0, W0rld"
s.startswith("He")   # True
s.endswith("ld")     # True
"World" in s         # True
len(s)               # 12
```

### Formatting
*Embed values into strings*

```python
name = "Alice"
age = 25

# f-string (preferred)
f"Name: {name}, Age: {age}"          # "Name: Alice, Age: 25"
f"{age:.2f}"                         # "25.00"
f"{name!r}"                          # "'Alice'"

# .format()
"Name: {}, Age: {}".format(name, age)

# Multiline
text = """
Line 1
Line 2
"""
```

---

## Input / Output
*Read from user, write to console*

```python
# Output
print("Hello")
print("Name:", name, "Age:", age)
print(f"Score: {score}", end="")  # no newline
print("a", "b", sep="-")         # "a-b"

# Usage
name = input("Enter name: ")     # always returns str
age = int(input("Enter age: "))  # convert to int
```

---

## Naming Conventions
*Standard Python naming rules*

| Type | Convention | Example |
|------|-----------|---------|
| Variable | `snake_case` | `user_name` |
| Constant | `UPPER_SNAKE_CASE` | `MAX_SIZE` |
| Function | `snake_case` | `get_user()` |
| Class | `PascalCase` | `UserAccount` |
| Module | `snake_case` | `my_module.py` |
| Private | `_prefix` | `_internal` |

---

## Best Practices

**Type Safety** – Use `isinstance()` over `type() ==` for type checks  
**Strings** – Prefer f-strings over `.format()` or `%`  
**Assignment** – Use augmented operators (`+=`, `*=`) when modifying in place  
**Naming** – Follow conventions always — readability over brevity
