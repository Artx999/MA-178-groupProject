from functions import *

# Task 2

# Task a
count = 0
for i in [f_1(), f_2(), f_3(), f_4()]:
    count += 1
    xAxis = np.linspace(interval(count - 1)[0], interval(count - 1)[1], 100)
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
    xAxis = np.linspace(interval(count - 1)[0], interval(count - 1)[1], 100)
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
    count += 1
    dx = 0.1
    diff = sym.simplify(sym.diff(i))
    xAxis = np.linspace(interval(count - 1)[0], interval(count - 1)[1], 100)
    yAxis = []
    for j in xAxis:
        yAxis.append((i.evalf(subs={x: j + dx}) - i.evalf(subs={x: j})) / dx)
    plt.plot(xAxis, yAxis, label="g_" + str(count) + "(" + str(dx) + ")")
plt.xlabel("x")
plt.ylabel("y")
plt.legend(loc="upper right")
plt.show()
print("Generated plots for task c")
