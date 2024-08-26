#!/usr/bin/env python3
"""
Contains an async routine that executes two coroutines at the same time """
from typing import List
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns an asynchronous coroutine (wait_random) n times with the specified
    max_delay and returns the list of delays in ascending order.

    Args:
        n (int): The number of times to spawn wait_random.
        max_delay (int): The maximum delay value to pass to wait_random.

    Returns:
        List[float]: List of delay times in ascending order.
    """
    coroutines = [wait_random(max_delay) for _ in range(n)]
    delays = []
    for coroutine in asyncio.as_completed(coroutines):
        result = await coroutine
        delays.append(result)
    return delays
