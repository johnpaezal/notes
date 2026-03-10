# Python Control Flow

## Conditionals
*Execute code based on conditions*

### if / elif / else
*Branch based on boolean expressions*

```python
age = 20

if age < 13:
    print("Child")
elif age < 18:
    print("Teen")
else:
    print("Adult")

# One-liner (ternary)
label = "Adult" if age >= 18 else "Minor"
```

### Truthiness Check
*Evaluate non-boolean values as bool*

```python
name = ""
if not name:
    print("Name is empty")

items = [1, 2, 3]
if items:
    print("List has items")
```

---

## Match-Case
*Pattern matching (Python 3.10+)*

```python
status = 404

match status:
    case 200:
        print("OK")
    case 404:
        print("Not Found")
    case 500 | 503:
        print("Server Error")
    case _:
        print("Unknown")

# Match with guard
match point:
    case (x, y) if x == y:
        print("Diagonal")
    case (x, y):
        print(f"Point at {x}, {y}")
```

---

## For Loops
*Iterate over sequences*

```python
# Basic
for i in range(5):        # 0, 1, 2, 3, 4
    print(i)

for i in range(2, 10, 2): # 2, 4, 6, 8
    print(i)

# Iterate list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# With index
for i, fruit in enumerate(fruits):
    print(i, fruit)

# Two lists together
for name, age in zip(["Alice", "Bob"], [25, 30]):
    print(name, age)

# Reverse
for fruit in reversed(fruits):
    print(fruit)
```

---

## While Loops
*Repeat while condition is true*

```python
count = 0
while count < 5:
    print(count)
    count += 1

# With else (runs if loop wasn't broken)
while count < 5:
    count += 1
else:
    print("Done")
```

---

## Loop Control
*Modify loop execution*

**`break`** – Exit loop immediately
**`continue`** – Skip to next iteration
**`pass`** – Do nothing (placeholder)

```python
for i in range(10):
    if i == 3:
        continue    # skip 3
    if i == 7:
        break       # stop at 7
    print(i)        # prints 0,1,2,4,5,6
```

---

## Comprehension-based Filtering
*Short loops inline*

```python
# List comprehension
evens = [x for x in range(10) if x % 2 == 0]

# Nested
pairs = [(x, y) for x in range(3) for y in range(3)]
```

> See `data-structures/notes.md` for full comprehension syntax.

---

## Best Practices

**Ternary** – Use `x if cond else y` for simple one-liners only  
**Match-Case** – Prefer over long if/elif chains (Python 3.10+)  
**Truthiness** – Use `if items:` over `if len(items) > 0:`  
**Loop else** – Rarely needed; use only when the distinction is clear
