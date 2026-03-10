# Python Design Patterns

## Overview
*Reusable solutions to common problems*

**Creational** – How objects are created
**Structural** – How objects are composed
**Behavioral** – How objects communicate

---

## Singleton
*Ensure only one instance exists*

```python
class Config:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.debug = False
        return cls._instance

# Usage
a = Config()
b = Config()
a is b          # True — same instance
a.debug = True
b.debug         # True
```

---

## Factory
*Create objects without specifying exact class*

```python
class Dog:
    def speak(self): return "Woof"

class Cat:
    def speak(self): return "Meow"

def animal_factory(kind):
    animals = {"dog": Dog, "cat": Cat}
    cls = animals.get(kind)
    if not cls:
        raise ValueError(f"Unknown animal: {kind}")
    return cls()

# Usage
pet = animal_factory("dog")
pet.speak()    # "Woof"
```

---

## Observer
*Notify multiple objects on state change*

```python
class EventEmitter:
    def __init__(self):
        self._listeners = []

    def subscribe(self, fn):
        self._listeners.append(fn)

    def emit(self, event):
        for fn in self._listeners:
            fn(event)

# Usage
emitter = EventEmitter()
emitter.subscribe(lambda e: print(f"Handler A: {e}"))
emitter.subscribe(lambda e: print(f"Handler B: {e}"))
emitter.emit("user.created")
# Handler A: user.created
# Handler B: user.created
```

---

## Strategy
*Swap algorithms at runtime*

```python
from abc import ABC, abstractmethod

class SortStrategy(ABC):
    @abstractmethod
    def sort(self, data): ...

class BubbleSort(SortStrategy):
    def sort(self, data): return sorted(data)   # simplified

class QuickSort(SortStrategy):
    def sort(self, data): return sorted(data, reverse=False)

class Sorter:
    def __init__(self, strategy: SortStrategy):
        self.strategy = strategy

    def sort(self, data):
        return self.strategy.sort(data)

# Usage
sorter = Sorter(QuickSort())
sorter.sort([3, 1, 2])          # [1, 2, 3]

sorter.strategy = BubbleSort()  # swap strategy at runtime
```

---

## Decorator Pattern
*Add behavior to objects dynamically*

```python
class Coffee:
    def cost(self): return 5
    def description(self): return "Coffee"

class MilkDecorator:
    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self): return self._coffee.cost() + 1
    def description(self): return self._coffee.description() + ", Milk"

# Usage
drink = MilkDecorator(Coffee())
drink.cost()           # 6
drink.description()    # "Coffee, Milk"
```

---

## Repository
*Abstract data access from business logic*

```python
from abc import ABC, abstractmethod

class UserRepository(ABC):
    @abstractmethod
    def find(self, id): ...
    @abstractmethod
    def save(self, user): ...

class InMemoryUserRepository(UserRepository):
    def __init__(self): self._store = {}
    def find(self, id): return self._store.get(id)
    def save(self, user): self._store[user["id"]] = user

# Usage
repo = InMemoryUserRepository()
repo.save({"id": 1, "name": "Alice"})
repo.find(1)   # {"id": 1, "name": "Alice"}
```

---

## Best Practices

**Singleton** – Use sparingly; prefer dependency injection over global state  
**Factory** – Use when object creation logic is complex or varies  
**Observer** – Use for event-driven decoupling between components  
**Strategy** – Use to avoid conditionals for swappable algorithms  
**Repository** – Always abstract DB access; enables easy testing with fakes  
