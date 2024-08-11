#!/usr/bin/env python3
"""
Contains function that takes in a string and an int or float and returns a
tuple.
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, Union[float]]:
    """Takes in a list of floats and returns their sum
    Args:
        k(str): String to be added to tuple
        v(int or float): Number to be added to tuple
    Return:
        (tuple)
    """
    return (k, v**2)
