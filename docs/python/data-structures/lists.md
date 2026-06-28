---
sidebar_position: 1
---

# Lists

**Module 3 · Lesson 1** | Difficulty: Beginner

## What Is a List?

A **list** is an ordered, mutable collection of items:

```python
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]
empty = []
```

Lists can hold any type and are **mutable** — you can change them after creation.

## Accessing Elements

```python
fruits = ["apple", "banana", "cherry"]
fruits[0]    # "apple"  (first)
fruits[-1]   # "cherry" (last)
fruits[1:3]  # ["banana", "cherry"]  (slicing)
```

### Slicing

```python
nums = [0, 1, 2, 3, 4, 5]
nums[1:4]    # [1, 2, 3]
nums[:3]     # [0, 1, 2]   from start
nums[3:]     # [3, 4, 5]   to end
nums[::2]    # [0, 2, 4]   every 2nd
nums[::-1]   # reversed
```

## Modifying Lists

```python
lst = [1, 2, 3]
lst.append(4)        # [1, 2, 3, 4]
lst.insert(0, 0)     # [0, 1, 2, 3, 4]
lst.extend([5, 6])   # [0, 1, 2, 3, 4, 5, 6]
lst.remove(0)        # removes first 0
popped = lst.pop()   # removes and returns last
lst[0] = 99          # [99, 1, 2, 3, 4, 5]
```

## Useful Methods

```python
nums = [3, 1, 4, 1, 5]
len(nums)           # 5
nums.count(1)       # 2
nums.index(4)       # 2
nums.sort()         # in-place sort → [1, 1, 3, 4, 5]
sorted(nums)        # returns new sorted list
nums.reverse()      # in-place reverse
```

## List Operations

```python
[1, 2] + [3, 4]    # [1, 2, 3, 4]
[1, 2] * 3         # [1, 2, 1, 2, 1, 2]
3 in [1, 2, 3]     # True
```

## Iterating

```python
for item in fruits:
    print(item)

for i, item in enumerate(fruits):
    print(i, item)
```

## Shallow Copy vs Reference

```python
a = [1, 2, 3]
b = a           # same object — changes affect both
c = a.copy()    # independent copy
c = a[:]        # also a copy
```

## Practice

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Saidsp19/cognitive-vidya/blob/main/notebooks/python-course/03-data-structures/09-lists.ipynb)

**Next:** [Tuples & Sets](./tuples-sets)
