
import sympy as sp
fn=input("ener fn")
x=sp.symbols("x")
f=sp.sympify(fn)
right=0
left=0
    # Get the degrees of the terms in the function
degrees = [sp.degree(term, gen=x) for term in f.as_ordered_terms()]
highest_power = max(degrees)
for term, degree in zip(f.as_ordered_terms(), degrees):
            # Get the the term of the highest power at different side of the function
        if degree == highest_power:
            left+=(term)
                # Get the coefficients of the terms and change the sign of it in the function
            expr_x = sp.collect(left, x)
            coefficients =sp.Poly(expr_x, x).coeffs()
            left= coefficients[0] * (-1)          
        else:
            right += (term)
    # Continue the simplify of the function
g=right/left      
gx=g**(1/highest_power)
    # user input
xo=float(input("enter x0"))
eps=float(input("enter eps"))

def simple(gx,xo,eps,max_iter=100):
    ggx=gx.subs(x,xo)
    error=100.00
    xipls=0
    iteration=0
    while error > eps and iteration < max_iter:
        if iteration==0:
            print('Iteration: ',iteration, 'xi: ', xo, 'F(xi): ', gx.subs(x,xo), 'Error: ', "---")
            
            
        else:
            xipls=gx.subs(x,xo)
            error=abs((xipls-xo)/xipls)*100
            xo=xipls
            print('Iteration: ',iteration, 'xi: ', xo, 'F(xi): ', gx.subs(x,xo), 'Error: ', error)  
       
        iteration += 1
        
    return xo

root=simple(gx,xo,eps)
print("root",root)