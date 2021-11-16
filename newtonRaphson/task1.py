import sympy as sym

x = sym.Symbol('x')


# Define function f
def f(x):
    return 3 * x ** 2 + 4 * x - 4


# Define the differentiation of f, called g
def g(x):
    return 6 * x + 4


# Define a function/algorithm for Newton Raphsons Method
def newtonRaphson(xn, E, n):
    print("NEWTON RAPHSONs METHOD\n")
    count = 1

    while True:
        if g(xn) == 0.0:
            print("Cannot divide by 0\n")
            break

        xn1 = xn - f(xn) / g(xn)
        print("Iteration %i: x_%i = %0.12f and f(x_%i) = %0.12f" % (count, count, xn1, count, f(xn1)))
        xn = xn1
        count += 1
        if count > n:
            print("Reached the maximum amount of iterations")
            break

        if not abs(f(xn1)) > E:
            break

    print("Konvergerer mot: %0.12f\n" % xn1)


# Asking for input
x0 = float(input("Enter x_0: "))
iterations = int(input("Enter number of maximum iterations allowed: "))

# Starting Newton Raphsons Method
newtonRaphson(x0, 10 ** -12, iterations)
