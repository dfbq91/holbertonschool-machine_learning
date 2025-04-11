#!/usr/bin/env python3
"""Module to plot a histogram of student grades."""


import numpy as np
import matplotlib.pyplot as plt


def frequency():
    """Plot a histogram of student grades."""
    np.random.seed(5)
    student_grades = np.random.normal(68, 15, 50)
    plt.figure(figsize=(6.4, 4.8))

    plt.hist(student_grades, edgecolor='black',
            bins=[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
    plt.xticks(ticks=[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
    plt.xlabel('Grades')
    plt.ylabel('Number of Students')
    plt.title('Project A')
    plt.axis([0, 100, 0, 30])
    plt.show()
