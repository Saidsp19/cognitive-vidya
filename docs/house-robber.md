---
sidebar_position: 2
---

# House Robber

**Difficulty:** Medium | **Pattern:** Dynamic Programming

## Problem Statement

Given an array `nums` representing money in each house, return the maximum amount you can rob without robbing two adjacent houses.

**Example:**
```
Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob houses 2 + 9 + 1 = 12
```

## Understanding the Pattern

At each house, choose **rob or skip**:

```python
def rob(nums):
    prev2, prev1 = 0, 0
    for n in nums:
        prev2, prev1 = prev1, max(prev1, prev2 + n)
    return prev1
```

`dp[i] = max(dp[i-1], dp[i-2] + nums[i])`

**Key Insight:** Track only last two states — space-optimized DP.

## Practice

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Saidsp19/cognitive-vidya/blob/main/notebooks/06-dynamic-programming/house-robber.ipynb)

<LessonProgress lessonId="house-robber" />
