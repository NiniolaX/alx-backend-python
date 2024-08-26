#!/usr/bin/env python3
"""
Contains a function that measures and returns the runtime of another function
wait_n.
"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ Measures and returns the runtime of function wait_n
    Args:
        n (int): First argument to pass to wait_n.
        max_delay (int): Second argument to pass to wait_n.
    Return:
        (float): total_time / n
    """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    total_time = end - start
    return total_time / n
