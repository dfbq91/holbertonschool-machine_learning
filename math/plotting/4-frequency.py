#!/usr/bin/env python3
"""Module to plot a histogram of student grades."""


import numpy as np
import matplotlib.pyplot as plt


def frequency():
    """Plot a histogram of student grades."""
    np.random.seed(5)
    student_grades = np.random.normal(68, 15, 50)
    plt.figure(figsize=(6.4, 4.8))

    plt.hist(student_grades, edgecolor='black', bins=range(0, 101, 10))
    plt.xticks(ticks=range(0, 101, 10))
    plt.xlabel('Grades')
    plt.ylabel('Number of Students')
    plt.title('Project A')
    plt.axis([0, 100, 0, 30])
    plt.show()
