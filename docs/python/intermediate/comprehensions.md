---
sidebar_position: 1
---

# List & Dict Comprehensions

**Module 7 · Lesson 1** | Difficulty: Intermediate

## List Comprehensions

Concise way to build lists:

```python
# Traditional
squares = []
for x in range(10):
    squares.append(x ** 2)

# Comprehension
squares = [x ** 2 for x in range(10)]
```

### With Condition

```python
evens = [x for x in range(20) if x % 2 == 0]
```

### Nested

```python
matrix = [[i * j for j in range(3)] for i in range(3)]
# [[0,0,0], [0,1,2], [0,2,4]]
```

## Dict Comprehensions

```python
word_lengths = {word: len(word) for word in ["hi", "hello", "hey"]}
# {'hi': 2, 'hello': 5, 'hey': 3}

inverted = {v: k for k, v in {"a": 1, "b": 2}.items()}
```

## Set Comprehensions

```python
unique_lengths = {len(w) for w in ["hi", "hello", "hey", "hi"]}
# {2, 5, 3}
```

## Generator Expressions

Like list comprehensions but lazy (memory-efficient):

```python
gen = (x ** 2 for x in range(1000000))  # no list created yet
sum(gen)  # consumes values one at a time
```

## When NOT to Use Comprehensions

Avoid when logic is complex — use a regular loop for readability:

```python
# Too complex — use a loop instead
result = [process(x) for x in data if validate(x) and transform(x) > 0]
```

## Practice

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Saidsp19/cognitive-vidya/blob/main/notebooks/python-course/07-intermediate/22-comprehensions.ipynb)

**Next:** [Generators](./generators)
