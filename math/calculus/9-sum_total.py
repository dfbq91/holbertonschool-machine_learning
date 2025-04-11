#!/usr/bin/env python3
"""sum_total"""


def summation_i_squared(n):
    """Summation of i^2 from 1 to n."""
    if n == 1:
        return 1
    if type(n) != int or n < 1:
        return None
    return summation_i_squared(n - 1) + n ** 2 
