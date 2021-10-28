# This file is for the mathematical functions in the tasks related to numerical derivation
# You can include this file to access the different function: f_1, f_2, f_3 and f_4
import numpy as np


def f_1(x):
    result = 7 * (x ** 2) - 8 * x + 1
    return result


def f_2(x):
    result = np.sin(x)
    return result


def f_3(x):
    result = (1 - x)/(x + 3)**2
    return result


def f_4(x):
    result = np.sqrt(1+x**2)
    return result
