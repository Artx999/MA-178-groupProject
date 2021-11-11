def nraphson(fn, dfn, x, tol, maxiter):
    for i in range(maxiter):
        xnew = x - fn(x) / dfn(x)
        if abs(xnew - x) < tol: break
        x = xnew
    return xnew, i


y = lambda x: 3 * x ** 2 + 4 * x - 4
dy = lambda x: 6 * x + 4
# y, dy, x0 gjetting, feiltoleranse oghvor mange ganger den skal kjøre
x, n = nraphson(y, dy, 1, 0.000000000001, 100)
print("svaret er %.20f etter å ha gjettet %d ganger" % (x, n))
