---
sidebar_position: 3
---

# Longest Substring Without Repeating Characters

**Difficulty:** Medium | **Pattern:** Variable Sliding Window

## Problem Statement

Given a string `s`, find the length of the longest substring without repeating characters.

**Example:**
```
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with length 3
```

## Understanding the Pattern

This is a **variable-size sliding window** problem — the window expands and contracts based on constraints.

### Key Insight

We maintain a window `[left, right]` that contains no duplicate characters:
- **Expand:** Move `right` pointer to include new characters
- **Contract:** When a duplicate is found, move `left` pointer until the duplicate is removed

### Algorithm

```python
char_set = set()
left = 0
max_length = 0

for right in range(len(s)):
    while s[right] in char_set:
        char_set.remove(s[left])
        left += 1
    char_set.add(s[right])
    max_length = max(max_length, right - left + 1)
```

**Time Complexity:** O(N) — each character is visited at most twice (once by `right`, once by `left`)

## Practice

Launch the interactive workspace to implement your solution.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Saidsp19/cognitive-vidya/blob/main/notebooks/01-sliding-window/longest-substring.ipynb)

<LessonProgress lessonId="longest-substring" />
