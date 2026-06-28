---
sidebar_position: 6
---

# Daily Temperatures

**Difficulty:** Medium | **Pattern:** Stack

## Problem Statement

Given daily temperatures, return an array `answer` where `answer[i]` is the number of days you must wait after day `i` for a warmer temperature. If no future day is warmer, `answer[i] = 0`.

**Example:**
```
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
```

## Understanding the Pattern

Use a **monotonic decreasing stack** storing indices. When a warmer day arrives, pop indices and compute the difference:

```python
def daily_temperatures(temps):
    answer = [0] * len(temps)
    stack = []  # indices
    for i, t in enumerate(temps):
        while stack and temps[stack[-1]] < t:
            prev = stack.pop()
            answer[prev] = i - prev
        stack.append(i)
    return answer
```

**Key Insight:** Stack tracks "days waiting for a warmer day."

## Practice

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Saidsp19/cognitive-vidya/blob/main/notebooks/03-stack/daily-temperatures.ipynb)

<LessonProgress lessonId="daily-temperatures" />
