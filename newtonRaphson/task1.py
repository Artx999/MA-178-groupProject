from sympy import *

x = Symbol('x')

#Definere funksjon
def f(x):
    return 3*x**2 + 4*x - 4

#Definere deriverte av funksjonen
def g(x):
    return 6*x + 4

#Definere funksjonen NewtonRaphson
def newtonRaphson(x0, E):
    print("NEWTON RAPHSON's METODE\n")
    count = 1

    condition = True
    while condition:
        if g(x0) == 0.0:
            print("Kan ikke dele på 0\n")
            break

        x1 = x0 - f(x0) / g(x0)
        print("Iteration-%d, x1 = %0.12f and f(x1) = %0.12f" % (count, x1, f(x1)))
        x0 = x1
        count = count + 1

        condition = abs(f(x1)) > E


    print("Rooten er: %0.12f\n" % x1)


#Asking for x0
x0 = float(input('Enter Guess: '))

# Starting Newton Raphson Method
newtonRaphson(x0, 10**-12)
