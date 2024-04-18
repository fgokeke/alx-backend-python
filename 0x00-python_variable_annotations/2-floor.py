#!/usr/bin/env python3

"""a type-annotated function floor which takes a float"""

import math


def floor(n: float) -> int:
    """
    Return the largest integer less than or equal to the given float.

    Parameters:
        n (float): The input float value.

    Returns:
        int: The floor value of the input float.
    """
    return math.floor(n)
