import sympy as sym

from functions import *

# Task 1
print("Task 1")
count = 0
for i in [f_1(), f_2(), f_3(), f_4()]:
    count += 1
    print("f_" + str(count) + "(x)=", i)
print("\n")

# Task a
print("Task a)")
count = 0
for i in [f_1(), f_2(), f_3(), f_4()]:
    count += 1
    diff = sym.diff(i)
    print("f_" + str(count) + "'(x)=", sym.simplify(diff))
print("\n")

# Task a
print("Task b)")
count = 0
for i in [f_1(), f_2(), f_3(), f_4()]:
    count += 1
    diff = sym.diff(i)
    print("f_" + str(count) + "'(" + str(x_0(count - 1)) + ")=", diff.evalf(subs={x: x_0(count - 1)}))
