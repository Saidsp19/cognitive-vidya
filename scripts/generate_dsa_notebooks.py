#!/usr/bin/env python3
"""Generate DSA pattern notebooks."""
import json
from pathlib import Path

ROOT = Path(__file__).parent.parent / "notebooks"

NOTEBOOKS = {
    "02-hashmap/contains-duplicate.ipynb": {
        "title": "Contains Duplicate",
        "pattern": "HashMap",
        "difficulty": "Easy",
        "desc": "Given an integer array `nums`, return `True` if any value appears at least twice.",
        "stub": "def contains_duplicate(nums: list[int]) -> bool:\n    pass",
        "func": "contains_duplicate",
        "tests": "[([1,2,3,1], True), ([1,2,3,4], False), ([1,1,1,3], True)]",
    },
    "02-hashmap/group-anagrams.ipynb": {
        "title": "Group Anagrams",
        "pattern": "HashMap",
        "difficulty": "Medium",
        "desc": "Group strings that are anagrams of each other.",
        "stub": "def group_anagrams(strs: list[str]) -> list[list[str]]:\n    pass",
        "func": "group_anagrams",
        "tests": """[
        (["eat","tea","tan","ate","nat","bat"],
         sorted([["bat"],["nat","tan"],["ate","eat","tea"]], key=sorted)),
    ]""",
        "custom_check": """
            result = group_anagrams(strs)
            norm = sorted([sorted(g) for g in result], key=lambda g: g[0] if g else "")
            if norm == expected:
                passed += 1; print(f"✅ Test {i+1} Passed")
            else:
                print(f"❌ Test {i+1} Failed. Got {result}")
        """,
    },
    "03-stack/daily-temperatures.ipynb": {
        "title": "Daily Temperatures",
        "pattern": "Stack",
        "difficulty": "Medium",
        "desc": "Return array where answer[i] is days until a warmer temperature.",
        "stub": "def daily_temperatures(temps: list[int]) -> list[int]:\n    pass",
        "func": "daily_temperatures",
        "tests": "[([73,74,75,71,69,72,76,73], [1,1,4,2,1,1,0,0]), ([30,40,50,60], [1,1,1,0])]",
    },
    "04-binary-search/search-insert-position.ipynb": {
        "title": "Search Insert Position",
        "pattern": "Binary Search",
        "difficulty": "Easy",
        "desc": "Find index of target in sorted array, or insert position if absent.",
        "stub": "def search_insert(nums: list[int], target: int) -> int:\n    pass",
        "func": "search_insert",
        "tests": "[([1,3,5,6], 5, 2), ([1,3,5,6], 2, 1), ([1,3,5,6], 7, 4)]",
    },
    "05-two-pointers/valid-palindrome.ipynb": {
        "title": "Valid Palindrome",
        "pattern": "Two Pointers",
        "difficulty": "Easy",
        "desc": "Return True if s is a palindrome (alphanumeric only, ignore case).",
        "stub": "def is_palindrome(s: str) -> bool:\n    pass",
        "func": "is_palindrome",
        "tests": '[("A man, a plan, a canal: Panama", True), ("race a car", False), (" ", True)]',
    },
    "05-two-pointers/container-water.ipynb": {
        "title": "Container With Most Water",
        "pattern": "Two Pointers",
        "difficulty": "Medium",
        "desc": "Find two lines that together with x-axis form a container holding most water.",
        "stub": "def max_area(height: list[int]) -> int:\n    pass",
        "func": "max_area",
        "tests": "[([1,8,6,2,5,4,8,3,7], 49), ([1,1], 1)]",
    },
    "06-dynamic-programming/climbing-stairs.ipynb": {
        "title": "Climbing Stairs",
        "pattern": "Dynamic Programming",
        "difficulty": "Easy",
        "desc": "Count distinct ways to climb n stairs taking 1 or 2 steps at a time.",
        "stub": "def climb_stairs(n: int) -> int:\n    pass",
        "func": "climb_stairs",
        "tests": "[(2, 2), (3, 3), (5, 8)]",
    },
    "06-dynamic-programming/house-robber.ipynb": {
        "title": "House Robber",
        "pattern": "Dynamic Programming",
        "difficulty": "Medium",
        "desc": "Max money robbing houses without robbing two adjacent houses.",
        "stub": "def rob(nums: list[int]) -> int:\n    pass",
        "func": "rob",
        "tests": "[([1,2,3,1], 4), ([2,7,9,3,1], 12), ([2,1,1,2], 4)]",
    },
    "07-bfs-dfs/max-depth-tree.ipynb": {
        "title": "Maximum Depth of Binary Tree",
        "pattern": "BFS/DFS",
        "difficulty": "Easy",
        "desc": "Return maximum depth of a binary tree.",
        "stub": """class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def max_depth(root) -> int:
    pass""",
        "func": "max_depth",
        "tests": "tree_tests",
        "custom_eval": """
    def make_tree(vals):
        if not vals: return None
        nodes = [TreeNode(v) if v is not None else None for v in vals]
        kids = nodes[::-1]
        root = kids.pop()
        for node in nodes:
            if node:
                if kids: node.left = kids.pop()
                if kids: node.right = kids.pop()
        return root

    cases = [([3,9,20,None,None,15,7], 3), ([1,None,2], 2), ([], 0)]
    for i, (vals, expected) in enumerate(cases):
        root = make_tree(vals) if vals else None
        try:
            result = max_depth(root)
            if result == expected:
                passed += 1; print(f"✅ Test {i+1} Passed")
            else:
                print(f"❌ Test {i+1} Failed. Expected {expected}, got {result}")
        except Exception as e:
            print(f"⚠️ Test {i+1} Error: {e}")
""",
    },
    "07-bfs-dfs/number-of-islands.ipynb": {
        "title": "Number of Islands",
        "pattern": "BFS/DFS",
        "difficulty": "Medium",
        "desc": "Count islands ('1') in a 2D grid surrounded by water ('0').",
        "stub": "def num_islands(grid: list[list[str]]) -> int:\n    pass",
        "func": "num_islands",
        "tests": """[
        ([["1","1","0"],["0","1","0"],["0","0","1"]], 3),
        ([["1","1","1"],["0","1","0"],["1","1","1"]], 1),
    ]""",
    },
    "08-heap/kth-largest.ipynb": {
        "title": "Kth Largest Element in Array",
        "pattern": "Heap",
        "difficulty": "Medium",
        "desc": "Find the kth largest element in an unsorted array.",
        "stub": "def find_kth_largest(nums: list[int], k: int) -> int:\n    pass",
        "func": "find_kth_largest",
        "tests": "[([3,2,1,5,6,4], 2, 5), ([3,2,3,1,2,4,5,5,6], 4, 4)]",
    },
    "09-linked-list/reverse-linked-list.ipynb": {
        "title": "Reverse Linked List",
        "pattern": "Linked List",
        "difficulty": "Easy",
        "desc": "Reverse a singly linked list.",
        "stub": """class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_list(head):
    pass""",
        "func": "reverse_list",
        "custom_eval": """
    def to_list(head):
        out = []
        while head:
            out.append(head.val)
            head = head.next
        return out

    def from_list(vals):
        dummy = ListNode(0)
        cur = dummy
        for v in vals:
            cur.next = ListNode(v)
            cur = cur.next
        return dummy.next

    cases = [([1,2,3,4,5], [5,4,3,2,1]), ([1,2], [2,1]), ([], [])]
    for i, (inp, expected) in enumerate(cases):
        head = from_list(inp) if inp else None
        try:
            result = to_list(reverse_list(head))
            if result == expected:
                passed += 1; print(f"✅ Test {i+1} Passed")
            else:
                print(f"❌ Test {i+1} Failed. Expected {expected}, got {result}")
        except Exception as e:
            print(f"⚠️ Test {i+1} Error: {e}")
""",
    },
}


