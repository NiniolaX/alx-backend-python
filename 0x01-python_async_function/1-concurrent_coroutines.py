#!/usr/bin/env python3
"""
Contains an async routine that executes two coroutines at the same time """
from typing import List
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns an asynchronous coroutine n times and returns a list of duration of
    each coroutine in ascending order.
    """
    coroutines = [wait_random(max_delay) for i in range(n)]
    delays = await asyncio.gather(*coroutines)
    delays.sort()
    return delays
