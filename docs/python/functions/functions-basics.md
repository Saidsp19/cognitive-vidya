---
sidebar_position: 1
---

# Functions Basics

**Module 4 · Lesson 1** | Difficulty: Intermediate

## Defining Functions

Functions bundle reusable logic:

```python
def greet(name):
  """Return a greeting string."""  # docstring
  return f"Hello, {name}!"

print(greet("Alice"))  # Hello, Alice!
```

## Parameters & Arguments

```python
def power(base, exponent=2):  # exponent has default value 2
    return base ** exponent

power(3)       # 9
power(3, 3)    # 27
power(base=2, exponent=10)  # keyword arguments
```

### `*args` and `**kwargs`

```python
def sum_all(*args):
    return sum(args)

sum_all(1, 2, 3, 4)  # 10

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Bob", age=25)
```

## Return Values

```python
def min_max(nums):
    return min(nums), max(nums)  # returns a tuple

lo, hi = min_max([3, 1, 4, 1, 5])
```

Functions without `return` implicitly return `None`.

## Docstrings

```python
def area(radius):
    """
    Calculate circle area.

    Args:
        radius (float): Circle radius

    Returns:
        float: Area of the circle
    """
    return 3.14159 * radius ** 2

help(area)
```

## Scope Preview

```python
x = 10  # global

def foo():
    x = 5  # local — shadows global
    print(x)

foo()    # 5
print(x) # 10
```

See [Scope & Closures](./scope-closures) for details.

## Practice

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Saidsp19/cognitive-vidya/blob/main/notebooks/python-course/04-functions/13-functions-basics.ipynb)

**Next:** [Scope & Closures](./scope-closures)
