---
sidebar_position: 1
---

# Climbing Stairs

**Difficulty:** Easy | **Pattern:** Dynamic Programming

## Problem Statement

You are climbing a staircase with `n` steps. Each time you can climb 1 or 2 steps. How many distinct ways can you climb to the top?

**Example:**
```
Input: n = 3
Output: 3
Explanation: 1+1+1, 1+2, 2+1
```

## Understanding the Pattern

This is **Fibonacci** in disguise: `ways(n) = ways(n-1) + ways(n-2)`

```python
def climb_stairs(n):
    if n <= 2:
        return n
    a, b = 1, 2
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b
```

**Key Insight:** Build solution from overlapping subproblems — classic 1D DP.

## Practice

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Saidsp19/cognitive-vidya/blob/main/notebooks/06-dynamic-programming/climbing-stairs.ipynb)

<LessonProgress lessonId="climbing-stairs" />
