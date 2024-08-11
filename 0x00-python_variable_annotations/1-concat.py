#!/usr/bin/env python3
"""
Contains a type-annoted function that takes in two strings and concatenates
them.
"""


def concat(str1: str, str2: str) -> str:
    """ Concatenates two strings
    Args:
        str1(str): First string
        str2(str): Second string
    Return:
        (str): Concatenation of two strings
    """
    return str1 + str2
