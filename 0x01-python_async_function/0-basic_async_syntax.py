#!/usr/bin/env python3
"""
Contains a coroutine
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> int:
    """
    Waits for a random delay between 0 and max_delay (included and float
    value) and returns the duration of the delay
    """
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
