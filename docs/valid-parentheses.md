---
sidebar_position: 5
---

# Valid Parentheses

**Difficulty:** Easy | **Pattern:** Stack

## Problem Statement

Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

**Example:**
```
Input: s = "({[]})"
Output: True

Input: s = "([)]"
Output: False
```

## Understanding the Pattern

The **Stack** pattern is ideal for tracking **nested structures** where the most recent item matters.

### Why Stack?

When we encounter a closing bracket, we need to verify it matches the **most recent unmatched opening bracket** — this is exactly what a stack provides (LIFO: Last In, First Out).

### Algorithm

```python
stack = []
pairs = {')': '(', ']': '[', '}': '{'}

for char in s:
    if char in pairs:  # Closing bracket
        if not stack or stack.pop() != pairs[char]:
            return False
    else:  # Opening bracket
        stack.append(char)

return len(stack) == 0
```

**Time Complexity:** O(N) — single pass through the string  
**Space Complexity:** O(N) — worst case, all opening brackets

## Practice

Launch the interactive workspace to implement your solution.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Saidsp19/cognitive-vidya/blob/main/notebooks/03-stack/valid-parentheses.ipynb)

<LessonProgress lessonId="valid-parentheses" />
