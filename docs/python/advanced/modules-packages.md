---
sidebar_position: 1
---

# Modules & Packages

**Module 8 · Lesson 1** | Difficulty: Advanced

## Modules

A **module** is any `.py` file. Import it to reuse code:

```python
# math_utils.py
def add(a, b):
    return a + b

PI = 3.14159
```

```python
import math_utils
math_utils.add(2, 3)

from math_utils import add, PI
add(2, 3)

from math_utils import add as sum_two
```

## Standard Library Highlights

```python
import os
import sys
import json
import random
import datetime
from pathlib import Path
from collections import Counter, defaultdict
from itertools import chain, combinations
```

## Packages

A **package** is a directory with `__init__.py`:

```
myproject/
├── mypackage/
│   ├── __init__.py
│   ├── core.py
│   └── utils.py
└── main.py
```

```python
from mypackage.core import process
from mypackage import utils
```

## Virtual Environments

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install requests pandas
pip freeze > requirements.txt
pip install -r requirements.txt
deactivate
```

## `if __name__ == "__main__"`

```python
def main():
    print("Running as script")

if __name__ == "__main__":
    main()
```

Runs `main()` only when executed directly, not when imported.

## Practice

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Saidsp19/cognitive-vidya/blob/main/notebooks/python-course/08-advanced/26-modules-packages.ipynb)

**Next:** [Testing](./testing)
