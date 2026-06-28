---
sidebar_position: 2
---

# Scope & Closures

**Module 4 · Lesson 2** | Difficulty: Intermediate

## LEGB Rule

Python looks up names in this order:

1. **L**ocal — inside the current function
2. **E**nclosing — in outer functions (closures)
3. **G**lobal — module level
4. **B**uilt-in — `print`, `len`, etc.

```python
x = "global"

def outer():
    x = "enclosing"
    def inner():
        x = "local"
        print(x)   # local
    inner()

outer()
print(x)  # global
```

## `global` and `nonlocal`

```python
count = 0

def increment():
    global count
    count += 1

def outer():
    n = 0
    def inner():
        nonlocal n
        n += 1
        return n
    return inner
```

Avoid `global` when possible — prefer passing values and returning results.

## Closures

A closure captures variables from its enclosing scope:

```python
def make_multiplier(factor):
    def multiply(x):
        return x * factor  # factor captured from enclosing scope
    return multiply

double = make_multiplier(2)
triple = make_multiplier(3)
double(5)   # 10
triple(5)   # 15
```

## Practical Closure Example

```python
def make_validator(min_val, max_val):
    def validate(x):
        return min_val <= x <= max_val
    return validate

is_percent = make_validator(0, 100)
is_percent(50)   # True
is_percent(150)  # False
```

## Practice

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Saidsp19/cognitive-vidya/blob/main/notebooks/python-course/04-function./scope-closures.ipynb)

**Next:** [Functional Programming](./functional-programming)
