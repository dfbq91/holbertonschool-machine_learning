#!/usr/bin/env python3
"""sum_total"""


def summation_i_squared(n):
    """Summation of i^2 from 1 to n."""
    if type(n) != int or n < 1:
        return None
    return sum(map(lambda i: i**2, range(1, n+1)))
