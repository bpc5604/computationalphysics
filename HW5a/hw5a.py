"""
Blake Cole
HW5a
Quantum Oscillator
"""

import numpy as np
import matplotlib.pyplot as plt


"""
[-h^2/2m dd/dx^2 + v(x)]Y =E Y
dY/dx=Q  dQ/dx=2m/h^2(V(x)-E)Y
"""
"""
I havent finished this program,
currently the energy value returned
is much too large
"""




m=9.1094e-31
hbar=1.0546e-34
e=1.6022e-19
L=5.2918e-11
a=10e-11
L=20*a
N=1000
h=a/N



def V(x):
    v=50   ##V0=50eV
    a=10e-11
    return v*(x**2)/(a**2)



def difeq(r,x,E):
    Y=r[0]
    Q=r[1]
    dY=Q
    dQ=(2*m/(hbar**2))*(V(x)-E)*Y
    return np.array([dY,dQ],dtype=np.longdouble)  ##had to use long double because of the small numbers

def solve(E):
    Y=0.0
    Q=1.0
    r=np.array([Y,Q],dtype=np.longdouble)

    for x in np.arange(0,L,h):     ##Runga Kutta 4th order method
        k1=h*difeq(r,x,E)
        k2=h*difeq(r + 0.5*k1, x + 0.5*h,E)
        k3=h*difeq(r+0.5*k2, x+0.5*h,E)
        k4=h*difeq(r+k3, x + h,E)
        r += (k1 + 2*k2 + 2*k3 +k4)/6
    return r[0]
E1=0.0
E2=e
Y2=solve(E1)
target=e/1000

while abs(E1-E2)>target:
    Y1,Y2=Y2,solve(E2)
    E1,E2=E2,E2-Y2*(E2-E1)/(Y2-Y1)
print("E=",E2/e,"eV")
