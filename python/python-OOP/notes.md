# Python OOP Notes

## Object-Oriented Programming
*Organizing code around objects and their interactions*

### Core Concepts
*Fundamental OOP principles*

**Object** – Entity combining data (attributes) and operations (methods)

**Benefits**: Reusability, Maintainability, Modifiability, Reliability

**Four Pillars**: Abstraction, Encapsulation, Inheritance, Polymorphism

---

### Classes and Objects
*Blueprints and instances*

**Class** – Template defining structure and behavior  
**Object** – Instance of a class with its own state

```python
# Define class
class Car:
    def __init__(self, model, year):
        self.model = model
        self.year = year
    
    def drive(self):
        print(f"{self.model} is driving")

# Create objects (instances)
car1 = Car("Tesla", 2024)
car2 = Car("BMW", 2023)
car1.drive()  # "Tesla is driving"
```

---

### Constructor (`__init__`)
*Initialize objects when created*

**`__init__`** – Special method called when object is created  
**`self`** – Reference to current instance

```python
class Person:
    def __init__(self, name, age=18):
        self.name = name
        self.age = age

# Usage
p1 = Person("Alice", 25)  # name="Alice", age=25
p2 = Person("Bob")        # name="Bob", age=18 (default)
```

---

### Attributes and Methods
*Object data and actions*

```python
class Example:
    # Class attribute (shared by all instances)
    count = 0
    MAX_SIZE = 100  # constant convention
    
    def __init__(self, name, age):
        # Instance attributes (each object has its own)
        self.name = name
        self.age = age
        Example.count += 1
    
    # Instance method
    def celebrate(self):
        self.age += 1
        print(f"{self.name} is now {self.age}")
    
    # Class method
    @classmethod
    def get_count(cls):
        return cls.count
    
    # Static method
    @staticmethod
    def is_adult(age):
        return age >= 18

# Usage
e1 = Example("Alice", 25)
e2 = Example("Bob", 30)

e1.celebrate()              # instance method
Example.get_count()         # class method: 2
Example.is_adult(20)        # static method: True
```

---

### Encapsulation
*Protecting and controlling data access*

**Access Levels**:
- `public` – normal attributes (no prefix)
- `_protected` – convention, use underscore prefix
- `__private` – name mangling, use double underscore prefix

```python
class User:
    def __init__(self, username, password):
        self.username = username      # public
        self._email = ""              # protected (convention)
        self.__password = password    # private (name mangling)
    
    # Getter
    def get_password(self):
        return self.__password
    
    # Setter with validation
    def set_password(self, password):
        if len(password) >= 8:
            self.__password = password
        else:
            print("Password too short")

# Usage
user = User("alice", "secret123")
user.username = "alice2"              # direct access (public)
user.set_password("newpass123")       # controlled access (private)
pwd = user.get_password()             # read via getter
```

---

### Properties
*Pythonic getters and setters*

**`@property`** – Access method like an attribute  
**`@setter`** – Set value with validation

```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self._price = price
    
    # Getter
    @property
    def price(self):
        return self._price
    
    # Setter
    @price.setter
    def price(self, value):
        if value >= 0:
            self._price = value
        else:
            raise ValueError("Price cannot be negative")
    
    # Read-only property
    @property
    def display_name(self):
        return f"{self.name} - ${self._price}"

# Usage
p = Product("Laptop", 999)
print(p.price)        # 999 (calls getter)
p.price = 1200        # calls setter
print(p.display_name) # "Laptop - $1200" (read-only)
```

---

### Magic Methods
*Special methods for operator overloading*

**Dunder methods** – Double underscore methods (`__method__`)

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    # String representation
    def __str__(self):
        return f"Point({self.x}, {self.y})"
    
    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"
    
    # Operator overloading
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    # Length
    def __len__(self):
        return int((self.x**2 + self.y**2)**0.5)

# Usage
p1 = Point(3, 4)
p2 = Point(1, 2)

print(p1)           # "Point(3, 4)" (calls __str__)
p3 = p1 + p2        # Point(4, 6) (calls __add__)
print(p1 == p2)     # False (calls __eq__)
print(len(p1))      # 5 (calls __len__)
```

**Common Magic Methods**:
- `__init__` – Constructor
- `__str__` – String for users
- `__repr__` – String for developers
- `__len__` – Length
- `__add__`, `__sub__`, `__mul__` – Arithmetic
- `__eq__`, `__lt__`, `__gt__` – Comparison
- `__getitem__`, `__setitem__` – Indexing

---

### Inheritance
*Reuse code through parent-child relationships*

**Single Inheritance** – One parent class

```python
# Parent class
class Animal:
    def __init__(self, name):
        self.name = name
    
    def eat(self):
        print(f"{self.name} is eating")

# Child class
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # call parent constructor
        self.breed = breed
    
    # Override parent method
    def eat(self):
        print(f"{self.name} is eating dog food")
    
    # New method
    def bark(self):
        print(f"{self.name} is barking")

