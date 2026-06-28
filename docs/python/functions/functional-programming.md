---
sidebar_position: 3
---

# Functional Programming

**Module 4 · Lesson 3** | Difficulty: Intermediate

## First-Class Functions

Functions are objects — pass them as arguments, return them, store in variables:

```python
def apply(func, value):
    return func(value)

apply(abs, -5)    # 5
apply(str.upper, "hello")  # error — use lambda instead
```

## Lambda Functions

Anonymous one-line functions:

```python
square = lambda x: x ** 2
square(4)  # 16

# common with sorted()
students = [("Alice", 90), ("Bob", 85)]
sorted(students, key=lambda s: s[1], reverse=True)
```

## `map`, `filter`, `reduce`

```python
nums = [1, 2, 3, 4, 5]

list(map(lambda x: x ** 2, nums))     # [1, 4, 9, 16, 25]
list(filter(lambda x: x % 2 == 0, nums))  # [2, 4]

from functools import reduce
reduce(lambda acc, x: acc + x, nums)  # 15
```

:::tip
List comprehensions often replace `map`/`filter` with clearer syntax:
`[x**2 for x in nums if x % 2 == 0]`
:::

## Higher-Order Functions

```python
def pipeline(data, *funcs):
    result = data
    for func in funcs:
        result = func(result)
    return result

def strip(s): return s.strip()
def upper(s): return s.upper()

pipeline("  hello  ", strip, upper)  # "HELLO"
```

## `functools.partial`

Pre-fill arguments:

```python
from functools import partial

def power(base, exp):
    return base ** exp

square = partial(power, exp=2)
cube = partial(power, exp=3)
square(5)  # 25
```

## Practice

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Saidsp19/cognitive-vidya/blob/main/notebooks/python-course/04-function./functional-programming.ipynb)

**Next:** [Classes & Objects](../oop/classes-objects) — Module 5
