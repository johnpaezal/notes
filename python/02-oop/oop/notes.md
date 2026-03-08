# Python OOP

## Core Concepts
*Vocabulary and four pillars*

**Object** – Entity combining data (attributes) and behavior (methods)
**Class** – Blueprint/template for creating objects
**Four Pillars**: Encapsulation, Inheritance, Polymorphism, Abstraction

---

## Classes & Objects
*Define blueprints and create instances*

```python
class Car:
    wheels = 4                  # class attribute (shared by all)

    def __init__(self, model, year):
        self.model = model      # instance attribute (per object)
        self.year  = year

    def drive(self):            # instance method
        print(f"{self.model} is driving")

    @classmethod
    def describe(cls):          # class method
        return f"Cars have {cls.wheels} wheels"

    @staticmethod
    def is_vintage(year):       # static method
        return year < 1980

# Usage
car = Car("Tesla", 2024)
car.drive()               # "Tesla is driving"
Car.describe()            # "Cars have 4 wheels"
Car.is_vintage(1975)      # True
```

---

## Encapsulation
*Control and validate data access*

- `public` – normal attributes (no prefix)
- `_protected` – convention, underscore prefix
- `__private` – name mangling, double underscore

### Properties
*Pythonic getters and setters*

```python
class Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value

    @property
    def label(self):            # read-only
        return f"${self._price:.2f}"

# Usage
p = Product(100)
p.price = 150                   # calls setter
p.price                         # 150 (calls getter)
p.label                         # "$150.00"
```

---

## Magic Methods
*Protocol via dunder methods*

```python
class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __str__(self):          return f"Vector({self.x}, {self.y})"
    def __repr__(self):         return f"Vector(x={self.x}, y={self.y})"
    def __add__(self, other):   return Vector(self.x + other.x, self.y + other.y)
    def __eq__(self, other):    return self.x == other.x and self.y == other.y
    def __len__(self):          return int((self.x**2 + self.y**2)**0.5)

# Usage
v1, v2 = Vector(3, 4), Vector(1, 2)
str(v1)       # "Vector(3, 4)"
v1 + v2       # Vector(4, 6)
v1 == v2      # False
len(v1)       # 5
```

**Common dunders**: `__init__` · `__str__` · `__repr__` · `__len__` · `__add__` · `__eq__` · `__getitem__` · `__contains__`

---

## Inheritance
*Reuse via parent-child hierarchy*

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)      # call parent __init__
        self.breed = breed

    def speak(self):                # override parent method
        return f"{self.name} barks"

# Usage
dog = Dog("Max", "Golden")
dog.speak()                         # "Max barks"
isinstance(dog, Animal)             # True
isinstance(dog, Dog)                # True
```

### Abstract Classes
*Force subclasses to implement methods*

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self): ...

    @abstractmethod
    def perimeter(self): ...

class Circle(Shape):
    def __init__(self, r): self.r = r
    def area(self):        return 3.14 * self.r ** 2
    def perimeter(self):   return 2 * 3.14 * self.r

# Shape()             # TypeError – can't instantiate abstract class
Circle(5).area()      # 78.5
```

**MRO** – Use `ClassName.__mro__` to inspect the method resolution order.

---

## Polymorphism
*One interface, multiple behaviors*

```python
class Cat(Animal):
    def speak(self): return f"{self.name} meows"

class Robot:
    def speak(self): return "beep boop"

def make_sound(obj):
    print(obj.speak())      # duck typing — any object with .speak() works

# Usage
for obj in [Dog("Max", "Lab"), Cat("Whiskers"), Robot()]:
    make_sound(obj)
```

---

## Dataclasses
*Auto-generated boilerplate (Python 3.7+)*

**`@dataclass`** – Auto-generates `__init__`, `__repr__`, `__eq__`

```python
from dataclasses import dataclass, field

@dataclass
class User:
    name: str
    age: int
    tags: list = field(default_factory=list)   # mutable default

@dataclass(frozen=True)     # immutable — raises FrozenInstanceError on write
class Point:
    x: int
    y: int

# Usage
u = User("Alice", 25)
u                           # User(name='Alice', age=25, tags=[])
p = Point(3, 4)
```

---

## Composition
*Build complex objects from simpler ones*

**Inheritance** – "is-a" relationship (`Dog` is an `Animal`)
**Composition** – "has-a" relationship, strong (`Car` owns an `Engine`)
**Aggregation** – "has-a" relationship, weak (`Team` references external `Player`s)

```python
class Engine:
    def start(self): print("Engine started")

class Car:
    def __init__(self, model):
        self.model  = model
        self.engine = Engine()      # Car owns Engine (composition)

    def start(self):
        self.engine.start()
        print(f"{self.model} moving")

# Usage
Car("Tesla").start()
```

---

## Best Practices

**`@dataclass`** – Prefer over manual `__init__` for simple data containers  
**`@property`** – Use instead of explicit `get_x()` / `set_x()` methods  
**`super()`** – Always call in `__init__` when extending a parent class  
**Composition** – Favor over deep inheritance chains  
**ABC** – Use for shared interfaces; never instantiate directly  
