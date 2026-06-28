---
sidebar_position: 3
---

# Dictionaries

**Module 3 · Lesson 3** | Difficulty: Beginner

## Key-Value Pairs

A **dictionary** maps unique keys to values — like a real dictionary maps words to definitions:

```python
person = {
    "name": "Alice",
    "age": 30,
    "city": "NYC"
}
```

Keys must be **immutable** (strings, numbers, tuples). Values can be anything.

## Accessing & Modifying

```python
person["name"]           # "Alice"
person.get("email", "N/A")  # safe access with default
person["email"] = "a@x.com"  # add or update
del person["city"]       # remove key
```

## Common Methods

```python
d = {"a": 1, "b": 2}
d.keys()      # dict_keys(['a', 'b'])
d.values()    # dict_values([1, 2])
d.items()     # dict_items([('a', 1), ('b', 2)])
d.pop("a")    # removes and returns value
d.update({"c": 3, "b": 99})
```

## Iterating

```python
for key in person:
    print(key, person[key])

for key, value in person.items():
    print(f"{key}: {value}")
```

## Dictionary Comprehension

```python
squares = {x: x**2 for x in range(6)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

## Nested Dictionaries

```python
users = {
    "alice": {"age": 30, "role": "admin"},
    "bob": {"age": 25, "role": "user"},
}
users["alice"]["role"]  # "admin"
```

## `defaultdict` and `Counter` (Preview)

```python
from collections import defaultdict, Counter

# Auto-create missing keys
counts = defaultdict(int)
for word in ["a", "b", "a"]:
    counts[word] += 1

# Frequency counting
Counter("abracadabra")  # Counter({'a': 5, 'b': 2, ...})
```

## Practice

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Saidsp19/cognitive-vidya/blob/main/notebooks/python-course/03-data-structure./dictionaries.ipynb)

**Next:** [Strings](./strings)
