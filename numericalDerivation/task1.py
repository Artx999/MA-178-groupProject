import sympy as sym

from functions import *

count = 0
for i in [f_1(), f_2(), f_3(), f_4()]:
    count += 1
    diff = sym.diff(i)
    print("f_" + str(count) + "(x)=", i)
    print("f_" + str(count) + "'(x)=", sym.simplify(diff))
    print("f_" + str(count) + "'(" + str(x_0(count - 1)) + ")=", diff.evalf(subs={x: x_0(count - 1)}))
    print("\n")
