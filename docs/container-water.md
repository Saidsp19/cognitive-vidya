---
sidebar_position: 2
---

# Container With Most Water

**Difficulty:** Medium | **Pattern:** Two Pointers

## Problem Statement

Given `n` non-negative integers representing heights of vertical lines, find two lines that together with the x-axis form a container that holds the most water.

**Example:**
```
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
```

## Understanding the Pattern

Start with widest container (left=0, right=n-1). Move the pointer at the **shorter** line inward:

```python
def max_area(height):
    left, right = 0, len(height) - 1
    best = 0
    while left < right:
        h = min(height[left], height[right])
        best = max(best, h * (right - left))
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return best
```

**Key Insight:** Greedy two-pointer — always try to improve by moving the shorter side.

## Practice

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Saidsp19/cognitive-vidya/blob/main/notebooks/05-two-pointers/container-water.ipynb)

<LessonProgress lessonId="container-water" />
