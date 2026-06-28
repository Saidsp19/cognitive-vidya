---
sidebar_position: 3
---

# Variables & Data Types

**Module 1 · Lesson 3** | Difficulty: Beginner

## Variables

A **variable** is a name that refers to a value in memory.

```python
age = 25
name = "Alice"
pi = 3.14159
is_student = True
```

Python is **dynamically typed** — you don't declare types; Python infers them at runtime.

```python
x = 10      # x is an int
x = "hello" # now x is a str — perfectly valid
```

## Naming Rules

- Letters, digits, underscores (`_`); cannot start with a digit
- Case-sensitive: `age` ≠ `Age`
- Avoid Python keywords (`if`, `for`, `class`, etc.)
- Convention: `snake_case` for variables and functions

```python
user_name = "bob"      # good
total_count = 100      # good
2fast = 10             # SyntaxError
```

## Core Data Types

| Type | Example | Description |
|------|---------|-------------|
| `int` | `42`, `-7`, `0` | Whole numbers, arbitrary precision |
| `float` | `3.14`, `-0.5`, `2e10` | Decimal numbers |
| `str` | `"hello"`, `'world'` | Text (immutable) |
| `bool` | `True`, `False` | Logical values |
| `NoneType` | `None` | Absence of a value |

### Checking Types

```python
type(42)        # <class 'int'>
type(3.14)      # <class 'float'>
type("hi")      # <class 'str'>
isinstance(42, int)  # True
```

## Type Conversion (Casting)

```python
int("42")       # 42
float("3.14")   # 3.14
str(100)        # "100"
bool(0)         # False  (falsy)
bool(1)         # True   (truthy)
bool("")        # False
bool("hello")   # True
```

## Arithmetic Operators

```python
10 + 3   # 13  addition
10 - 3   # 7   subtraction
10 * 3   # 30  multiplication
10 / 3   # 3.333...  division (always float)
10 // 3  # 3   floor division
10 % 3   # 1   modulo (remainder)
2 ** 10  # 1024 exponentiation
```

## Assignment Operators

```python
x = 10
x += 5    # x = x + 5  → 15
x *= 2    # x = x * 2  → 30
```

## Multiple Assignment

```python
a, b, c = 1, 2, 3
x = y = z = 0   # all three are 0
```

## Constants (Convention)

Python has no true constants. By convention, `UPPER_SNAKE_CASE` signals "don't reassign":

```python
MAX_RETRIES = 3
PI = 3.14159
```

## Practice

Complete exercises on variables, types, and casting.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Saidsp19/cognitive-vidya/blob/main/notebooks/python-course/01-fundamental./variables-types.ipynb)

**Next:** [Operators & Expressions](./operators)
