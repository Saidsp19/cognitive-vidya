---
sidebar_position: 3
---

# Decorators

**Module 7 · Lesson 3** | Difficulty: Advanced

## What Is a Decorator?

A **decorator** wraps a function to extend its behavior without modifying its source:

```python
def log_calls(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Finished {func.__name__}")
        return result
    return wrapper

@log_calls
def greet(name):
    return f"Hello, {name}!"

greet("Alice")
# Calling greet
# Finished greet
```

`@log_calls` is syntactic sugar for `greet = log_calls(greet)`.

## Preserving Metadata with `functools.wraps`

```python
from functools import wraps

def log_calls(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper
```

## Decorators with Arguments

```python
def repeat(n):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def say_hi():
    print("Hi!")
```

## Built-in Decorators

```python
class MyClass:
    @staticmethod
    def utility():
        pass

    @classmethod
    def from_string(cls, s):
        return cls(s)

    @property
    def value(self):
        return self._value
```

## Practical: Timing Decorator

```python
import time
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"{func.__name__} took {elapsed:.4f}s")
        return result
    return wrapper
```

## Practice

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Saidsp19/cognitive-vidya/blob/main/notebooks/python-course/07-intermediat./decorators.ipynb)

**Next:** [Context Managers](./context-managers)
