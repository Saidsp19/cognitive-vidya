#!/usr/bin/env python3
"""Generate all Python course notebooks with auto-graders."""
import json
from pathlib import Path

ROOT = Path(__file__).parent.parent / "notebooks" / "python-course"

NOTEBOOKS = {
    "01-fundamentals/01-introduction.ipynb": {
        "title": "Introduction to Python",
        "module": "Module 1 · Lesson 1",
        "desc": "Your first Python exercises — print, comments, and basic expressions.",
        "exercises": '''
def exercise_greet(name: str) -> str:
    """Return 'Hello, {name}!'"""
    pass

def exercise_add(a, b):
    """Return the sum of a and b."""
    pass

def exercise_is_python_fun() -> bool:
    """Return True (Python is fun!)."""
    pass
''',
        "tests": '''
    tests = [
        ("exercise_greet", exercise_greet, [("World", "Hello, World!"), ("Alice", "Hello, Alice!")]),
        ("exercise_add", exercise_add, [(2, 3, 5), (10, -5, 5), (0, 0, 0)]),
        ("exercise_is_python_fun", exercise_is_python_fun, [(True,)]),
    ]
    for name, func, cases in tests:
        for case in cases:
            expected = case[-1]
            args = case[:-1]
            try:
                result = func(*args) if args else func()
                if result == expected:
                    passed += 1
                    print(f"✅ {name}{args} Passed")
                else:
                    print(f"❌ {name}{args} Failed. Expected {expected}, got {result}")
            except Exception as e:
                print(f"⚠️ {name} Error: {e}")
''',
    },
    "01-fundamentals/02-setup.ipynb": {
        "title": "Setting Up Python",
        "module": "Module 1 · Lesson 2",
        "desc": "Verify your environment and run basic Python operations.",
        "exercises": '''
def exercise_version_tuple() -> tuple:
    """Return (3, 10) representing a valid Python 3.10+ version."""
    pass

def exercise_multiline_sum() -> int:
    """Return sum of 1+2+3+4+5 without using sum()."""
    pass
''',
        "tests": '''
    if exercise_version_tuple() == (3, 10):
        passed += 1; print("✅ exercise_version_tuple Passed")
    else:
        print("❌ exercise_version_tuple Failed")
    if exercise_multiline_sum() == 15:
        passed += 1; print("✅ exercise_multiline_sum Passed")
    else:
        print("❌ exercise_multiline_sum Failed")
''',
    },
    "01-fundamentals/03-variables-types.ipynb": {
        "title": "Variables & Data Types",
        "module": "Module 1 · Lesson 3",
        "desc": "Practice variables, types, and type conversion.",
        "exercises": '''
def exercise_types() -> dict:
    """Return dict with keys int, float, str, bool mapping to example values."""
    pass

def exercise_cast_to_int(value: str) -> int:
    """Convert string to int."""
    pass

def exercise_floor_div(a: int, b: int) -> int:
    """Return a // b."""
    pass
''',
        "tests": '''
    t = exercise_types()
    if isinstance(t, dict) and isinstance(t.get("int"), int):
        passed += 1; print("✅ exercise_types Passed")
    else:
        print("❌ exercise_types Failed")
    if exercise_cast_to_int("42") == 42:
        passed += 1; print("✅ exercise_cast_to_int Passed")
    else:
        print("❌ exercise_cast_to_int Failed")
    if exercise_floor_div(10, 3) == 3:
        passed += 1; print("✅ exercise_floor_div Passed")
    else:
        print("❌ exercise_floor_div Failed")
''',
    },
    "01-fundamentals/04-operators.ipynb": {
        "title": "Operators & Expressions",
        "module": "Module 1 · Lesson 4",
        "desc": "Comparison, logical operators, and f-strings.",
        "exercises": '''
def exercise_in_range(x: int) -> bool:
    """Return True if 1 <= x <= 100."""
    pass

def exercise_fstring(name: str, score: float) -> str:
    """Return '{name} scored {score:.1f}%' e.g. 'Bob scored 95.5%'"""
    pass

def exercise_all_true(a, b, c) -> bool:
    """Return True only if all three are truthy."""
    pass
''',
        "tests": '''
    if exercise_in_range(50) and not exercise_in_range(0):
        passed += 1; print("✅ exercise_in_range Passed")
    else:
        print("❌ exercise_in_range Failed")
    if exercise_fstring("Bob", 95.567) == "Bob scored 95.6%":
        passed += 1; print("✅ exercise_fstring Passed")
    else:
        print("❌ exercise_fstring Failed")
    if exercise_all_true(1, "hi", [1]) and not exercise_all_true(1, 0, 1):
        passed += 1; print("✅ exercise_all_true Passed")
    else:
        print("❌ exercise_all_true Failed")
''',
    },
    "01-fundamentals/05-input-output.ipynb": {
        "title": "Input & Output",
        "module": "Module 1 · Lesson 5",
        "desc": "String formatting and text processing.",
        "exercises": '''
def exercise_clean_and_upper(text: str) -> str:
    """Strip whitespace and return uppercase."""
    pass

def exercise_parse_name_age(line: str) -> tuple:
    """Parse 'Name,25' into ('Name', 25)."""
    pass

def exercise_join_words(words: list) -> str:
    """Join words with '-'."""
    pass
''',
        "tests": '''
    if exercise_clean_and_upper("  hello  ") == "HELLO":
        passed += 1; print("✅ exercise_clean_and_upper Passed")
    else:
        print("❌ exercise_clean_and_upper Failed")
    if exercise_parse_name_age("Alice,30") == ("Alice", 30):
        passed += 1; print("✅ exercise_parse_name_age Passed")
    else:
        print("❌ exercise_parse_name_age Failed")
    if exercise_join_words(["a","b","c"]) == "a-b-c":
        passed += 1; print("✅ exercise_join_words Passed")
    else:
        print("❌ exercise_join_words Failed")
''',
    },
    "02-control-flow/06-conditionals.ipynb": {
        "title": "Conditionals",
        "module": "Module 2 · Lesson 1",
        "desc": "if/elif/else logic exercises.",
        "exercises": '''
def exercise_grade(score: int) -> str:
    """Return A(90+), B(80+), C(70+), D(60+), F otherwise."""
    pass

def exercise_sign(n: int) -> str:
    """Return 'positive', 'negative', or 'zero'."""
    pass

def exercise_leap_year(year: int) -> bool:
    """Return True if year is a leap year."""
    pass
''',
        "tests": '''
    if exercise_grade(85) == "B" and exercise_grade(59) == "F":
        passed += 1; print("✅ exercise_grade Passed")
    else:
        print("❌ exercise_grade Failed")
    if exercise_sign(5) == "positive" and exercise_sign(0) == "zero":
        passed += 1; print("✅ exercise_sign Passed")
    else:
        print("❌ exercise_sign Failed")
    if exercise_leap_year(2024) and not exercise_leap_year(1900):
        passed += 1; print("✅ exercise_leap_year Passed")
    else:
        print("❌ exercise_leap_year Failed")
''',
    },
    "02-control-flow/07-for-loops.ipynb": {
        "title": "For Loops",
        "module": "Module 2 · Lesson 2",
        "desc": "Iteration, range, and accumulator patterns.",
        "exercises": '''
def exercise_sum_list(nums: list) -> int:
    """Sum all numbers without using sum()."""
    pass

def exercise_count_evens(nums: list) -> int:
    """Count even numbers in list."""
    pass

def exercise_fizzbuzz_value(n: int) -> str:
    """Return FizzBuzz value for n (Fizz, Buzz, FizzBuzz, or str(n))."""
    pass
''',
        "tests": '''
    if exercise_sum_list([1,2,3,4,5]) == 15:
        passed += 1; print("✅ exercise_sum_list Passed")
    else:
        print("❌ exercise_sum_list Failed")
    if exercise_count_evens([1,2,3,4,5,6]) == 3:
        passed += 1; print("✅ exercise_count_evens Passed")
    else:
        print("❌ exercise_count_evens Failed")
    if exercise_fizzbuzz_value(15) == "FizzBuzz" and exercise_fizzbuzz_value(3) == "Fizz":
        passed += 1; print("✅ exercise_fizzbuzz_value Passed")
    else:
        print("❌ exercise_fizzbuzz_value Failed")
''',
    },
    "02-control-flow/08-while-loops.ipynb": {
        "title": "While Loops",
        "module": "Module 2 · Lesson 3",
        "desc": "While loops and sentinel patterns.",
        "exercises": '''
def exercise_countdown(n: int) -> list:
    """Return [n, n-1, ..., 1] using while loop."""
    pass

def exercise_collatz_steps(n: int) -> int:
    """Return number of steps to reach 1 in Collatz sequence (n > 0)."""
    pass
''',
        "tests": '''
    if exercise_countdown(5) == [5,4,3,2,1]:
        passed += 1; print("✅ exercise_countdown Passed")
    else:
        print("❌ exercise_countdown Failed")
    if exercise_collatz_steps(10) == 6:
        passed += 1; print("✅ exercise_collatz_steps Passed")
    else:
        print("❌ exercise_collatz_steps Failed")
''',
    },
    "03-data-structures/09-lists.ipynb": {
        "title": "Lists",
        "module": "Module 3 · Lesson 1",
        "desc": "List manipulation, slicing, and methods.",
        "exercises": '''
def exercise_reverse_list(lst: list) -> list:
    """Return reversed list without using reversed() or [::-1]."""
    pass

def exercise_remove_duplicates(lst: list) -> list:
    """Return list with duplicates removed, preserving order."""
    pass

def exercise_flatten(nested: list) -> list:
    """Flatten one level: [[1,2],[3]] -> [1,2,3]."""
    pass
''',
        "tests": '''
    if exercise_reverse_list([1,2,3]) == [3,2,1]:
        passed += 1; print("✅ exercise_reverse_list Passed")
    else:
        print("❌ exercise_reverse_list Failed")
    if exercise_remove_duplicates([1,2,2,3,1]) == [1,2,3]:
        passed += 1; print("✅ exercise_remove_duplicates Passed")
    else:
        print("❌ exercise_remove_duplicates Failed")
    if exercise_flatten([[1,2],[3,4]]) == [1,2,3,4]:
        passed += 1; print("✅ exercise_flatten Passed")
    else:
        print("❌ exercise_flatten Failed")
''',
    },
    "03-data-structures/10-tuples-sets.ipynb": {
        "title": "Tuples & Sets",
        "module": "Module 3 · Lesson 2",
        "desc": "Immutable tuples and unique sets.",
        "exercises": '''
def exercise_swap(a, b):
    """Return (b, a) using tuple unpacking."""
    pass

def exercise_set_operations(a: set, b: set) -> dict:
    """Return dict with keys union, intersection, difference."""
    pass
''',
        "tests": '''
    if exercise_swap(1, 2) == (2, 1):
        passed += 1; print("✅ exercise_swap Passed")
    else:
        print("❌ exercise_swap Failed")
    r = exercise_set_operations({1,2,3}, {3,4,5})
    if r and r.get("union") == {1,2,3,4,5} and r.get("intersection") == {3}:
        passed += 1; print("✅ exercise_set_operations Passed")
    else:
        print("❌ exercise_set_operations Failed")
''',
    },
    "03-data-structures/11-dictionaries.ipynb": {
        "title": "Dictionaries",
        "module": "Module 3 · Lesson 3",
        "desc": "Key-value pairs and dict operations.",
        "exercises": '''
def exercise_word_count(words: list) -> dict:
    """Return frequency count of each word."""
    pass

def exercise_invert_dict(d: dict) -> dict:
    """Swap keys and values (values are unique)."""
    pass
''',
        "tests": '''
    if exercise_word_count(["a","b","a"]) == {"a":2,"b":1}:
        passed += 1; print("✅ exercise_word_count Passed")
    else:
        print("❌ exercise_word_count Failed")
    if exercise_invert_dict({"a":1,"b":2}) == {1:"a",2:"b"}:
        passed += 1; print("✅ exercise_invert_dict Passed")
    else:
        print("❌ exercise_invert_dict Failed")
''',
    },
    "03-data-structures/12-strings.ipynb": {
        "title": "Strings",
        "module": "Module 3 · Lesson 4",
        "desc": "String methods and manipulation.",
        "exercises": '''
def exercise_is_palindrome(s: str) -> bool:
    """Check if s is palindrome (ignore case and non-alphanumeric)."""
    pass

def exercise_title_case(s: str) -> str:
    """Return title-cased string."""
    pass
''',
        "tests": '''
    if exercise_is_palindrome("Racecar") and exercise_is_palindrome("A man, a plan, a canal: Panama"):
        passed += 1; print("✅ exercise_is_palindrome Passed")
    else:
        print("❌ exercise_is_palindrome Failed")
    if exercise_title_case("hello world") == "Hello World":
        passed += 1; print("✅ exercise_title_case Passed")
    else:
        print("❌ exercise_title_case Failed")
''',
    },
    "04-functions/13-functions-basics.ipynb": {
        "title": "Functions Basics",
        "module": "Module 4 · Lesson 1",
        "desc": "Define and use functions with parameters.",
        "exercises": '''
def exercise_factorial(n: int) -> int:
    """Return n! for n >= 0."""
    pass

def exercise_celsius_to_fahrenheit(c: float) -> float:
    """Convert Celsius to Fahrenheit."""
    pass

def exercise_greet(name: str, greeting: str = "Hello") -> str:
    """Return '{greeting}, {name}!'"""
    pass
''',
        "tests": '''
    if exercise_factorial(5) == 120 and exercise_factorial(0) == 1:
        passed += 1; print("✅ exercise_factorial Passed")
    else:
        print("❌ exercise_factorial Failed")
    if abs(exercise_celsius_to_fahrenheit(100) - 212.0) < 0.01:
        passed += 1; print("✅ exercise_celsius_to_fahrenheit Passed")
    else:
        print("❌ exercise_celsius_to_fahrenheit Failed")
    if exercise_greet("Bob") == "Hello, Bob!" and exercise_greet("Bob","Hi") == "Hi, Bob!":
        passed += 1; print("✅ exercise_greet Passed")
    else:
        print("❌ exercise_greet Failed")
''',
    },
    "04-functions/14-scope-closures.ipynb": {
        "title": "Scope & Closures",
        "module": "Module 4 · Lesson 2",
        "desc": "Closures and factory functions.",
        "exercises": '''
def make_adder(n):
    """Return a function that adds n to its argument."""
    pass

def make_counter():
    """Return a function that returns incrementing count starting at 1."""
    pass
''',
        "tests": '''
    add5 = make_adder(5)
    if add5 and add5(3) == 8:
        passed += 1; print("✅ make_adder Passed")
    else:
        print("❌ make_adder Failed")
    counter = make_counter()
    if counter and counter() == 1 and counter() == 2:
        passed += 1; print("✅ make_counter Passed")
    else:
        print("❌ make_counter Failed")
''',
    },
    "04-functions/15-functional-programming.ipynb": {
        "title": "Functional Programming",
        "module": "Module 4 · Lesson 3",
        "desc": "map, filter, lambda, and higher-order functions.",
        "exercises": '''
def exercise_filter_positives(nums: list) -> list:
    """Return positive numbers using filter."""
    pass

def exercise_apply_twice(func, value):
    """Apply func to value twice: func(func(value))."""
    pass
''',
        "tests": '''
    if exercise_filter_positives([-1,2,-3,4]) == [2,4]:
        passed += 1; print("✅ exercise_filter_positives Passed")
    else:
        print("❌ exercise_filter_positives Failed")
    if exercise_apply_twice(lambda x: x*2, 3) == 12:
        passed += 1; print("✅ exercise_apply_twice Passed")
    else:
        print("❌ exercise_apply_twice Failed")
''',
    },
    "05-oop/16-classes-objects.ipynb": {
        "title": "Classes & Objects",
        "module": "Module 5 · Lesson 1",
        "desc": "Create classes with attributes and methods.",
        "exercises": '''
class Rectangle:
    """Rectangle with width, height, area(), and perimeter()."""
    def __init__(self, width, height):
        pass

    def area(self):
        pass

    def perimeter(self):
        pass
''',
        "tests": '''
    r = Rectangle(3, 4)
    if r.area() == 12 and r.perimeter() == 14:
        passed += 1; print("✅ Rectangle Passed")
    else:
        print("❌ Rectangle Failed")
''',
    },
    "05-oop/17-inheritance.ipynb": {
        "title": "Inheritance",
        "module": "Module 5 · Lesson 2",
        "desc": "Extend classes with inheritance.",
        "exercises": '''
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError

class Dog(Animal):
    def speak(self):
        pass

class Cat(Animal):
    def speak(self):
        pass
''',
        "tests": '''
    if Dog("Rex").speak() == "Rex says Woof!" and Cat("Luna").speak() == "Luna says Meow!":
        passed += 1; print("✅ Inheritance Passed")
    else:
        print("❌ Inheritance Failed")
''',
    },
    "05-oop/18-polymorphism.ipynb": {
        "title": "Polymorphism",
        "module": "Module 5 · Lesson 3",
        "desc": "Dunder methods and polymorphic behavior.",
        "exercises": '''
class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __add__(self, other):
        pass

    def __repr__(self):
        pass
''',
        "tests": '''
    v = Vector(1,2) + Vector(3,4)
    if v and v.x == 4 and v.y == 6 and "Vector" in repr(v):
        passed += 1; print("✅ Vector Passed")
    else:
        print("❌ Vector Failed")
''',
    },
    "06-files-errors/19-exception-handling.ipynb": {
        "title": "Exception Handling",
        "module": "Module 6 · Lesson 1",
        "desc": "try/except and custom exceptions.",
        "exercises": '''
def safe_divide(a, b):
    """Return a/b or None if division by zero."""
    pass

def parse_int(s: str):
    """Return int(s) or None if invalid."""
    pass
''',
        "tests": '''
    if safe_divide(10, 2) == 5.0 and safe_divide(1, 0) is None:
        passed += 1; print("✅ safe_divide Passed")
    else:
        print("❌ safe_divide Failed")
    if parse_int("42") == 42 and parse_int("abc") is None:
        passed += 1; print("✅ parse_int Passed")
    else:
        print("❌ parse_int Failed")
''',
    },
    "06-files-errors/20-file-io.ipynb": {
        "title": "File I/O",
        "module": "Module 6 · Lesson 2",
        "desc": "Read and write files with pathlib.",
        "exercises": '''
from pathlib import Path

def write_and_read(path: str, content: str) -> str:
    """Write content to path and return read content."""
    pass

def count_lines(content: str) -> int:
    """Count non-empty lines in content string."""
    pass
''',
        "tests": '''
    import tempfile, os
    with tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".txt") as f:
        tmp = f.name
    try:
        if write_and_read(tmp, "hello\\nworld") == "hello\\nworld":
            passed += 1; print("✅ write_and_read Passed")
        else:
            print("❌ write_and_read Failed")
    finally:
        os.unlink(tmp)
    if count_lines("a\\n\\nb\\n") == 2:
        passed += 1; print("✅ count_lines Passed")
    else:
        print("❌ count_lines Failed")
''',
    },
    "06-files-errors/21-json-csv.ipynb": {
        "title": "JSON & CSV",
        "module": "Module 6 · Lesson 3",
        "desc": "Serialize and parse JSON data.",
        "exercises": '''
import json

def to_json(data: dict) -> str:
    """Serialize dict to JSON string with indent=2."""
    pass

def from_json(s: str) -> dict:
    """Parse JSON string to dict."""
    pass
''',
        "tests": '''
    d = {"name": "Alice", "age": 30}
    s = to_json(d)
    if s and "\\n" in s and from_json(s) == d:
        passed += 1; print("✅ JSON Passed")
    else:
        print("❌ JSON Failed")
''',
    },
    "07-intermediate/22-comprehensions.ipynb": {
        "title": "Comprehensions",
        "module": "Module 7 · Lesson 1",
        "desc": "List, dict, and set comprehensions.",
        "exercises": '''
def exercise_squares(n: int) -> list:
    """Return [0,1,4,...,n-1 squared] using comprehension."""
    pass

def exercise_word_lengths(words: list) -> dict:
    """Return {word: len(word)} using dict comprehension."""
    pass
''',
        "tests": '''
    if exercise_squares(5) == [0,1,4,9,16]:
        passed += 1; print("✅ exercise_squares Passed")
    else:
        print("❌ exercise_squares Failed")
    if exercise_word_lengths(["hi","hey"]) == {"hi":2,"hey":3}:
        passed += 1; print("✅ exercise_word_lengths Passed")
    else:
        print("❌ exercise_word_lengths Failed")
''',
    },
    "07-intermediate/23-generators.ipynb": {
        "title": "Generators",
        "module": "Module 7 · Lesson 2",
        "desc": "Generator functions with yield.",
        "exercises": '''
def fibonacci(n: int):
    """Yield first n Fibonacci numbers."""
    pass

def read_chunks(text: str, size: int):
    """Yield text in chunks of given size."""
    pass
''',
        "tests": '''
    if list(fibonacci(6)) == [0,1,1,2,3,5]:
        passed += 1; print("✅ fibonacci Passed")
    else:
        print("❌ fibonacci Failed")
    if list(read_chunks("abcdef", 2)) == ["ab","cd","ef"]:
        passed += 1; print("✅ read_chunks Passed")
    else:
        print("❌ read_chunks Failed")
''',
    },
    "07-intermediate/24-decorators.ipynb": {
        "title": "Decorators",
        "module": "Module 7 · Lesson 3",
        "desc": "Write and apply decorators.",
        "exercises": '''
def uppercase_result(func):
    """Decorator that uppercases string return value."""
    pass

@uppercase_result
def greet(name):
    return f"hello, {name}"
''',
        "tests": '''
    if greet("alice") == "HELLO, ALICE":
        passed += 1; print("✅ uppercase_result Passed")
    else:
        print("❌ uppercase_result Failed")
''',
    },
    "07-intermediate/25-context-managers.ipynb": {
        "title": "Context Managers",
        "module": "Module 7 · Lesson 4",
        "desc": "Build context managers with contextlib.",
        "exercises": '''
from contextlib import contextmanager

@contextmanager
def tag(name):
    """Print <name> on enter and </name> on exit."""
    pass
''',
        "tests": '''
    import io
    from contextlib import redirect_stdout
    buf = io.StringIO()
    with redirect_stdout(buf):
        with tag("div"):
            print("content")
    out = buf.getvalue()
    if "<div>" in out and "</div>" in out and "content" in out:
        passed += 1; print("✅ tag Passed")
    else:
        print("❌ tag Failed")
''',
    },
    "08-advanced/26-modules-packages.ipynb": {
        "title": "Modules & Packages",
        "module": "Module 8 · Lesson 1",
        "desc": "Import and use standard library modules.",
        "exercises": '''
import math
from collections import Counter

def exercise_stdlib(nums: list) -> dict:
    """Return {mean, median, mode} for nums. Use statistics module for median."""
    pass
''',
        "tests": '''
    import statistics
    r = exercise_stdlib([1,2,2,3])
    if r and abs(r["mean"] - 2.0) < 0.01 and r["mode"] == 2:
        passed += 1; print("✅ exercise_stdlib Passed")
    else:
        print("❌ exercise_stdlib Failed")
''',
    },
    "08-advanced/27-testing.ipynb": {
        "title": "Testing",
        "module": "Module 8 · Lesson 2",
        "desc": "Write testable functions and assertions.",
        "exercises": '''
def is_prime(n: int) -> bool:
    """Return True if n is prime (n >= 2)."""
    pass

def run_self_tests():
    """Run assertions testing is_prime. Return True if all pass."""
    pass
''',
        "tests": '''
    if is_prime(7) and not is_prime(9) and is_prime(2):
        passed += 1; print("✅ is_prime Passed")
    else:
        print("❌ is_prime Failed")
    if run_self_tests():
        passed += 1; print("✅ run_self_tests Passed")
    else:
        print("❌ run_self_tests Failed")
''',
    },
    "08-advanced/28-type-hints.ipynb": {
        "title": "Type Hints",
        "module": "Module 8 · Lesson 3",
        "desc": "Annotate functions with type hints.",
        "exercises": '''
def merge_dicts(a: dict[str, int], b: dict[str, int]) -> dict[str, int]:
    """Merge two dicts (b overwrites a on conflict)."""
    pass

def first_or_none(items: list) -> object:
    """Return first item or None if empty."""
    pass
''',
        "tests": '''
    if merge_dicts({"a":1},{"b":2,"a":3}) == {"a":3,"b":2}:
        passed += 1; print("✅ merge_dicts Passed")
    else:
        print("❌ merge_dicts Failed")
    if first_or_none([1,2]) == 1 and first_or_none([]) is None:
        passed += 1; print("✅ first_or_none Passed")
    else:
        print("❌ first_or_none Failed")
''',
    },
    "08-advanced/29-async.ipynb": {
        "title": "Async Basics",
        "module": "Module 8 · Lesson 4",
        "desc": "async/await fundamentals.",
        "exercises": '''
import asyncio

async def fetch_value(delay: float, value: int) -> int:
    """Await asyncio.sleep(delay) and return value."""
    pass

async def fetch_all() -> list:
    """Gather fetch_value(0.01,1), fetch_value(0.01,2), fetch_value(0.01,3)."""
    pass
''',
        "tests": '''
    import asyncio
    if asyncio.run(fetch_value(0.001, 42)) == 42:
        passed += 1; print("✅ fetch_value Passed")
    else:
        print("❌ fetch_value Failed")
    if asyncio.run(fetch_all()) == [1,2,3]:
        passed += 1; print("✅ fetch_all Passed")
    else:
        print("❌ fetch_all Failed")
''',
    },
    "08-advanced/30-best-practices.ipynb": {
        "title": "Best Practices",
        "module": "Module 8 · Lesson 5",
        "desc": "Capstone — idiomatic Python refactoring.",
        "exercises": '''
def count_words_unpythonic(words: list) -> dict:
    """Count word frequencies — refactor to be Pythonic."""
    result = {}
    for i in range(len(words)):
        w = words[i]
        found = False
        for k in result:
            if k == w:
                result[k] = result[k] + 1
                found = True
        if not found:
            result[w] = 1
    return result

def count_words_pythonic(words: list) -> dict:
    """Pythonic version using dict.get or Counter."""
    pass
''',
        "tests": '''
    words = ["a","b","a","c","b","a"]
    if count_words_pythonic(words) == count_words_unpythonic(words) == {"a":3,"b":2,"c":1}:
        passed += 1; print("✅ count_words_pythonic Passed")
    else:
        print("❌ count_words_pythonic Failed")
''',
    },
}


def make_notebook(meta: dict) -> dict:
    total_hint = meta["tests"].count("passed += 1")
    eval_code = f'''# --- EVALUATION ENGINE ---
def evaluate():
    passed = 0
    total = {max(total_hint, 1)}
{meta["tests"]}
    if passed == total:
        print("\\n🎉 ALL TESTS PASSED! Great work!")
    else:
        print(f"\\n📊 Score: {{passed}}/{{total}} tests passed")

evaluate()'''

    return {
        "cells": [
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    f"# {meta['title']}\n",
                    f"**{meta['module']}**\n",
                    f"\n{meta['desc']}\n",
                    "\nComplete the exercises below, then run the grader cell.",
                ],
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [line + "\n" for line in meta["exercises"].strip().split("\n")],
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [line + "\n" for line in eval_code.strip().split("\n")],
            },
        ],
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3",
            },
            "language_info": {"name": "python", "version": "3.10.0"},
        },
        "nbformat": 4,
        "nbformat_minor": 4,
    }


def main():
    for rel_path, meta in NOTEBOOKS.items():
        path = ROOT / rel_path
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, "w") as f:
            json.dump(make_notebook(meta), f, indent=1)
        print(f"Created {rel_path}")


if __name__ == "__main__":
    main()
