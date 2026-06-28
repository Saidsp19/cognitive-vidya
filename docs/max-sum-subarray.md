---
sidebar_position: 2
---

# Maximum Sum Subarray of Size K

**Difficulty:** Easy | **Pattern:** Sliding Window

## Problem Statement

Given an array `nums` and integer `k`, find the maximum sum of any contiguous subarray of size `k`.

**Example:**
```
Input: nums = [2, 1, 5, 1, 3, 2], k = 3
Output: 9
Explanation: Subarray [5, 1, 3] has maximum sum = 9
```

## Understanding the Pattern

The **Sliding Window** pattern helps us avoid redundant calculations when processing contiguous subarrays.

### Brute Force Approach (O(N·K))
```python
for i in range(len(nums) - k + 1):
    window_sum = sum(nums[i:i+k])  # Recalculating sum each time
    max_sum = max(max_sum, window_sum)
```

This recalculates the entire window sum from scratch for each position.

### Optimal Approach (O(N))

Instead of recalculating, **slide the window**:
1. Start with the sum of the first `k` elements
2. For each new position, add the new element and subtract the element that left the window

```python
window_sum = sum(nums[:k])
max_sum = window_sum

for i in range(k, len(nums)):
    window_sum += nums[i] - nums[i - k]  # Slide the window
    max_sum = max(max_sum, window_sum)
```

**Key Insight:** Each element is visited exactly once → O(N) time complexity.

## Practice

Ready to implement it? Launch the interactive workspace below.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Saidsp19/cognitive-vidya/blob/main/notebooks/01-sliding-window/max-sum-subarray.ipynb)

The notebook includes:
- Pre-written test cases
- Auto-grader to validate your solution
- Hints if you get stuck
