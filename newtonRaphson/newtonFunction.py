# You can include this file to access the function/algorithm for Newton Raphsons Method
# By including this file, you also get access too the necessary libraries
import sympy as sym

x = sym.Symbol('x')


# Define a function/algorithm for Newton Raphsons Method
def newtonRaphson(function, startingValue, errorTolerance, maxIterations, doPrint=True):
    count = 1
    # Get function and the derivative
    f = function()
    g = sym.diff(f)
    newValue = 0

    while True:
        # Check for problems with division by zero
        if g.evalf(subs={x: startingValue}) == 0.0:
            print("Cannot divide by 0\n")
            break
        # Get x_n+1
        newValue = startingValue - f.evalf(subs={x: startingValue}) / g.evalf(subs={x: startingValue})
        # Only print if wanted
        if doPrint:
            # Print info about iteration
            print("Iteration %i: x_%i = %0.12f and f(x_%i) = %0.12f" % (count, count, newValue, count, g.evalf(subs={x: newValue})))
        startingValue = newValue
        count += 1
        # Check if the algorithm has reached the max amount of allowed iterations
        if count > maxIterations:
            print("Reached the maximum amount of iterations")
            break

        # CHeck if the value is within the tolerated error
        if not abs(f.evalf(subs={x: newValue})) > errorTolerance:
            break

    # If wanted, print the result
    if doPrint:
        print("Converges to: %0.12f\n" % newValue)

    return newValue
