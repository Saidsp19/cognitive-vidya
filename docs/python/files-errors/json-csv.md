---
sidebar_position: 3
---

# JSON & Structured Data

**Module 6 · Lesson 3** | Difficulty: Intermediate

## JSON — JavaScript Object Notation

The standard format for APIs and config files. Maps closely to Python dicts/lists:

```python
import json

data = {"name": "Alice", "age": 30, "skills": ["Python", "SQL"]}

# Python → JSON string
json_str = json.dumps(data, indent=2)

# JSON string → Python
parsed = json.loads(json_str)

# Write to file
with open("user.json", "w") as f:
    json.dump(data, f, indent=2)

# Read from file
with open("user.json", "r") as f:
    loaded = json.load(f)
```

## Handling Non-Serializable Types

```python
from datetime import datetime

def default_serializer(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()
    raise TypeError(f"Type {type(obj)} not serializable")

json.dumps({"created": datetime.now()}, default=default_serializer)
```

## Practical Example: Config File

```python
# config.json
# {"debug": true, "port": 8080, "hosts": ["localhost"]}

import json
from pathlib import Path

config = json.loads(Path("config.json").read_text())
if config["debug"]:
    print(f"Starting on port {config['port']}")
```

## CSV vs JSON

| Format | Best For |
|--------|----------|
| **CSV** | Tabular data, spreadsheets |
| **JSON** | Nested structures, APIs, configs |

## Practice

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Saidsp19/cognitive-vidya/blob/main/notebooks/python-course/06-files-error./json-csv.ipynb)

**Next:** [Comprehensions](../intermediate/comprehensions) — Module 7
