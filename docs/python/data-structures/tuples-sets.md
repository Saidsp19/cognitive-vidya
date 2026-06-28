---
sidebar_position: 2
---

# Tuples & Sets

**Module 3 · Lesson 2** | Difficulty: Beginner

## Tuples — Immutable Sequences

A **tuple** is like a list but **cannot be changed** after creation:

```python
point = (3, 4)
colors = ("red", "green", "blue")
single = (42,)       # note the comma for single-element tuple
not_tuple = (42)     # just an int in parentheses
```

### Why Use Tuples?

- **Immutable** — safe as dictionary keys, function return values
- **Faster** than lists for fixed data
- **Unpacking** — elegant multiple assignment

```python
x, y = (10, 20)           # unpacking
name, age, city = ("Alice", 30, "NYC")

# swap without temp variable
a, b = 1, 2
a, b = b, a
```

### Tuple Methods

```python
t = (1, 2, 2, 3)
t.count(2)    # 2
t.index(3)    # 3
```

## Sets — Unique Unordered Collections

A **set** stores unique elements with no guaranteed order:

```python
nums = {1, 2, 3, 3, 3}   # {1, 2, 3}
empty = set()             # not {} — that's a dict!
```

### Set Operations

```python
a = {1, 2, 3}
b = {3, 4, 5}

a | b    # union: {1, 2, 3, 4, 5}
a & b    # intersection: {3}
a - b    # difference: {1, 2}
a ^ b    # symmetric difference: {1, 2, 4, 5}
```

### Modifying Sets

```python
s = {1, 2}
s.add(3)          # {1, 2, 3}
s.discard(2)      # {1, 3}  (no error if missing)
s.remove(1)       # raises KeyError if missing
```

### Removing Duplicates from a List

```python
items = [1, 2, 2, 3, 3, 3]
unique = list(set(items))   # order not preserved
# preserve order:
seen = set()
result = []
for x in items:
    if x not in seen:
        seen.add(x)
        result.append(x)
```

## Comparison Table

| Feature | List | Tuple | Set |
|---------|------|-------|-----|
| Ordered | Yes | Yes | No |
| Mutable | Yes | No | Yes |
| Duplicates | Yes | Yes | No |
| Indexing | Yes | Yes | No |

## Practice

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Saidsp19/cognitive-vidya/blob/main/notebooks/python-course/03-data-structure./tuples-sets.ipynb)

**Next:** [Dictionaries](./dictionaries)
