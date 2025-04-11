#!/usr/bin/env python3
"""Module to plot a graph comparing two exponential decay functions."""


import numpy as np
import matplotlib.pyplot as plt


def two():
    """Plot a graph comparing two exponential decay functions."""
    x = np.arange(0, 21000, 1000)
    r = np.log(0.5)
    t1 = 5730
    t2 = 1600
    y1 = np.exp((r / t1) * x)
    y2 = np.exp((r / t2) * x)
    plt.figure(figsize=(6.4, 4.8))

    plt.title('Exponential Decay of Radioactive Elements')
    plt.xlabel('Time (years)')
    plt.ylabel('Fraction Remaining')
    plt.xlim(0, 20000)
    plt.ylim(0, 1)
    plt.plot(x, y1, label='C-14', color='r', linestyle=':')
    plt.plot(x, y2, label='Ra-226', color='green', linestyle='-')
    plt.legend(loc='upper right')
    plt.show()
