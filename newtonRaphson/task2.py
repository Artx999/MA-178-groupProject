# Import libraries and Newton Raphsons Method
from newtonFunction import *


# Define a function that expresses the relation between angele 1 and angle 2
def f(o1):
    return (-2 * sym.sin(o1) - (17 / 2) * sym.sin(x) + 6) ** 2 + (
            -(17 / 2) * sym.cos(x) - 2 * sym.cos(o1) + 10) ** 2 - 49


# Define a function for f, using the first value for angle 1
def f1():
    return f(0)


# Define a function for f, using the first value for angle 2
def f2():
    return f(sym.pi / 2)


# Define a function for f, using the first value for angle 3
def f3():
    return f(sym.pi)


# An array used for getting the names of the sub tasks
# The index corresponds to the (task number  - 1)
def tasks(index):
    arr = ["a", "b", "c"]
    return arr[index]


count = 0
for i in [f1, f2, f3]:
    count += 1
    # Defines arrays for storing radians and degrees
    radArr = []
    degArr = []
    # Checks 20 initial values between -10 and 10, to check if the method converges towards different values
    for j in range(-10, 10):
        # Using Newton Raphsons Method
        a = newtonRaphson(i, j, 10 ** -12, 1000, False)

        # Since the function is a trigonometric function, it will be periodic
        # It is therefore necessary to check if it is between the interval [0, 2*pi]
        # If not, subtract n*2*pi to get a value between the interval
        while a > 2 * sym.pi or a < 0:
            if a > 2 * sym.pi:
                a -= 2 * sym.pi
            else:
                a += 2 * sym.pi
        # Round the answer to 9 digits, giving the result in radians
        rad = round(a, 9)
        # Round the answer to 9 digits, giving the result in degrees
        deg = round(a*180/sym.pi, 9)
        # Check if the converged result has been found with another initial value
        if rad not in radArr:
            radArr.append(rad)
            degArr.append(deg)
    # Print the result with both radians and degrees
    print(tasks(count - 1) + ") This translates to: " + str(radArr) + " in radians, which is " +
          str(degArr) + " in degrees, for the definition area [0, 2pi]")
