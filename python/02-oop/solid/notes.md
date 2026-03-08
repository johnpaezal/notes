# SOLID Principles

## Overview
*Five principles for clean OOP design*

**SOLID**: SRP, OCP, LSP, ISP, DIP

---

## S — Single Responsibility
*One class, one reason to change*

**SRP** – A class should have only one job

```python
# Bad – one class does too many things
class User:
    def save_to_db(self): ...
    def send_email(self): ...
    def generate_report(self): ...

# Good – each class has one responsibility
class UserRepository:
    def save(self, user): ...

class EmailService:
    def send(self, user, message): ...

class ReportGenerator:
    def generate(self, user): ...
```

---

## O — Open/Closed
*Open for extension, closed for modification*

**OCP** – Add new behavior without changing existing code

```python
# Bad – must modify class to add new discount type
class Order:
    def discount(self, type):
        if type == "vip":
            return 0.2
        elif type == "student":   # must edit class each time
            return 0.1

# Good – extend via subclass, never modify base
class Discount:
    def apply(self, price):
        return price

class VIPDiscount(Discount):
    def apply(self, price):
        return price * 0.8

class StudentDiscount(Discount):
    def apply(self, price):
        return price * 0.9

# Usage
def checkout(price, discount: Discount):
    return discount.apply(price)

checkout(100, VIPDiscount())      # 80
checkout(100, StudentDiscount())  # 90
```

---

## L — Liskov Substitution
*Subclasses must be substitutable for their parent*

**LSP** – Child class must behave correctly wherever parent is expected

```python
# Bad – Square breaks Rectangle's contract
class Rectangle:
    def set_width(self, w):  self.width = w
    def set_height(self, h): self.height = h
    def area(self):          return self.width * self.height

class Square(Rectangle):
    def set_width(self, w):  # violates LSP
        self.width = self.height = w
    def set_height(self, h):
        self.width = self.height = h

# Good – separate classes with a shared interface
class Shape:
    def area(self): ...

class Rectangle(Shape):
    def __init__(self, w, h): self.w, self.h = w, h
    def area(self): return self.w * self.h

class Square(Shape):
    def __init__(self, s): self.s = s
    def area(self): return self.s ** 2

# Usage
shapes = [Rectangle(3, 4), Square(5)]
for shape in shapes:
    print(shape.area())   # works for all Shape subtypes
```

---

## I — Interface Segregation
*No class should depend on methods it doesn't use*

**ISP** – Split large interfaces into smaller, specific ones

```python
# Bad – Animal forced to implement methods it can't use
class Animal:
    def fly(self): ...
    def swim(self): ...
    def run(self): ...

class Dog(Animal):
    def fly(self): raise NotImplementedError  # Dog can't fly!

# Good – small, focused interfaces
class Runnable:
    def run(self): ...

class Swimmable:
    def swim(self): ...

class Flyable:
    def fly(self): ...

class Dog(Runnable, Swimmable):
    def run(self):  print("Running")
    def swim(self): print("Swimming")

class Bird(Runnable, Flyable):
    def run(self): print("Running")
    def fly(self): print("Flying")
```

---

## D — Dependency Inversion
*Depend on abstractions, not on concrete classes*

**DIP** – High-level modules should not depend on low-level modules

```python
# Bad – Order is tightly coupled to MySQLDatabase
class MySQLDatabase:
    def save(self, data): ...

class Order:
    def __init__(self):
        self.db = MySQLDatabase()   # hard dependency

    def place(self, data):
        self.db.save(data)

# Good – depend on abstraction (interface)
from abc import ABC, abstractmethod

class Database(ABC):
    @abstractmethod
    def save(self, data): ...

class MySQLDatabase(Database):
    def save(self, data): print(f"MySQL: {data}")

class MongoDatabase(Database):
    def save(self, data): print(f"Mongo: {data}")

class Order:
    def __init__(self, db: Database):   # inject dependency
        self.db = db

    def place(self, data):
        self.db.save(data)

# Usage
order = Order(MySQLDatabase())
order.place({"item": "laptop"})

order = Order(MongoDatabase())   # swap DB without touching Order
order.place({"item": "laptop"})
```

---

## Quick Reference

| Principle | Key Idea | Violation Signal |
|-----------|----------|-----------------|
| **SRP** | One class, one job | Class has methods from different domains |
| **OCP** | Extend, don't modify | Adding features requires editing existing code |
| **LSP** | Subtypes are substitutable | Child raises `NotImplementedError` or breaks parent contract |
| **ISP** | Small, focused interfaces | Class implements methods it doesn't use |
| **DIP** | Depend on abstractions | Class instantiates its own dependencies with `= ConcreteClass()` |

---

## Best Practices

**SRP** – If you need "and" to describe a class, split it  
**OCP** – Use inheritance or composition to add behavior  
**LSP** – If a subclass breaks parent behavior, reconsider the hierarchy  
**ISP** – Prefer many small abstract classes over one large one  
**DIP** – Inject dependencies via constructor, not inside the class
