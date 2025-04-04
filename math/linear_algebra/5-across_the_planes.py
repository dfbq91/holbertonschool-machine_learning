#!/usr/bin/env python3
"""across the planes"""


def add_matrices2D(mat1, mat2):
    """Adds two matrices element-wise"""
    len_m1 = len(mat1)
    len_m2 = len(mat2)
    result = []

    if len_m1 != len_m2:
        return None

    for arr1, arr2 in zip(mat1, mat2):
        if len(arr1) != len(arr2):
            return None
        previous = []
        # print('arr1', arr1)
        # print('arr2', arr2)
        for i, j in zip(arr1, arr2):
            previous.append(i + j)
        result.append(previous)
    return result