# Usage
dog = Dog("Max", "Golden")
dog.eat()   # "Max is eating dog food" (overridden)
dog.bark()  # "Max is barking" (new method)
```

**Multiple Inheritance** – Multiple parent classes

```python
class Flyable:
    def fly(self):
        print("Flying")

class Swimmable:
    def swim(self):
        print("Swimming")

class Duck(Animal, Flyable, Swimmable):
    def __init__(self, name):
        super().__init__(name)

# Usage
duck = Duck("Donald")
duck.eat()   # from Animal
duck.fly()   # from Flyable
duck.swim()  # from Swimmable
```

**Method Resolution Order (MRO)** – Order of method lookup

```python
print(Duck.__mro__)  # shows inheritance chain
print(Duck.mro())    # same as above
```

---

### Abstract Classes
*Force child classes to implement methods*

**ABC** – Abstract Base Class module

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14 * self.radius

# Cannot instantiate abstract class
# shape = Shape()  # Error!

circle = Circle(5)
print(circle.area())  # 78.5
```

---

### Polymorphism
*One interface, multiple implementations*

**Method Overriding** – Child class redefines parent method

```python
class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")

# Runtime polymorphism
animals = [Dog(), Cat(), Dog()]
for animal in animals:
    animal.sound()  # calls appropriate method

# Duck typing (if it walks like a duck...)
class Robot:
    def sound(self):
        print("Robot beeps")

def make_sound(obj):
    obj.sound()  # works with any object that has sound()

make_sound(Dog())    # "Dog barks"
make_sound(Robot())  # "Robot beeps"
```

---

### Dataclasses
*Simplified class creation (Python 3.7+)*

**@dataclass** – Auto-generates `__init__`, `__repr__`, `__eq__`

```python
from dataclasses import dataclass, field

@dataclass
class Person:
    name: str
    age: int
    email: str = "unknown"  # default value

# Equivalent to:
# def __init__(self, name, age, email="unknown"):
#     self.name = name
#     self.age = age
#     self.email = email

p = Person("Alice", 25)
print(p)  # Person(name='Alice', age=25, email='unknown')

# With methods
@dataclass
class Point:
    x: int
    y: int
    
    def distance(self):
        return (self.x**2 + self.y**2)**0.5

# Immutable dataclass
@dataclass(frozen=True)
class ImmutablePoint:
    x: int
    y: int

# Advanced features
@dataclass
class Student:
    name: str
    grades: list = field(default_factory=list)  # mutable default
```

---

### Composition
*Building complex objects from simpler ones*

**"Has-a" relationship** – Object contains other objects

```python
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower
    
    def start(self):
        print(f"Engine with {self.horsepower}hp started")

class Car:
    def __init__(self, model, horsepower):
        self.model = model
        self.engine = Engine(horsepower)  # composition
    
    def start(self):
        print(f"Starting {self.model}")
        self.engine.start()

car = Car("Tesla", 500)
car.start()
# "Starting Tesla"
# "Engine with 500hp started"
```

---

### Class Relationships Summary

**Inheritance** – "Is-a" relationship
```python
class Dog(Animal):  # Dog IS-A Animal
    pass
```

**Composition** – "Has-a" relationship (strong)
```python
class Car:
    def __init__(self):
        self.engine = Engine()  # Car HAS-A Engine
```

**Aggregation** – "Has-a" relationship (weak)
```python
class Team:
    def __init__(self, players):
        self.players = players  # Team HAS players (created outside)
```

---

### Type Checking
*Check object types*

```python
class Animal:
    pass

class Dog(Animal):
    pass

dog = Dog()

# isinstance - check if object is instance of class
print(isinstance(dog, Dog))     # True
print(isinstance(dog, Animal))  # True (inheritance)
print(isinstance(dog, str))     # False

# issubclass - check if class inherits from another
print(issubclass(Dog, Animal))  # True
print(issubclass(Animal, Dog))  # False

# type - get exact type
print(type(dog))                # <class 'Dog'>
print(type(dog) == Dog)         # True
```

---

### Class vs Instance Variables

```python
class Counter:
    # Class variable (shared)
    total_count = 0
    
    def __init__(self, name):
        # Instance variable (unique per object)
        self.name = name
        self.count = 0
        Counter.total_count += 1
    
    def increment(self):
        self.count += 1

c1 = Counter("First")
c2 = Counter("Second")

c1.increment()
c1.increment()
c2.increment()

print(c1.count)              # 2 (instance)
print(c2.count)              # 1 (instance)
print(Counter.total_count)   # 2 (class - shared)
```

---

### Best Practices

**Naming Conventions**:
- Classes: `PascalCase`
- Methods/attributes: `snake_case`
- Private: `_protected`, `__private`
- Constants: `UPPER_SNAKE_CASE`

**Principles**:
- Single Responsibility – One class, one purpose
- Favor composition over inheritance
- Use properties for validation
- Keep methods short and focused
- Use abstract classes for contracts
- Prefer dataclasses for simple data holders