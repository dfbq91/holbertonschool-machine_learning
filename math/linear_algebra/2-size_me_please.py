#!/usr/bin/env python3
"""Calculates the shape of a matrix"""


def matrix_shape(matrix):
    """Calculates the shape of a matrix"""
    result = []
    while (type(matrix) is list):
        result.append(len(matrix))
        matrix = matrix[0]
    return result
