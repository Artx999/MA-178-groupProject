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
    diff = sym.simplify(sym.diff(i))
    print("f_" + str(count) + "'(x)=", diff)
print("\n")

# Task b
print("Task b)")
count = 0
for i in [f_1(), f_2(), f_3(), f_4()]:
    count += 1
    dx = 0.1
    diff = sym.simplify(sym.diff(i))
    g = (i.evalf(subs={x: x_0(count - 1) + dx}) - i.evalf(subs={x: x_0(count - 1)}))/dx
    print("f_" + str(count) + "'(" + str(x_0(count - 1)) + ")=", diff.evalf(subs={x: x_0(count - 1)}))
    print("g_" + str(count) + "(" + str(x_0(count - 1)) + ")=", g)
print("\n")

# Task c
print("Task c)")
count = 0
for i in [f_1(), f_2(), f_3(), f_4()]:
    count += 1
    dx = 0.1
    diff = sym.diff(i)
    g = (i.evalf(subs={x: x_0(count - 1) + dx}) - i.evalf(subs={x: x_0(count - 1)}))/dx
    print("E_" + str(count) + "'(" + str(x_0(count - 1)) + ")=", abs(diff.evalf(subs={x: x_0(count - 1)}) - g))
print("\n")

# Task d
print("Task d)")
count = 0
for i in [f_1(), f_2(), f_3(), f_4()]:
    truePath = False
    nextFunc = False
    degree = 2
    count += 1
    f = 0.001
    dx = 0.1
    diff = sym.diff(i).evalf(subs={x: x_0(count - 1)})
    while not nextFunc:
        g = (i.evalf(subs={x: x_0(count - 1) + dx}) - i.evalf(subs={x: x_0(count - 1)})) / dx
        E = abs(diff - g)

        if E > f:
            if truePath:
                dx = dx - 1/(10**degree)
                nextFunc = True
            if not nextFunc:
                dx = dx / 10
                degree += 1
        else:
            dx = dx + 1/(10**degree)
            truePath = True
    print("dx_" + str(count) + " = " + str(dx))
