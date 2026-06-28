---
sidebar_position: 1
---

# Classes & Objects

**Module 5 · Lesson 1** | Difficulty: Intermediate

<VideoEmbed videoId="Ej_02ICOIgs" title="Object-Oriented Programming in Python — Classes & Instances" />

## Object-Oriented Programming

OOP models real-world entities as **objects** with **attributes** (data) and **methods** (behavior).

```python
class Dog:
    def __init__(self, name, breed):
        self.name = name      # instance attribute
        self.breed = breed

    def bark(self):
        return f"{self.name} says Woof!"

buddy = Dog("Buddy", "Labrador")
print(buddy.name)    # Buddy
print(buddy.bark())  # Buddy says Woof!
```

## `__init__` Constructor

Called automatically when creating an instance. `self` refers to the current instance.

## Instance vs Class Attributes

```python
class Counter:
    count = 0  # class attribute — shared by all instances

    def __init__(self):
        Counter.count += 1
        self.id = Counter.count  # instance attribute
```

## Encapsulation

Convention: prefix with `_` for "internal use", `__` for name mangling:

```python
class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount

    def get_balance(self):
        return self._balance
```

## Properties

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius must be positive")
        self._radius = value

    @property
    def area(self):
        return 3.14159 * self._radius ** 2
```

## `__str__` and `__repr__`

```python
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"
```

## Practice

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Saidsp19/cognitive-vidya/blob/main/notebooks/python-course/05-oop/16-classes-objects.ipynb)

<LessonProgress lessonId="python/oop/classes-objects" />

**Next:** [Inheritance](./inheritance)
