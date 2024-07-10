# -0.6 * pow(x, 2) + 2.4 * x + 5.5
import sympy as sp

def bisect(func,xl,xu,eps,max_iter=100):
    x = sp.symbols('x')
    f = sp.sympify(func)

    if f.subs(x,xl)*f.subs(x,xu) < 0:
        
        iteration = 0
        xr = 0
        xrold = 0
        error = 100
        while error > eps and iteration < max_iter:
            xrold = xr
            xr =(xl+xu)/2
            error = abs((xr - xrold) / xr) * 100
            if iteration == 0:
                print("iteration= ", iteration, "|xl= ", xl, "|f(xl)= ", f.subs(x, xl), "|xu= ", xu, "|f(xu)= ", f.subs(x, xu), "|xr= ", xr, "|f(xr)= ", f.subs(x, xr), "ERROR= ", "_")
            else:
                print("iteration= ", iteration, "|xl= ", xl, "|f(xl)= ", f.subs(x, xl), "|xu= ", xu, "|f(xu)= ", f.subs(x, xu), "|xr= ", xr, "|f(xr)= ", f.subs(x, xr), "ERROR= ", error, "%")
            if f.subs(x, xl) * f.subs(x, xr) < 0:
                xu = xr
            else:
                xl = xr
            iteration += 1
        return xr
    else:
        print('Please enter valid values.')
        fn, xl, xu, eps = get_input()
        root = bisect(fn, xl, xu, eps)
        print(f"ROOT= {root}")

def get_input():
    fn = input("Enter the function: ")
    xl = float(input("Enter XL: "))
    xu = float(input("Enter XU: "))
    eps = float(input("Enter the error: "))
    return fn, xl, xu, eps

xx, cc, bb, ww = get_input()
root = bisect(xx, cc, bb, ww)
print(f"ROOT= {root}")