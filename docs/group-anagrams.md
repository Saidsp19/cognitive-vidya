---
sidebar_position: 6
---

# Group Anagrams

**Difficulty:** Medium | **Pattern:** HashMap

## Problem Statement

Given an array of strings `strs`, group the anagrams together.

**Example:**
```
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
```

## Understanding the Pattern

Anagrams share the same **character frequency**. Use a sorted tuple or char-count tuple as a HashMap key:

```python
from collections import defaultdict

def group_anagrams(strs):
    groups = defaultdict(list)
    for s in strs:
        key = tuple(sorted(s))
        groups[key].append(s)
    return list(groups.values())
```

**Key Insight:** Normalize each string to a canonical form, then bucket by that key.

## Practice

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Saidsp19/cognitive-vidya/blob/main/notebooks/02-hashmap/group-anagrams.ipynb)

<LessonProgress lessonId="group-anagrams" />
