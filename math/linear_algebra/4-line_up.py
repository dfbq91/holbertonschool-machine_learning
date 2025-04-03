#!/usr/bin/env python3
"""Adds two arrays element-wise"""


def add_arrays(arr1, arr2):
    """Adds two arrays element-wise"""
    result = []
    if (len(arr1) != len(arr2)):
        return None
    for x, y in zip(arr1, arr2):
        result.append(x + y)
    return result