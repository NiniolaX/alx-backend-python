#!/usr/bin/env python3
"""
Contains an async routine that executes multiple coroutines at the same time.
"""
from typing import List
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns an asynchronous coroutine (task_wait_random) n times with the
    specified max_delay and returns the list of delays in ascending order.

    Args:
        n (int): The number of times to spawn task_wait_random.
        max_delay (int): The maximum delay value to pass to wait_random.

    Returns:
        List[float]: List of delay times in ascending order.
    """
    coroutines = [task_wait_random(max_delay) for _ in range(n)]
    delays = []
    for coroutine in asyncio.as_completed(coroutines):
        result = await coroutine
        delays.append(result)
    return delays
