#!/usr/bin/env python3
"""
neuron.py
A simple implementation of a neuron in Python.
"""


import numpy as np


class Neuron:
    """A simple neuron class."""

    def __init__(self, nx):
        """Initialize the neuron"""

        if not isinstance(nx, int):
            raise TypeError("nx must be an integer")
        if nx <= 0:
            raise ValueError("nx must be a positive integer")

        self.W = np.random.normal(0, 1, (1, nx))
        self.b = 0
        self.A = 0
