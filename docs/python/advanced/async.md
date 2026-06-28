---
sidebar_position: 4
---

# Async Python Basics

**Module 8 · Lesson 4** | Difficulty: Expert

## Synchronous vs Asynchronous

**Synchronous** code runs line by line — if one task waits (network, disk), everything blocks.

**Asynchronous** code can switch to other tasks while waiting — ideal for I/O-bound work (APIs, web servers, file downloads).

## `async` and `await`

```python
import asyncio

async def fetch_data(url: str) -> str:
    await asyncio.sleep(1)  # simulate network delay
    return f"Data from {url}"

async def main():
    result = await fetch_data("https://api.example.com")
    print(result)

asyncio.run(main())
```

## Running Multiple Tasks Concurrently

```python
async def main():
    results = await asyncio.gather(
        fetch_data("url1"),
        fetch_data("url2"),
        fetch_data("url3"),
    )
    print(results)  # all three complete in ~1 second, not 3
```

## Async Context Managers

```python
import aiohttp

async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()
```

## When to Use Async

| Use Async | Use Sync |
|-----------|----------|
| Web APIs, microservices | CPU-heavy computation |
| Many concurrent I/O operations | Simple scripts |
| WebSockets, chat servers | Data science pipelines |

For CPU-bound parallelism, use `multiprocessing` instead.

## Practice

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Saidsp19/cognitive-vidya/blob/main/notebooks/python-course/08-advance./async.ipynb)

**Next:** [Best Practices](./best-practices)
