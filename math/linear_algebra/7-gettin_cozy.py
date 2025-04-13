#!/usr/bin/env python3
"""7-gettin cozy"""


def cat_matrices2D(mat1, mat2, axis=0):
    """Returns a new concatenat matrix"""
    if len(mat1) == 0 or len(mat2) == 0:
        return None
    if axis == 0:
        return mat1 + mat2
    else:
        if len(mat1) != len(mat2):
            return None
        return [mat1[i] + mat2[i] for i in range(len(mat2))]