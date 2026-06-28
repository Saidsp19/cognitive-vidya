---
sidebar_position: 4
---

# Two Sum

**Difficulty:** Easy | **Pattern:** HashMap

## Problem Statement

Given an array of integers `nums` and an integer `target`, return indices of the two numbers that add up to `target`.

**Example:**
```
Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
Explanation: nums[0] + nums[1] = 2 + 7 = 9
```

## Understanding the Pattern

The **HashMap** pattern allows us to trade space for time — storing previously seen values for O(1) lookups.

### Brute Force (O(N²))
```python
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            return [i, j]
```

This checks every pair, resulting in quadratic time complexity.

### Optimal Approach (O(N))

For each number, check if its **complement** `(target - nums[i])` has been seen before:

```python
seen = {}  # {value: index}

for i, num in enumerate(nums):
    complement = target - num
    if complement in seen:
        return [seen[complement], i]
    seen[num] = i
```

**Key Insight:** Instead of searching for pairs, search for complements using a HashMap.

## Practice

Launch the interactive workspace to implement your solution.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Saidsp19/cognitive-vidya/blob/main/notebooks/02-hashmap/two-sum.ipynb)

<VideoEmbed videoId="KLlXCFG5TnA" title="Two Sum — Hash Map Pattern Explained" />

<LessonProgress lessonId="two-sum" />
