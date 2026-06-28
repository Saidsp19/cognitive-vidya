---
sidebar_position: 1
---

# Reverse Linked List

**Difficulty:** Easy | **Pattern:** Linked List

## Problem Statement

Given the head of a singly linked list, reverse the list and return the reversed head.

**Example:**
```
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
```

## Understanding the Pattern

**Iterative** — three pointers: `prev`, `curr`, `next`:

```python
def reverse_list(head):
    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev
```

**Key Insight:** Reverse links one node at a time — O(N) time, O(1) space.

## Practice

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Saidsp19/cognitive-vidya/blob/main/notebooks/09-linked-list/reverse-linked-list.ipynb)

<LessonProgress lessonId="reverse-linked-list" />
