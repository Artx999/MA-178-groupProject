from newtonFunction import *


def f(o1):
    return (-2 * sym.sin(o1) - (17 / 2) * sym.sin(x) + 6) ** 2 + (
            -(17 / 2) * sym.cos(x) - 2 * sym.cos(o1) + 10) ** 2 - 49


def f1():
    return f(0)


def f2():
    return f(sym.pi / 2)


def f3():
    return f(sym.pi)


def tasks(index):
    arr = ["a", "b", "c"]
    return arr[index]


count = 0
for i in [f1, f2, f3]:
    count += 1
    radArr = []
    degArr = []
    for j in range(-10, 10):
        a = newtonRaphson(i, j, 10 ** -12, 1000, False)

        while a > 2 * sym.pi or a < 0:
            if a > 2 * sym.pi:
                a -= 2 * sym.pi
            else:
                a += 2 * sym.pi
        rad = round(a, 9)
        deg = round(a*180/sym.pi, 9)
        if rad not in radArr:
            radArr.append(rad)
            degArr.append(deg)

    print(tasks(count - 1) + ") This translates to: " + str(radArr) + " in radians, which is " +
          str(degArr) + " in degrees, for the definition area [0, 2pi]")
