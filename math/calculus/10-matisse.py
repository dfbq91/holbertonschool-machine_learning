#!/usr/bin/env python3
"""10-poly"""


def poly_derivative(poly):
    """Calculates the derivative of a polynomial.

    Args:
        poly (list): A list of coefficients representing a polynomial.

    Returns:
        list: A list of coefficients
    """
    result = []
    if type(poly) is not list or len(poly) == 0:
        return None
    if len(poly) == 1:
        return [0]
    for i in range(0, len(poly)):
        if i == 0:
            continue
        else:
            result.append(poly[i] * i)
    if all(c == 0 for c in result):
        return [0]
    return result
