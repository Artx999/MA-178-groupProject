from functions import *

# Task 2

# Task a
count = 0
for i in [f_1(), f_2(), f_3(), f_4()]:
    count += 1
    xAxis = np.linspace(interval(count - 1)[0], interval(count - 1)[1], 1000)
    yAxis = []
    for j in xAxis:
        yAxis.append(i.evalf(subs={x: j}))
    plt.plot(xAxis, yAxis, label="f_" + str(count) + "(x)")
plt.xlabel("x")
plt.ylabel("y")
plt.legend(loc="upper right")
plt.show()
print("Generated plots for task a")

# Task b
count = 0
for i in [f_1(), f_2(), f_3(), f_4()]:
    count += 1
    diff = sym.simplify(sym.diff(i))
    xAxis = np.linspace(interval(count - 1)[0], interval(count - 1)[1], 1000)
    yAxis = []
    for j in xAxis:
        yAxis.append(diff.evalf(subs={x: j}))
    plt.plot(xAxis, yAxis, label="f_" + str(count) + "'(x)")
plt.xlabel("x")
plt.ylabel("y")
plt.legend(loc="upper right")
plt.show()
print("Generated plots for task b")

# Task c
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
                dx = dx - 1/(10**(degree + 1))
                nextFunc = True
            if not nextFunc:
                dx = dx / 10
                degree += 1
        else:
            dx = dx + 1/(10**(degree + 1))
            truePath = True
    dxRounded = round(dx, degree)

    xAxis = np.linspace(interval(count - 1)[0], interval(count - 1)[1], 1000)
    yAxis = []
    for j in xAxis:
        yAxis.append((i.evalf(subs={x: j + dxRounded}) - i.evalf(subs={x: j})) / dxRounded)
    plt.plot(xAxis, yAxis, label="g_" + str(count) + "(x)")
plt.xlabel("x")
plt.ylabel("y")
plt.legend(loc="upper right")
plt.show()
print("Generated plots for task c")

# Task d
count = 0
for i in [f_1(), f_2(), f_3(), f_4()]:
    truePath = False
    nextFunc = False
    degree = 2
    count += 1
    f = 0.001
    dx = 0.1
    diff = sym.simplify(sym.diff(i))
    diffVal = sym.diff(i).evalf(subs={x: x_0(count - 1)})
    while not nextFunc:
        g = (i.evalf(subs={x: x_0(count - 1) + dx}) - i.evalf(subs={x: x_0(count - 1)})) / dx
        E = abs(diffVal - g)

        if E > f:
            if truePath:
                dx = dx - 1 / (10 ** (degree + 1))
                nextFunc = True
            if not nextFunc:
                dx = dx / 10
                degree += 1
        else:
            dx = dx + 1 / (10 ** (degree + 1))
            truePath = True
    dxRounded = round(dx, degree)

    xAxis = np.linspace(interval(count - 1)[0], interval(count - 1)[1], 1000)
    yAxis = []
    for j in xAxis:
        yAxis.append(abs(((i.evalf(subs={x: j + dxRounded}) - i.evalf(subs={x: j})) / dxRounded) - diff.evalf(subs={x: j})))
    plt.subplot(2, 2, count)
    plt.plot(xAxis, yAxis, label="E_" + str(count) + "(x)")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend(loc="upper right")
plt.show()
print("Generated plots for task d")
