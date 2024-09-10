#!/usr/bin/env python3
"""
Contains an asynchronous coroutine that executes another asynchronous
coroutine four times in parallel and measures its total runtime.
"""
from time import time
import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Runs an asynchronous coroutine 4 times concurrently and returns its
    runtime.
    """
    start = time()
    await asyncio.gather(*[async_comprehension() for _ in range(4)])
    end = time()
    runtime = end - start
    return runtime
