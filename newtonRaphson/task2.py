from newtonFunction import *


def f(o1):
    return (-2*sym.sin(o1) - (17/2)*sym.sin(x) + 6)**2 + (-(17/2)*sym.cos(x) - 2*sym.cos(o1) + 10)**2 - 49


def f1():
    return f(0)


newtonRaphson(f1, 10, 10**-12, 1000)
