---
sidebar_position: 7
---

# Search Insert Position

**Difficulty:** Easy | **Pattern:** Binary Search

## Problem Statement

Given a sorted array and a target, return the index if found. Otherwise return the index where it would be inserted in order.

**Example:**
```
Input: nums = [1,3,5,6], target = 5
Output: 2

Input: nums = [1,3,5,6], target = 2
Output: 1
```

## Understanding the Pattern

Classic binary search — when the loop ends, `left` points to the insert position:

```python
def search_insert(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left
```

## Practice

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Saidsp19/cognitive-vidya/blob/main/notebooks/04-binary-search/search-insert-position.ipynb)

<LessonProgress lessonId="search-insert-position" />
