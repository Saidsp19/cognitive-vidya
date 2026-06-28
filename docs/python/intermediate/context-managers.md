---
sidebar_position: 4
---

# Context Managers

**Module 7 · Lesson 4** | Difficulty: Advanced

## The `with` Statement

Context managers guarantee setup and teardown — even if an error occurs:

```python
with open("file.txt") as f:
    data = f.read()
# file automatically closed here
```

Equivalent to:

```python
f = open("file.txt")
try:
    data = f.read()
finally:
    f.close()
```

## Creating Context Managers

### Class-based

```python
from contextlib import contextmanager

class Timer:
    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        elapsed = time.perf_counter() - self.start
        print(f"Elapsed: {elapsed:.4f}s")
        return False  # don't suppress exceptions
```

### Function-based with `@contextmanager`

```python
from contextlib import contextmanager

@contextmanager
def temporary_value(obj, attr, value):
    old = getattr(obj, attr)
    setattr(obj, attr, value)
    try:
        yield
    finally:
        setattr(obj, attr, old)
```

## `contextlib` Utilities

```python
from contextlib import suppress, redirect_stdout
import io

# Suppress specific exceptions
with suppress(FileNotFoundError):
    os.remove("maybe_missing.txt")

# Redirect stdout
buf = io.StringIO()
with redirect_stdout(buf):
    print("captured")
print(buf.getvalue())  # "captured\n"
```

## Practice

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Saidsp19/cognitive-vidya/blob/main/notebooks/python-course/07-intermediat./context-managers.ipynb)

**Next:** [Modules & Packages](../advanced/modules-packages) — Module 8
