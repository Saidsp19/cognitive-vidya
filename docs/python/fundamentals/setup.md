---
sidebar_position: 2
---

# Setting Up Python

**Module 1 · Lesson 2** | Difficulty: Beginner

## Installation Options

| Option | Best For |
|--------|----------|
| **Google Colab** | Zero setup — use our course notebooks directly |
| **python.org** | Local development on your machine |
| **VS Code + Python extension** | Full IDE experience |

For this course, **Google Colab** is recommended. Every lesson links to a ready-to-run notebook.

### Local Installation (Optional)

1. Download Python 3.10+ from [python.org/downloads](https://www.python.org/downloads/)
2. Verify installation:

```bash
python3 --version
# Python 3.12.x
```

3. Run code in the terminal:

```bash
python3
>>> print("Hello!")
Hello!
>>> exit()
```

Or save to a file `hello.py` and run `python3 hello.py`.

## The Python REPL

**REPL** = Read-Eval-Print Loop. An interactive shell for experimenting:

```python
>>> 2 + 2
4
>>> name = "Alice"
>>> print(f"Hello, {name}!")
Hello, Alice!
```

Press `Ctrl+D` (macOS/Linux) or `Ctrl+Z` then Enter (Windows) to exit.

## Running Scripts

A **script** is a `.py` file with multiple statements:

```python
# greet.py
name = input("What is your name? ")
print(f"Nice to meet you, {name}!")
```

```bash
python3 greet.py
What is your name? Bob
Nice to meet you, Bob!
```

## Google Colab Workflow

1. Click **Open In Colab** on any lesson page
2. Sign in with your Google account
3. Click **Runtime → Run all** (or run cells one by one with Shift+Enter)
4. Edit code in exercise cells and re-run the grader

## Virtual Environments (Preview)

For local projects, isolate dependencies with `venv`:

```bash
python3 -m venv myproject
source myproject/bin/activate   # macOS/Linux
# myproject\Scripts\activate    # Windows
pip install requests
```

We'll cover this in depth in [Modules & Packages](../advanced/modules-packages).

## Practice

Verify your setup and run your first graded exercises.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Saidsp19/cognitive-vidya/blob/main/notebooks/python-course/01-fundamental./setup.ipynb)

**Next:** [Variables & Types](./variables-types)
