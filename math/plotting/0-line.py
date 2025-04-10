#!/usr/bin/env python3
"""Plot a line graph with x and y values."""
import numpy as np
import matplotlib.pyplot as plt


def line():
    """Plot a line graph with x and y values."""
    y = np.arange(0, 11) ** 3
    plt.figure(figsize=(6.4, 4.8))

    plt.plot(y, color="red")
    plt.xlim(0, 10)
    plt.show()
