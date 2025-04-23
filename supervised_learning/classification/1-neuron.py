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

        self.__W = np.random.normal(0, 1, (1, nx))
        self.__b = 0
        self.__A = 0

    @property
    def W(self):
        """Getter for W"""
        return self.__W

    @property
    def b(self):
        """Getter for b"""
        return self.__b

    @property
    def A(self):
        """Getter for A"""
        return self.__A
