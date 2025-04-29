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

    def sigmoid(self, Z):
        """Sigmoid activation function: 1/(1 + e^(-Z))"""
        return 1 / (1 + np.exp(-Z))

    def forward_prop(self, X):
        """Calculates forward propagation of the neuron"""
        Z = np.dot(self.__W, X) + self.__b
        self.__A = self.sigmoid(Z)
        return self.__A

    def cost(self, Y, A):
        """
        Calculates the cost of the model with LR
        Y: numpy.ndarray - labels for the input data
        A activated output of the neuron for each example
        """
        m = Y.shape[1]
        C = - (1 / m) * np.sum(
            np.multiply(
                Y, np.log(A)) + np.multiply(
                1 - Y, np.log(1.0000001 - A)))
        return C

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
