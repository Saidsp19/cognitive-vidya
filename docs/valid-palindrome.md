---
sidebar_position: 1
---

# Valid Palindrome

**Difficulty:** Easy | **Pattern:** Two Pointers

## Problem Statement

Given a string `s`, return `true` if it is a palindrome after converting all uppercase letters to lowercase and removing non-alphanumeric characters.

**Example:**
```
Input: s = "A man, a plan, a canal: Panama"
Output: true
```

## Understanding the Pattern

Place **left** and **right** pointers at both ends, skip non-alphanumeric, compare inward:

```python
def is_palindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True
```

**Key Insight:** Two pointers converge from both ends — O(N) time, O(1) space.

## Practice

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Saidsp19/cognitive-vidya/blob/main/notebooks/05-two-pointers/valid-palindrome.ipynb)

<LessonProgress lessonId="valid-palindrome" />
