---
sidebar_position: 4
---

# Strings Deep Dive

**Module 3 · Lesson 4** | Difficulty: Beginner

## Strings Are Immutable Sequences

```python
s = "Hello, World!"
s[0]       # 'H'
s[-1]      # '!'
s[0:5]     # 'Hello'
len(s)     # 13
```

You cannot change a character in place: `s[0] = 'h'` raises `TypeError`.

## Essential Methods

```python
text = "  Hello, Python!  "

text.strip()              # "Hello, Python!"
text.lower()              # "  hello, python!  "
text.upper()              # "  HELLO, PYTHON!  "
text.replace("Python", "World")
text.split(", ")          # ['  Hello', 'Python!  ']
", ".join(["a", "b"])     # "a, b"
text.startswith("  He")   # True
text.find("Python")       # 9  (-1 if not found)
text.isdigit()            # False
```

## String Formatting

```python
name, score = "Alice", 95.567

# f-strings (Python 3.6+) — preferred
f"{name}: {score:.1f}%"
f"{'left':>10}"           # right-align in 10 chars
f"{1000000:,}"            # 1,000,000

# Format specifiers
f"{3.14159:.2f}"          # 3.14
f"{255:#x}"               # 0xff
```

## Raw Strings

Backslashes are literal — useful for regex and file paths:

```python
path = r"C:\Users\name\file.txt"
pattern = r"\d+\.\d+"
```

## Multi-line Strings

```python
poem = """
Roses are red,
Violets are blue,
Python is awesome,
And so are you.
"""
```

## Character Operations

```python
"abc".isalpha()     # True
"123".isdigit()     # True
"Hello".isupper()   # False
ord('A')            # 65
chr(65)             # 'A'
```

## Practice

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Saidsp19/cognitive-vidya/blob/main/notebooks/python-course/03-data-structure./strings.ipynb)

**Next:** [Functions Basics](../functions/functions-basics) — Module 4
