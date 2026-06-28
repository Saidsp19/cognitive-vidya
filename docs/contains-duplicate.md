---
sidebar_position: 5
---

# Contains Duplicate

**Difficulty:** Easy | **Pattern:** HashMap

## Problem Statement

Given an integer array `nums`, return `true` if any value appears **at least twice**, and `false` if every element is distinct.

**Example:**
```
Input: nums = [1, 2, 3, 1]
Output: true

Input: nums = [1, 2, 3, 4]
Output: false
```

## Understanding the Pattern

Use a **set** (or HashMap) to track seen elements in O(N) time:

```python
def contains_duplicate(nums):
    seen = set()
    for n in nums:
        if n in seen:
            return True
        seen.add(n)
    return False
```

**Key Insight:** Sets give O(1) membership checks — trade memory for speed.

## Practice

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Saidsp19/cognitive-vidya/blob/main/notebooks/02-hashmap/contains-duplicate.ipynb)

<LessonProgress lessonId="contains-duplicate" />
