---
sidebar_position: 2
---

# Inheritance

**Module 5 · Lesson 2** | Difficulty: Intermediate

## Extending Classes

**Inheritance** lets a child class reuse and extend a parent class:

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement")

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

Dog("Buddy").speak()  # Buddy says Woof!
```

## `super()` — Call Parent Methods

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department
```

## Method Overriding

Child replaces parent behavior while keeping the interface:

```python
class Shape:
    def area(self):
        raise NotImplementedError

class Rectangle(Shape):
    def __init__(self, w, h):
        self.w, self.h = w, h

    def area(self):
        return self.w * self.h
```

## Multiple Inheritance

```python
class Flyer:
    def fly(self):
        return "Flying!"

class Swimmer:
    def swim(self):
        return "Swimming!"

class Duck(Animal, Flyer, Swimmer):
    def speak(self):
        return "Quack!"

# Method Resolution Order (MRO)
Duck.__mro__
```

## `isinstance` and `issubclass`

```python
isinstance(Dog("x"), Animal)   # True
issubclass(Dog, Animal)        # True
```

## Practice

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Saidsp19/cognitive-vidya/blob/main/notebooks/python-course/05-oo./inheritance.ipynb)

**Next:** [Polymorphism](./polymorphism)
