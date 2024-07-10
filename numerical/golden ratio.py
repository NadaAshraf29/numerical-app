import sympy as sp
def determinMax(func,xl,xu,site):
    x = sp.symbols('x')
    f = sp.sympify(func)
    gr = ((5**0.5)- 1) / 2  # Golden ratio
    d = gr * (xu - xl)  # Initial distance
    x1 = xu - d  # First trial point
    x2 = xl + d  # Second trial point
    iteration = 1
    print("iteration= ",iteration,"|xl= ",xl,"|f(xl)= ",f.subs(x,xl),"|xu= ",xu,"|f(xu)= ",f.subs(x,xu),"|x1= ",x1,"|f(x1)= ",f.subs(x,x1),"|x2= ",x2,"|f(x2)= ",f.subs(x,x2),"|d= ",d,"\n")         
    while iteration < site :
        iteration +=1
        if(f.subs(x,x1)<f.subs(x,x2)) :
            xu=x1
            x1=x2
        else :
            xl=x2
            x2=x1
        d = gr * (xu - xl)  # Initial distance
        x1 = xu - d  # First trial point
        x2 = xl + d  # Second trial point
         
        print("iteration= ",iteration,"|xl= ",xl,"|f(xl)= ",f.subs(x,xl),"|xu= ",xu,"|f(xu)= ",f.subs(x,xu),"|x1= ",x1,"|f(x1)= ",f.subs(x,x1),"|x2= ",x2,"|f(x2)= ",f.subs(x,x2),"|d= ",d,"\n")       
    if (x1 > x2):
        max=x1
    else :
        max=x2    
    return max


def determinMin(func,xl,xu,site):
    x = sp.symbols('x')
    f = sp.sympify(func)
    gr = ((5**0.5)- 1) / 2  # Golden ratio
    d = gr * (xu - xl)  # Initial distance
    x1 = xu - d  # First trial point
    x2 = xl + d  # Second trial point
    iteration = 1
    print("iteration= ",iteration,"|xl= ",xl,"|f(xl)= ",f.subs(x,xl),"|xu= ",xu,"|f(xu)= ",f.subs(x,xu),"|x1= ",x1,"|f(x1)= ",f.subs(x,x1),"|x2= ",x2,"|f(x2)= ",f.subs(x,x2),"|d= ",d,"\n")         
    while iteration < site :
        iteration +=1
        if(f.subs(x,x1)<f.subs(x,x2)) :
            xl=x2
            x2=x1
            
        else :
            xu=x1
            x1=x2
        d = gr * (xu - xl)  # Initial distance
        x1 = xu - d  # First trial point
        x2 = xl + d  # Second trial point
         
        print("iteration= ",iteration,"|xl= ",xl,"|f(xl)= ",f.subs(x,xl),"|xu= ",xu,"|f(xu)= ",f.subs(x,xu),"|x1= ",x1,"|f(x1)= ",f.subs(x,x1),"|x2= ",x2,"|f(x2)= ",f.subs(x,x2),"|d= ",d,"\n")       
    if (x1 < x2):
        min=x1
    else :
        min=x2    
    return min



#MAIN CODE
choice=0
while choice != 3:
    print ("choose from menue")
    print("1 determine max")
    print("2 determine min")
    choice= int(input())
    
    if choice== 1 or choice == 2 :
        # Input function from the user
        func_str = input("Enter the function: ")
        xl=float(input("Enter Xl: "))
        xu=float(input("Enter Xu: "))
        site=float(input("Enter stop iteration: "))

        if choice == 1 :
            
            root=determinMax(func_str,xl,xu,site)
            print(f"the maximum value is= {root}")
        elif choice == 2:
        
            root=determinMin(func_str,xl,xu,site)
            print(f"the minimum vaule is= {root}")
        else :
             print("enter valid values")



