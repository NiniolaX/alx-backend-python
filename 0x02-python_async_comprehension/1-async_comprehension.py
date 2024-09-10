#!/usr/bin/env python3
"""
Contains a coroutine that returns a list of 10 random numbers using async
comprehension over a coroutine async_generator
"""
from typing import Iterable

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> Iterable[float]:
    """
    Returns a list of 10 random numbers using async comprehension over
    coroutine async_generator()
    """
    return [i async for i in async_generator()]
