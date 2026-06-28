---
sidebar_position: 6
---

# Binary Search

**Difficulty:** Easy | **Pattern:** Divide & Conquer

## Problem Statement

Given a sorted array `nums` and a target value `target`, return the index if the target is found. If not, return `-1`.

**Example:**
```
Input: nums = [-1, 0, 3, 5, 9, 12], target = 9
Output: 4
```

## Understanding the Pattern

**Binary Search** is the foundational **Divide & Conquer** algorithm — repeatedly split the search space in half.

### Why It Works

The array is **sorted**, so we can eliminate half the search space with each comparison:
- If `nums[mid] < target`, the target must be in the right half
- If `nums[mid] > target`, the target must be in the left half
- If `nums[mid] == target`, we found it

### Algorithm

```python
left, right = 0, len(nums) - 1

while left <= right:
    mid = (left + right) // 2
    
    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        left = mid + 1
    else:
        right = mid - 1

return -1
```

**Time Complexity:** O(log N) — search space halves each iteration  
**Space Complexity:** O(1) — only using pointers

### Visualization

For `nums = [1, 3, 5, 7, 9]`, `target = 7`:
```
Step 1: [1, 3, 5, 7, 9]  mid=5  → search right
Step 2:       [7, 9]     mid=7  → found!
```

## Practice

Launch the interactive workspace to implement your solution.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Saidsp19/cognitive-vidya/blob/main/notebooks/04-binary-search/binary-search.ipynb)

<LessonProgress lessonId="binary-search" />
