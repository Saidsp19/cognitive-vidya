---
sidebar_position: 1
---

# Exception Handling

**Module 6 · Lesson 1** | Difficulty: Intermediate

## Why Handle Errors?

Programs encounter unexpected situations — bad input, missing files, network failures. **Exceptions** let you recover gracefully instead of crashing.

## try / except / else / finally

```python
try:
    result = 10 / int(input("Enter divisor: "))
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Please enter a valid integer.")
else:
    print(f"Result: {result}")   # runs only if no exception
finally:
    print("Done.")               # always runs
```

## Catching Multiple Exceptions

```python
try:
    process(data)
except (TypeError, ValueError) as e:
    print(f"Invalid data: {e}")
```

## Raising Exceptions

```python
def withdraw(balance, amount):
    if amount > balance:
        raise ValueError("Insufficient funds")
    return balance - amount
```

## Custom Exceptions

```python
class ValidationError(Exception):
    def __init__(self, field, message):
        self.field = field
        super().__init__(f"{field}: {message}")

raise ValidationError("email", "invalid format")
```

## Common Built-in Exceptions

| Exception | When |
|-----------|------|
| `ValueError` | Wrong value type/content |
| `TypeError` | Wrong type for operation |
| `KeyError` | Missing dict key |
| `IndexError` | List index out of range |
| `FileNotFoundError` | File doesn't exist |
| `ZeroDivisionError` | Division by zero |

## EAFP vs LBYL

Python prefers **EAFP** (Easier to Ask Forgiveness than Permission):

```python
# EAFP (Pythonic)
try:
    value = d[key]
except KeyError:
    value = default

# LBYL (Look Before You Leap)
if key in d:
    value = d[key]
else:
    value = default
```

## Practice

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Saidsp19/cognitive-vidya/blob/main/notebooks/python-course/06-files-errors/19-exception-handling.ipynb)

**Next:** [File I/O](./file-io)
