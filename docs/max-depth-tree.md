---
sidebar_position: 1
---

# Maximum Depth of Binary Tree

**Difficulty:** Easy | **Pattern:** BFS/DFS

## Problem Statement

Given the root of a binary tree, return its maximum depth (number of nodes along the longest path from root to leaf).

**Example:**
```
Input: root = [3,9,20,null,null,15,7]
Output: 3
```

## Understanding the Pattern

**Recursive DFS:**
```python
def max_depth(root):
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))
```

**BFS alternative:** Count levels while traversing level-by-level with a queue.

**Key Insight:** Tree problems often decompose into left and right subproblems.

## Practice

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Saidsp19/cognitive-vidya/blob/main/notebooks/07-bfs-dfs/max-depth-tree.ipynb)

<LessonProgress lessonId="max-depth-tree" />
