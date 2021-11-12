from functions import *

# Task 1
print("Task 1")
count = 0
for i in [f_1(), f_2(), f_3(), f_4()]:
    count += 1
    print("f_" + str(count) + "(x)=", i)
    xAxis = np.linspace(interval(count - 1)[0], interval(count - 1)[1], 100)
    yAxis = []
    for j in xAxis:
        yAxis.append(i.evalf(subs={x: j}))
    plt.plot(xAxis, yAxis, label="f_" + str(count) + "(x)")
plt.xlabel("x")
plt.ylabel("y")
plt.legend(loc="upper right")
plt.show()
print("\n")

# Task a
print("Task a)")
count = 0
for i in [f_1(), f_2(), f_3(), f_4()]:
    count += 1
    diff = sym.diff(i)
    print("f_" + str(count) + "'(x)=", sym.simplify(diff))
print("\n")

# Task b
print("Task b)")
count = 0
for i in [f_1(), f_2(), f_3(), f_4()]:
    count += 1
    dx = 0.1
    diff = sym.diff(i)
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
range = 0
for i in [f_1(), f_2(), f_3(), f_4()]:
    truePath = False
    nextFunc = False
    count = 2
    range += 1
    f = 0.001
    dx = 0.1
    diff = sym.diff(i).evalf(subs={x: x_0(range - 1)})
    while not nextFunc:
        g = (i.evalf(subs={x: x_0(range - 1) + dx}) - i.evalf(subs={x: x_0(range - 1)})) / dx
        E = abs(diff - g)

        if E > f:
            if truePath:
                dx = dx - 1/(10**count)
                nextFunc = True
            if not nextFunc:
                dx = dx / 10
                count += 1
        if E < f and not nextFunc:
            dx = dx + 1/(10**count)
            truePath = True
    print("dx_" + str(range) + " = " + str(round(dx, 10)))
