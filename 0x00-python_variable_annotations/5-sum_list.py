#!/usr/bin/env python3

"""a type-annotated function sum_list"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Calculate the sum of a list of floats.

    Args:
        input_list: A list of floats.

    Returns:
        The sum of the floats in the input list.
    """
    return sum(input_list)
