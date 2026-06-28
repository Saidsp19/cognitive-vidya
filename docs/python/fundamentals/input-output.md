---
sidebar_position: 5
---

# Input & Output

**Module 1 · Lesson 5** | Difficulty: Beginner

## Output with `print()`

```python
print("Hello")                    # Hello
print("A", "B", "C")              # A B C  (space-separated)
print("A", "B", sep="-")          # A-B
print("no newline", end=" ")
print("continues")                # no newline continues
```

### Formatting Options

```python
name, score = "Bob", 95.5

# f-string (preferred)
print(f"{name} scored {score:.1f}%")

# .format() method
print("{} scored {:.1f}%".format(name, score))

# % formatting (legacy)
print("%s scored %.1f%%" % (name, score))
```

## Input with `input()`

`input()` always returns a **string**:

```python
name = input("Enter your name: ")
print(f"Hello, {name}!")

age = input("Enter your age: ")
age = int(age)   # convert to int for math
print(f"Next year you'll be {age + 1}")
```

### Safe Conversion Pattern

```python
while True:
    raw = input("Enter a number: ")
    try:
        number = int(raw)
        break
    except ValueError:
        print("That's not a valid integer. Try again.")
```

(We'll cover `try/except` fully in [Exception Handling](../files-errors/exception-handling).)

## Building a Simple Program

```python
print("=== Temperature Converter ===")
celsius = float(input("Enter °C: "))
fahrenheit = celsius * 9/5 + 32
print(f"{celsius}°C = {fahrenheit:.1f}°F")
```

## String Methods for I/O

```python
text = "  Hello, World!  "
text.strip()        # "Hello, World!"  remove whitespace
text.lower()        # "  hello, world!  "
text.upper()        # "  HELLO, WORLD!  "
text.replace("World", "Python")  # "  Hello, Python!  "
text.split(", ")    # ["  Hello", "World!  "]
```

## Reading Multi-Line Input

```python
lines = []
print("Enter lines (empty line to finish):")
while True:
    line = input()
    if line == "":
        break
    lines.append(line)
print(f"You entered {len(lines)} lines.")
```

## Practice

Build interactive programs with graded exercises.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Saidsp19/cognitive-vidya/blob/main/notebooks/python-course/01-fundamental./input-output.ipynb)

**Next:** [Conditionals](../control-flow/conditionals) — Module 2
