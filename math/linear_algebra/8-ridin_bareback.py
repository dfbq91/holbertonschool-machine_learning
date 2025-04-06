#!/usr/bin/env python3
"""8-ridin bareback"""

def mat_mul(mat1, mat2):
    """Returns the product of two matrices"""
    if not isinstance(mat1, list) or not isinstance(mat2, list):
        return None
    if len(mat1) == 0 or len(mat2) == 0:
        return None
    if not all(isinstance(i, list) for i in mat1):
        return None
    if not all(isinstance(i, list) for i in mat2):
        return None
    if len(mat1[0]) != len(mat2):
        return None
    for i in mat1:
        if len(i) != len(mat1[0]):
            return None
    for i in mat2:
        if len(i) != len(mat2[0]):
            return None
    result = [[0 for j in range(len(mat2[0]))] for i in range(len(mat1))]
    for i in range(len(mat1)):
        for j in range(len(mat2[0])):
            for k in range(len(mat2)):
                result[i][j] += mat1[i][k] * mat2[k][j]
    return result