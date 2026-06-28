---
sidebar_position: 3
---

# Polymorphism & Special Methods

**Module 5 · Lesson 3** | Difficulty: Intermediate

## Polymorphism

**Polymorphism** — "many forms" — lets different types respond to the same interface:

```python
def animal_sound(animal):
    print(animal.speak())

animal_sound(Dog("Rex"))   # Rex says Woof!
animal_sound(Cat("Luna"))  # Luna says Meow!
```

## Duck Typing

"If it walks like a duck and quacks like a duck, it's a duck."

```python
class Duck:
    def speak(self):
        return "Quack!"

# No inheritance needed — just implement speak()
animal_sound(Duck())
```

## Essential Dunder Methods

| Method | Purpose | Example |
|--------|---------|---------|
| `__init__` | Constructor | `obj = Class()` |
| `__str__` | Human-readable string | `print(obj)` |
| `__repr__` | Developer representation | `repr(obj)` |
| `__len__` | Length | `len(obj)` |
| `__getitem__` | Indexing | `obj[0]` |
| `__eq__` | Equality | `obj == other` |
| `__lt__` | Less than | `obj < other` |
| `__add__` | Addition | `obj + other` |

```python
class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

Vector(1, 2) + Vector(3, 4)  # Vector(4, 6)
```

## Abstract Base Classes

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14159 * self.r ** 2
```

## Practice

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Saidsp19/cognitive-vidya/blob/main/notebooks/python-course/05-oo./polymorphism.ipynb)

**Next:** [Exception Handling](../files-errors/exception-handling) — Module 6
