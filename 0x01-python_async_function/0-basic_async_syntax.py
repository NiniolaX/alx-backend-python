#!/usr/bin/env python3
"""
Contains a coroutine 'wait_random' that waits for a randomly generated delay
and returns the duration of the delay.
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Waits for a random delay between 0 and max_delay (included and float
    value) and returns the duration of the delay.

    Uses the `random` module to generate random delays.

    Args:
        max_delay (int): The maximum duration of delay

    Return:
        int: Duration of delay
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
