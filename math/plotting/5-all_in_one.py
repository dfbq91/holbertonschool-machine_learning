#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

def all_in_one():

    y0 = np.arange(0, 11) ** 3

    mean = [69, 0]
    cov = [[15, 8], [8, 15]]
    np.random.seed(5)
    x1, y1 = np.random.multivariate_normal(mean, cov, 2000).T
    y1 += 180

    x2 = np.arange(0, 28651, 5730)
    r2 = np.log(0.5)
    t2 = 5730
    y2 = np.exp((r2 / t2) * x2)

    x3 = np.arange(0, 21000, 1000)
    r3 = np.log(0.5)
    t31 = 5730
    t32 = 1600
    y31 = np.exp((r3 / t31) * x3)
    y32 = np.exp((r3 / t32) * x3)

    np.random.seed(5)
    student_grades = np.random.normal(68, 15, 50)

    fig = plt.figure()

    first = fig.add_subplot(3, 2, 1)
    first.plot(y0, 'r-')
    first.set_xlim((0, 10))

    second = fig.add_subplot(3, 2, 2)
    second.scatter(x1, y1, c='m')
    second.set_title("Men's Height vs Weight", fontsize='x-small')
    second.set_xlabel('Height (in)', fontsize='x-small')
    second.set_ylabel('Weight (lbs)', fontsize='x-small')

    third = fig.add_subplot(3, 2, 3)
    third.plot(x2, y2)
    third.set_title("Exponential Decay of C-14", fontsize='x-small')
    third.set_xlabel('Time (years)', fontsize='x-small')
    third.set_ylabel('Fraction Remaining', fontsize='x-small')
    third.set_yscale("log")
    third.set_xlim((0, 28650))

    fourth = fig.add_subplot(3, 2, 4)
    fourth.plot(x3, y31, 'r--', label='C-14')
    fourth.plot(x3, y32, 'g-', label='Ra-226')
    fourth.set_title("Exponential Decay of Radioactive Elements", fontsize='x-small')
    fourth.set_xlabel('Time (years)', fontsize='x-small')
    fourth.set_ylabel('Fraction Remaining', fontsize='x-small')
    fourth.legend()
    fourth.set_xlim((0, 20000))
    fourth.set_ylim((0, 1))

    fifth = fig.add_subplot(3, 1, 3)
    fifth.hist(student_grades,
            bins=[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
            edgecolor='black')
    fifth.set_title("Project A", fontsize='x-small')
    fifth.set_xlabel('Grades', fontsize='x-small')
    fifth.set_ylabel('Number of Students', fontsize='x-small')
    fifth.set_xlim((0, 100))
    fifth.set_xticks(np.arange(0, 101, 10))
    fifth.set_ylim((0, 30))

    fig.suptitle("All in One")
    plt.tight_layout()
    plt.show()

all_in_one()