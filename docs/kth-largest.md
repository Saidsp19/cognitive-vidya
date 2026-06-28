---
sidebar_position: 1
---

# Kth Largest Element in an Array

**Difficulty:** Medium | **Pattern:** Heap

## Problem Statement

Given an integer array `nums` and integer `k`, return the **kth largest** element in the array.

**Example:**
```
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
```

## Understanding the Pattern

Use a **min-heap** of size k — the root is the kth largest:

```python
import heapq

def find_kth_largest(nums, k):
    heap = nums[:k]
    heapq.heapify(heap)
    for n in nums[k:]:
        if n > heap[0]:
            heapq.heapreplace(heap, n)
    return heap[0]
```

**Alternative:** Quickselect for O(N) average time.

**Key Insight:** Heaps maintain top-k elements efficiently.

## Practice

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Saidsp19/cognitive-vidya/blob/main/notebooks/08-heap/kth-largest.ipynb)

<LessonProgress lessonId="kth-largest" />
