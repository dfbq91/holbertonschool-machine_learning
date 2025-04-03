#!/usr/bin/env python3
"""Transposes a matrix"""


def matrix_transpose(matrix):
    """Transposes a matrix"""
    result = []
    previous = []
    rows_number = len(matrix)
    columns_number = len(matrix[0])
    for i in range(columns_number):
        previous = []
        for j in range(rows_number):
            previous.append(matrix[j][i])
        if previous:
            result.append(previous)
    return result
