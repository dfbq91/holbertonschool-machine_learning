#!/usr/bin/env python3
"""13-cats-tongue"""


import numpy as np


def np_cat(mat1, mat2, axis=0):
    """Returns concatenated matrices"""
    return np.concatenate((mat1, mat2), axis)
