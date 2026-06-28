---
sidebar_position: 2
---

# File I/O

**Module 6 · Lesson 2** | Difficulty: Intermediate

## Reading Files

Always use `with` to ensure files are closed:

```python
with open("data.txt", "r") as f:
    content = f.read()        # entire file as string

with open("data.txt", "r") as f:
    lines = f.readlines()       # list of lines

with open("data.txt", "r") as f:
    for line in f:            # memory-efficient for large files
        print(line.strip())
```

## Writing Files

```python
with open("output.txt", "w") as f:   # overwrites
    f.write("Hello\n")
    f.writelines(["Line 1\n", "Line 2\n"])

with open("output.txt", "a") as f:   # append
    f.write("New line\n")
```

## File Modes

| Mode | Meaning |
|------|---------|
| `r` | Read (default) |
| `w` | Write (truncate) |
| `a` | Append |
| `r+` | Read and write |
| `b` | Binary (`rb`, `wb`) |

## Path Handling with `pathlib`

```python
from pathlib import Path

p = Path("data") / "users" / "alice.txt"
p.exists()
p.read_text()
p.write_text("Hello!")
list(p.parent.glob("*.txt"))
```

## Working with CSV

```python
import csv

with open("data.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["name"], row["age"])

with open("out.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "age"])
    writer.writerow(["Alice", 30])
```

## Practice

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Saidsp19/cognitive-vidya/blob/main/notebooks/python-course/06-files-error./file-io.ipynb)

**Next:** [JSON & CSV](./json-csv)
