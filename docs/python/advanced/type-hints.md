---
sidebar_position: 3
---

# Type Hints

**Module 8 · Lesson 3** | Difficulty: Advanced

## Why Type Hints?

Type hints document expected types and enable static analysis with tools like **mypy**:

```python
def greet(name: str) -> str:
    return f"Hello, {name}!"
```

Hints are **not enforced at runtime** by default — they're for developers and tools.

## Basic Annotations

```python
age: int = 25
name: str = "Alice"
scores: list[float] = [90.5, 85.0]
person: dict[str, int] = {"age": 30}
```

## Function Signatures

```python
def add(a: int, b: int) -> int:
    return a + b

def process(items: list[str], limit: int = 10) -> None:
    for item in items[:limit]:
        print(item)
```

## Optional and Union

```python
from typing import Optional, Union

def find_user(id: int) -> Optional[str]:  # str or None
    ...

def parse(value: Union[int, str]) -> int:   # int or str
    ...
```

Python 3.10+ shorthand: `str | None`, `int | str`

## Collections

```python
from typing import List, Dict, Tuple, Set  # legacy
# Python 3.9+: use built-in list, dict, tuple, set

def matrix() -> list[list[int]]:
    return [[1, 2], [3, 4]]

def mapping() -> dict[str, list[int]]:
    return {"a": [1, 2]}
```

## Type Aliases and TypedDict

```python
from typing import TypedDict

class User(TypedDict):
    name: str
    age: int
    email: str

def create_user(data: User) -> User:
    return data
```

## Running mypy

```bash
pip install mypy
mypy your_module.py
```

## Practice

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Saidsp19/cognitive-vidya/blob/main/notebooks/python-course/08-advance./type-hints.ipynb)

**Next:** [Async Basics](./async)
