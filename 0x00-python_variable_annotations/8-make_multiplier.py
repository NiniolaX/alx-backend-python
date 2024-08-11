#!/usr/bin/env python3
"""
Contains type-annoted function that takes in a float and returns a function
where the float is used as a multiplier.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Takes in a float and returns a function
    Args:
        multiplier(float): Number to be used as multiplier in returning
            function
    Return:
        (func): Function to return
    """
    def multiplier_function(number: float) -> float:
        """Multiplies a given number with a multipier"""
        return number * multiplier

    return multiplier_function
