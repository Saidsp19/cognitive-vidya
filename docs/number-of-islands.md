---
sidebar_position: 2
---

# Number of Islands

**Difficulty:** Medium | **Pattern:** BFS/DFS

## Problem Statement

Given an `m x n` grid of `'1'` (land) and `'0'` (water), return the number of islands.

**Example:**
```
Input: grid = [
  ["1","1","0"],
  ["0","1","0"],
  ["0","0","1"]
]
Output: 3
```

## Understanding the Pattern

For each unvisited `'1'`, run **DFS/BFS** to mark the entire island as visited:

```python
def num_islands(grid):
    count = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == '1':
                dfs(grid, r, c)
                count += 1
    return count

def dfs(grid, r, c):
    if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]):
        return
    if grid[r][c] != '1':
        return
    grid[r][c] = '0'
    dfs(grid, r+1, c); dfs(grid, r-1, c)
    dfs(grid, r, c+1); dfs(grid, r, c-1)
```

**Key Insight:** Graph traversal on implicit grids — flood-fill each connected component.

## Practice

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Saidsp19/cognitive-vidya/blob/main/notebooks/07-bfs-dfs/number-of-islands.ipynb)

<LessonProgress lessonId="number-of-islands" />
