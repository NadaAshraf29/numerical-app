# -2 + 6 * x - 4 * pow(x, 2) + .5 * pow(x, 3)
#x0 = 1
#eps = 0.5
import sympy as sp

def newton(func, xi, eps, max_iter=100):
    x=sp.symbols('x')
    f=sp.sympify(func)
    fdash=sp.diff(f)
    print("f':",fdash)
    iteration=0
    xipls=0
    error=100.00
    print('Iteration: ',iteration, 'xi: ', xi, 'F(xi): ', f.subs(x,xi), "f'(xi)", fdash.subs(x,xi), 'Error: ', "_")
    iteration+=1
    while error >= eps and iteration < max_iter:
        xipls=xi-(f.subs(x,xi)/fdash.subs(x,xi))
        error=abs((xipls-xi)/xipls)*100
        xi=xipls
        print('Iteration: ',iteration, 'xi: ', xi, 'F(xi): ', f.subs(x,xi), "f'(xi)", fdash.subs(x,xi), 'Error: ', error)
        iteration += 1
        
    return xi


fuc_str=input("Enter Function: ")
xi= float(input("Enter x0: "))
eps= float(input("Enter Error: "))

root=newton(fuc_str,xi,eps)
print(f"ROOT= {root}")