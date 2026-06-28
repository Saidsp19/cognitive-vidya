---
sidebar_position: 2
---

# Generators & Iterators

**Module 7 · Lesson 2** | Difficulty: Advanced

## Iterators

An **iterator** is an object with `__iter__()` and `__next__()`:

```python
nums = iter([1, 2, 3])
next(nums)  # 1
next(nums)  # 2
next(nums)  # 3
next(nums)  # StopIteration
```

## Generator Functions

Use `yield` to produce values lazily:

```python
def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1

for num in count_up_to(5):
    print(num)  # 1 2 3 4 5
```

Generators are **memory-efficient** — they produce one value at a time.

## Generator Expression

```python
squares = (x**2 for x in range(1000000))
```

## `yield from` — Delegate to Sub-Generator

```python
def chain(*iterables):
    for it in iterables:
        yield from it

list(chain([1, 2], [3, 4]))  # [1, 2, 3, 4]
```

## Practical: Reading Large Files

```python
def read_lines(path):
    with open(path) as f:
        for line in f:
            yield line.strip()

for line in read_lines("huge_file.txt"):
    process(line)  # one line in memory at a time
```

## `itertools` Module

```python
from itertools import count, cycle, islice, chain, combinations

list(islice(count(10), 5))       # [10, 11, 12, 13, 14]
list(combinations("ABC", 2))     # [('A','B'), ('A','C'), ('B','C')]
```

## Practice

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Saidsp19/cognitive-vidya/blob/main/notebooks/python-course/07-intermediat./generators.ipynb)

**Next:** [Decorators](./decorators)
