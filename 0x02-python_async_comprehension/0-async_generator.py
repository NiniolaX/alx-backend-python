#!/usr/bin/env python3
"""
Contains a coroutine that loops each time, yields a random number and waits 1
second.
"""
from typing import Generator
import asyncio
import random


async def async_generator() -> Generator[float, None, None]:
    """
    Loops 10 times, each time asynchronously waiting 1 second, then yield a
    random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
