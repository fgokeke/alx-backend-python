#!/usr/bin/env python3

"""a type-annotated function make_multiplier"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Create a multiplier function.

    Args:
        multiplier: A float to multiply by.

    Returns:
        A function that takes a float and returns the
        result of multiplying it by the multiplier.
    """
    def multiplier_function(x: float) -> float:
        """
        Multiply a float by the multiplier.

        Args:
            x: The float to multiply.

        Returns:
            The result of multiplying x by the multiplier.
        """
        return x * multiplier

    return multiplier_function
