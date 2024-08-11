#!/usr/bin/env python3
"""
Contains a type-annoted function that takes in a list and returns a list of
tuples.
"""
from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns a list of tuples
    """
    return [(i, len(i)) for i in lst]
