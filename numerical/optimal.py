import sympy as sp
import math as m

def Gradiant(func, x, y):
    x ,y =sp.symbols('x y')   
    f=sp.sympify(func)
    fdashx=sp.diff(f,x)
    print("f':",fdashx)
    fdashy=sp.diff(f,y)
    print("f':",fdashy)
    p=fdashx.subs({x:xo , y:yo})

    k=fdashy.subs({x:xo , y:yo})
    gradiant=str(p) +"i" + str(k)+"j"
    print("gradiant =",gradiant)
    
    magnitude=((p**2)+(k**2))**0.5
    print("magnitude = ", magnitude)
    cyta=m.degrees(m.atan(yo/xo))
    if cyta <0:
        cyta = 180+cyta
    else :
        cyta = cyta
    print("cyta=",cyta)
  

def Hessians(func, x, y):
    x ,y =sp.symbols('x y')   
    f=sp.sympify(func)
    fdashx=sp.diff(f,x) #2y+2-2x
    fdashx2=sp.diff(fdashx,x) #0+0-2
    fdashy=sp.diff(f,y) # 2x-4y
    fdashy2=sp.diff(fdashy,y) #0-4
    fdash2xy=sp.diff(fdashy,x)
    fdash2yx=sp.diff(fdashx,y)
    print("d**2*f/d*x**2=",fdashx2)
    print("d**2*f/d*y**2=",fdashy2)
    print("d**2*f/d*x*d*y=",fdash2xy)
    print("d**2*f/d*y*d*x=",fdash2yx)
    H=[[fdashx2,fdash2yx],
       [fdash2xy,fdashy2]]
    detaH=(H[0][0]*H[1][1])-(H[0][1]*H[1][0])
    if detaH>0:
        if H[0][0] >0 :
            localMIN=H[0][0]
            print("local min=",localMIN)
        elif H[0][0] <0 :
            localMAX=H[0][0]
            print("local max =", localMAX)
    elif detaH<0 :
        print("has no sadle point")
        
    
    
fuc_str=input("Enter Function: ")
xo= float(input("Enter x: "))
yo= float(input("Enter y: "))
Gradiant(fuc_str,xo,yo)
Hessians(fuc_str, xo, yo)
