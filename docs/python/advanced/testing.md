---
sidebar_position: 2
---

# Testing with pytest

**Module 8 · Lesson 2** | Difficulty: Advanced

## Why Test?

Tests catch bugs early, document behavior, and enable safe refactoring.

## Writing Testable Code

```python
def is_palindrome(s: str) -> bool:
    cleaned = "".join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]
```

## `unittest` (Built-in)

```python
import unittest

class TestPalindrome(unittest.TestCase):
    def test_simple(self):
        self.assertTrue(is_palindrome("racecar"))

    def test_with_spaces(self):
        self.assertTrue(is_palindrome("A man a plan a canal Panama"))

    def test_not_palindrome(self):
        self.assertFalse(is_palindrome("hello"))

if __name__ == "__main__":
    unittest.main()
```

## pytest (Recommended)

```python
# test_palindrome.py
def test_simple():
    assert is_palindrome("racecar")

def test_with_spaces():
    assert is_palindrome("A man a plan a canal Panama")

def test_not_palindrome():
    assert not is_palindrome("hello")
```

Run: `pytest test_palindrome.py -v`

## Fixtures

```python
import pytest

@pytest.fixture
def sample_data():
    return [1, 2, 3, 4, 5]

def test_sum(sample_data):
    assert sum(sample_data) == 15
```

## Parametrized Tests

```python
@pytest.mark.parametrize("input,expected", [
    ("racecar", True),
    ("hello", False),
    ("", True),
])
def test_palindrome(input, expected):
    assert is_palindrome(input) == expected
```

## Practice

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Saidsp19/cognitive-vidya/blob/main/notebooks/python-course/08-advance./testing.ipynb)

**Next:** [Type Hints](./type-hints)
