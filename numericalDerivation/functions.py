# This file is for the mathematical functions in the tasks related to numerical derivation
# You can include this file to access the different function: f_1, f_2, f_3 and f_4
import sympy as sym

x, y, dx = sym.symbols("x y dx")  # idk if dx actually does anything


def f_1():
    return 7*x**2-8*x+1


def f_2():
    return sym.sin(x)


def f_3():
    return (1 - x)/(x + 3)**2


def f_4():
    return sym.sqrt(1+x**2)


def x_0(i):
    arr = [1, sym.pi/4, 1, 5]
    return arr[i]
