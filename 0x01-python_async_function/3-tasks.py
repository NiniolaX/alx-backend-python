#!/usr/bin/env python3
"""
Contains function that returns a asyncio.Task
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Returns a asyncio.Task

    Args:
        max_delay (int): The maximum delay value to pass to wait_random

    Return:
        (asyncio.Task): an asynchronous task
    """
    return asyncio.create_task(wait_random(max_delay))
