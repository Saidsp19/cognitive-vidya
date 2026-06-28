---
sidebar_position: 4
---

# Operators & Expressions

**Module 1 · Lesson 4** | Difficulty: Beginner

## Expressions vs Statements

- **Expression:** Produces a value — `2 + 3`, `len("hi")`, `x > 5`
- **Statement:** Performs an action — `x = 5`, `print(x)`, `if x > 0:`

## Comparison Operators

Return `True` or `False`:

```python
5 == 5    # True   equal
5 != 3    # True   not equal
5 > 3     # True   greater than
5 < 3     # False  less than
5 >= 5    # True   greater or equal
5 <= 4    # False  less or equal
```

:::caution
Use `==` for equality, not `=`. `=` is assignment.
:::

## Logical Operators

Combine boolean expressions:

```python
True and False   # False
True or False    # True
not True         # False

age = 20
age >= 18 and age < 65   # True (working age example)
```

### Short-Circuit Evaluation

```python
False and expensive_call()  # expensive_call() never runs
True or expensive_call()    # expensive_call() never runs
```

## Membership Operators

```python
"a" in "abc"       # True
5 in [1, 2, 3]     # False
"x" not in "abc"   # True
```

## Identity Operators

Check if two variables refer to the **same object** in memory:

```python
a = [1, 2]
b = [1, 2]
a == b    # True  (same values)
a is b    # False (different objects)

c = a
a is c    # True  (same object)
```

## Operator Precedence

Highest to lowest (simplified):

1. `**` (exponent)
2. `*`, `/`, `//`, `%`
3. `+`, `-`
4. `==`, `!=`, `<`, `>`, `<=`, `>=`
5. `not`
6. `and`
7. `or`

Use parentheses to clarify:

```python
2 + 3 * 4      # 14, not 20
(2 + 3) * 4    # 20
```

## String Operations

```python
"Hello" + " " + "World"   # concatenation
"ha" * 3                  # "hahaha"
len("Python")             # 6
```

## F-Strings (Formatted Strings)

The modern way to embed values in strings:

```python
name = "Alice"
age = 30
print(f"{name} is {age} years old")
# Alice is 30 years old

print(f"Next year: {age + 1}")
print(f"Pi to 2 decimals: {3.14159:.2f}")  # 3.14
```

## Truthiness

Every value has a boolean context in `if` statements:

| Falsy | Truthy |
|-------|--------|
| `0`, `0.0` | Any non-zero number |
| `""` | Any non-empty string |
| `[]`, `{}`, `()` | Any non-empty collection |
| `None` | Most other values |

```python
if name:          # runs if name is non-empty
    print(f"Hello, {name}")
```

## Practice

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Saidsp19/cognitive-vidya/blob/main/notebooks/python-course/01-fundamental./operators.ipynb)

**Next:** [Input & Output](./input-output)
