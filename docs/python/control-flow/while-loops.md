---
sidebar_position: 3
---

# While Loops

**Module 2 · Lesson 3** | Difficulty: Beginner

## Loop While Condition Is True

Unlike `for` loops (iterate over a sequence), `while` loops run until a condition becomes `False`:

```python
count = 0
while count < 5:
    print(count)
    count += 1
```

## When to Use `while` vs `for`

| Use `for` | Use `while` |
|-----------|---------------|
| Known number of iterations | Unknown iterations |
| Iterating a collection | Waiting for a condition |
| `range(n)` patterns | User input validation |
| | Game loops, polling |

## Infinite Loops (and How to Avoid Them)

```python
# Dangerous — never ends!
# while True:
#     print("forever")

# Controlled infinite loop with break
while True:
    command = input("Enter 'quit' to exit: ")
    if command == "quit":
        break
    print(f"You said: {command}")
```

## Common Patterns

### Input validation

```python
while True:
    age = input("Enter age (1-120): ")
    if age.isdigit() and 1 <= int(age) <= 120:
        age = int(age)
        break
    print("Invalid input. Try again.")
```

### Sentinel value

```python
total = 0
while True:
    value = int(input("Enter number (0 to stop): "))
    if value == 0:
        break
    total += value
print(f"Sum: {total}")
```

### Counter-controlled while

```python
n = 5
while n > 0:
    print(n)
    n -= 1
print("Blast off!")
```

## `else` on Loops

Runs when the loop completes **without** `break`:

```python
for n in range(2, 10):
    if n % 7 == 0:
        print("divisible by 7")
        break
else:
    print("no divisor found")  # runs if no break
```

## Practice

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Saidsp19/cognitive-vidya/blob/main/notebooks/python-course/02-control-flo./while-loops.ipynb)

**Next:** [Lists](../data-structures/lists) — Module 3
