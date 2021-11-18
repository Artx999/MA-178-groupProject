import sympy as sym

x = sym.Symbol('x')


# Define a function/algorithm for Newton Raphsons Method
def newtonRaphson(function, startingValue, errorTolerance, maxIterations):
    print("NEWTON RAPHSONs METHOD\n")
    count = 1
    f = function()
    g = sym.diff(f)
    newValue = 0

    while True:
        if g.evalf(subs={x: startingValue}) == 0.0:
            print("Cannot divide by 0\n")
            break

        newValue = startingValue - f.evalf(subs={x: startingValue}) / g.evalf(subs={x: startingValue})
        print("Iteration %i: x_%i = %0.12f and f(x_%i) = %0.12f" % (count, count, newValue, count, g.evalf(subs={x: newValue})))
        startingValue = newValue
        count += 1
        if count > maxIterations:
            print("Reached the maximum amount of iterations")
            break

        if not abs(f.evalf(subs={x: newValue})) > errorTolerance:
            break

    print("Converges to: %0.12f\n" % newValue)

    return newValue
