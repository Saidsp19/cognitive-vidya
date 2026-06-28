---
sidebar_position: 2
---

# For Loops

**Module 2 · Lesson 2** | Difficulty: Beginner

## Iterating Over Sequences

A `for` loop repeats code for each item in a sequence:

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

## `range()` Function

Generate a sequence of numbers:

```python
for i in range(5):       # 0, 1, 2, 3, 4
    print(i)

for i in range(2, 6):    # 2, 3, 4, 5
    print(i)

for i in range(0, 10, 2):  # 0, 2, 4, 6, 8  (step=2)
    print(i)
```

## Looping with Index

```python
colors = ["red", "green", "blue"]
for i in range(len(colors)):
    print(f"{i}: {colors[i]}")

# Better — use enumerate()
for i, color in enumerate(colors):
    print(f"{i}: {color}")
```

## Iterating Over Strings

```python
for char in "Python":
    print(char)
# P y t h o n (each on its own line)
```

## Loop Control

```python
# break — exit loop immediately
for n in range(10):
    if n == 5:
        break
    print(n)  # 0 1 2 3 4

# continue — skip to next iteration
for n in range(5):
    if n == 2:
        continue
    print(n)  # 0 1 3 4
```

## Nested Loops

```python
for row in range(3):
    for col in range(3):
        print(f"({row},{col})", end=" ")
    print()
```

## Accumulator Pattern

```python
numbers = [1, 2, 3, 4, 5]
total = 0
for n in numbers:
    total += n
print(total)  # 15

# Or use built-in:
print(sum(numbers))
```

## Practice

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Saidsp19/cognitive-vidya/blob/main/notebooks/python-course/02-control-flo./for-loops.ipynb)

**Next:** [While Loops](./while-loops)
