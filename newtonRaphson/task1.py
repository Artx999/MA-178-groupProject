# Import libraries and Newton Raphsons Method
from newtonFunction import *


# Define function f
def f():
    return 3*x**2 + 4*x - 4


# Asking for input
x0 = float(input("Enter x_0: "))
iterations = int(input("Enter number of maximum iterations allowed: "))

# Using Newton Raphsons Method
newtonRaphson(f, x0, 10**-12, iterations)