def make_eval(meta):
    if meta.get("custom_eval"):
        return meta["custom_eval"]
    func = meta["func"]
    tests = meta["tests"]
    if tests.startswith("["):
        return f"""
    test_cases = {tests}
    for i, case in enumerate(test_cases):
        *args, expected = case
        try:
            result = {func}(*args) if len(args) > 1 else {func}(args[0])
            if result == expected:
                passed += 1
                print(f"✅ Test {{i+1}} Passed")
            else:
                print(f"❌ Test {{i+1}} Failed. Expected {{expected}}, got {{result}}")
        except Exception as e:
            print(f"⚠️ Test {{i+1}} Error: {{e}}")
"""
    return ""


def make_notebook(meta):
    eval_body = make_eval(meta)
    total = eval_body.count("passed += 1") or 1
    eval_code = f"""# --- EVALUATION ENGINE ---
def evaluate():
    passed = 0
    total = {max(total, 1)}
{eval_body}
    if passed == total:
        print("\\n🎉 ALL TESTS PASSED!")
    else:
        print(f"\\n📊 Score: {{passed}}/{{total}} tests passed")

evaluate()"""

    return {
        "cells": [
            {"cell_type": "markdown", "metadata": {}, "source": [
                f"# {meta['title']}\n",
                f"**Difficulty:** {meta['difficulty']} | **Pattern:** {meta['pattern']}\n\n",
                f"{meta['desc']}\n",
            ]},
            {"cell_type": "code", "execution_count": None, "metadata": {}, "outputs": [],
             "source": [l + "\n" for l in meta["stub"].split("\n")]},
            {"cell_type": "code", "execution_count": None, "metadata": {}, "outputs": [],
             "source": [l + "\n" for l in eval_code.strip().split("\n")]},
        ],
        "metadata": {"kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
                     "language_info": {"name": "python", "version": "3.10.0"}},
        "nbformat": 4, "nbformat_minor": 4,
    }


def main():
    for rel, meta in NOTEBOOKS.items():
        path = ROOT / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, "w") as f:
            json.dump(make_notebook(meta), f, indent=1)
        print(f"Created {rel}")


if __name__ == "__main__":
    main()
