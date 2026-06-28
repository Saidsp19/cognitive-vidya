---
sidebar_position: 5
---

# Python Best Practices

**Module 8 · Lesson 5** | Difficulty: Expert

<VideoEmbed videoId="wf-BqAjZb8M" title="Python Best Practices — Writing Clean, Pythonic Code" />

## PEP 8 Style Guide

Follow the official Python style guide:

```python
# Good
def calculate_total(items: list[float]) -> float:
    return sum(items)

# Bad
def CalculateTotal(Items):
    return sum(Items)
```

Key rules:
- 4 spaces for indentation
- Max line length: 79–88 characters
- `snake_case` for functions/variables
- `PascalCase` for classes
- `UPPER_SNAKE` for constants

## The Zen of Python

```python
import this
```

Highlights: *Beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex. Readability counts.*

## Pythonic Idioms

```python
# Swap
a, b = b, a

# Default dict value
counts = {}
counts[key] = counts.get(key, 0) + 1

# Unpacking
first, *middle, last = [1, 2, 3, 4, 5]

# Truthiness
if items:  # not: if len(items) > 0
    process(items)

# enumerate over range(len())
for i, item in enumerate(items):
    ...

# open files with context manager
with open("f.txt") as f:
    ...
```

## Error Handling Best Practices

- Catch specific exceptions, not bare `except:`
- Use EAFP where appropriate
- Fail fast with clear error messages
- Log errors in production code

## Performance Tips

1. **Profile first** — `cProfile`, `timeit`
2. Use **built-ins** and standard library (written in C)
3. Use **generators** for large datasets
4. Use **`set`** for membership tests
5. Use **list comprehensions** over manual loops
6. For heavy numerics, use **NumPy**

## Project Structure

```
myproject/
├── src/
│   └── mypackage/
│       ├── __init__.py
│       ├── core.py
│       └── utils.py
├── tests/
│   └── test_core.py
├── requirements.txt
├── pyproject.toml
└── README.md
```

## What's Next?

You've completed the Python course! Continue to **DSA Patterns** in the sidebar to apply your skills to interview-style problems:

- Sliding Window, HashMap, Stack, Binary Search, Two Pointers, DP, BFS/DFS, Heap & Linked List

## Practice

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Saidsp19/cognitive-vidya/blob/main/notebooks/python-course/08-advanced/30-best-practices.ipynb)

<LessonProgress lessonId="python/advanced/best-practices" />

Take the [DSA Patterns Quiz](../quizzes/dsa) and claim your **[Certificate](/certificate)**!

**Congratulations — you're ready for expert-level Python and DSA!**
