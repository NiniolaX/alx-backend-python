#!/usr/bin/env python3
"""
Contains function that takes in a list of floats as argument and returns their
sum as float.
"""


def sum_list(input_list: list[float]) -> float:
    """Takes in a list of floats and returns their sum
    Args:
        input_list(list of floats): List of floats
    Return:
        (float): sum of floats in list
    """
    return sum(input_list)
