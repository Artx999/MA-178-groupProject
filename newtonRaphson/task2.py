from newtonFunction import *


def f(o1):
    return (-2*sym.sin(o1) - (17/2)*sym.sin(x) + 6)**2 + (-(17/2)*sym.cos(x) - 2*sym.cos(o1) + 10)**2 - 49


def f1():
    return f(0)


x0 = float(input("Enter x_0: "))
iterations = int(input("Enter number of maximum iterations allowed: "))


for i in range(10):
    a = newtonRaphson(f1, x0, 10 ** -12, iterations)

    while a > 2*sym.pi or a < 0:
        if a > 2*sym.pi:
            a -= 2*sym.pi
        else:
            a += 2*sym.pi

    print("This translates to: " + str(round(a, 5)) + " in radians for the definition area [0, 2pi]")

    x0 += 1
