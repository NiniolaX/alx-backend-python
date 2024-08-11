#!/usr/bin/env python3
"""
Contains type-annoted function that takes in a list of integers and floats and
returns their sum as a float.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Takes in a list of integers and floats and returns their sum
    Args:
        mxd_lst(list of ints and floats): List of integers and floats
    Return:
        (float): sum of numbers in list
    """
    return sum(mxd_lst)
