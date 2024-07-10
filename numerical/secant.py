# 0.95*x*3-5.9*x*2+10.9*x-6 , x-1= 2.5 , x0 = 3.5 , eps= 0.5

import sympy as sp

def secant(func, xmin, xi, eps=1, maxiter=100):
    x =sp.symbols('x')
    f =sp.sympify(func)

    iteration=0
    xipls=0
    error=100
    while error>eps and iteration<maxiter:
        xipls=xi - ((f.subs(x,xi)*(xmin-xi))/(f.subs(x,xmin)-f.subs(x,xi)))
        error=abs((xi-xmin)/xi)*100
        print("iteration= ",iteration,"|xi-1= ",xmin,"|f(xi-1)= ",f.subs(x,xmin),"|xi= ",xi,"|f(xi)= ",f.subs(x,xi),"ERROR= ",error,"%")
        iteration += 1
        xmin=xi
        xi=xipls
    return xi

# Input function from the user
func_str = input("Enter the function: ")
xmin=float(input("Enter Xi-1: "))
xi=float(input("Enter X0: "))
eps=float(input("Enter Error%: "))

root=secant(func_str,xmin,xi,eps)
print(f"ROOT= {root}")