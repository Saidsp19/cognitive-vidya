---
sidebar_position: 1
---

# Conditionals (if / elif / else)

**Module 2 · Lesson 1** | Difficulty: Beginner

## Making Decisions

Programs need to branch based on conditions. Python uses `if`, `elif`, and `else`:

```python
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"

print(grade)  # B
```

## Syntax Rules

```python
if condition:
    # indented block — runs if condition is True
elif other_condition:
    # runs if first was False and this is True
else:
    # runs if all above were False
```

- Colon `:` after every condition
- **4-space indent** for each block
- `elif` is short for "else if"

## Nested Conditionals

```python
age = 20
has_ticket = True

if age >= 18:
    if has_ticket:
        print("Welcome to the concert!")
    else:
        print("You need a ticket.")
else:
    print("Must be 18 or older.")
```

Prefer flat logic when possible:

```python
if age >= 18 and has_ticket:
    print("Welcome to the concert!")
elif age >= 18:
    print("You need a ticket.")
else:
    print("Must be 18 or older.")
```

## Ternary Expression

One-line conditional:

```python
status = "adult" if age >= 18 else "minor"
```

## Common Patterns

### Range checks

```python
if 0 <= x <= 100:   # Python allows chained comparisons
    print("Valid percentage")
```

### Membership

```python
if letter in "aeiou":
    print("Vowel")
```

### Guard clauses

```python
def process(data):
    if not data:
        return None
    if len(data) == 0:
        return []
    # main logic here
```

## Practice

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Saidsp19/cognitive-vidya/blob/main/notebooks/python-course/02-control-flow/06-conditionals.ipynb)

**Next:** [For Loops](./for-loops)
