import matplotlib.pyplot as plt
import numpy as np
import math
"""
HW2b
Blake Cole
1/23/2020
"""
"""
Problem1: Integrate and plot bessel functions
Method:
1.define bessel function equation ((function of theta,m,x))
2.integrate the function from 0-pi with respect to theta
    a. we have three equations to integrate m=0,1,2
    b. for all of these x=0-20
3. for one m value, integrate over a->b (theta) AND loop through x=0->20
"""

m0=0     ##define J_m values to use later
m1=1
m2=2

def bessel_fun(theta,m,x):
    f= math.cos(m*theta - x*math.sin(theta))     ##returns a function
    return f

def bessel_integrate(a,b,m,x,n):                ##integration routine which also stores m,x values
    h=(b-a)/n
    #sum=f(a)+f(b)
    sum=bessel_fun(a,m,x)+bessel_fun(b,m,x)      ##integrating over theta!

    i=0
    e_sum=o_sum=0
    for i in np.arange(1,n,2):    ##odd range
        o_sum+=bessel_fun(a + h*i,m,x)
        i+=1
    for i in np.arange(2,n,2):    ##even range
        e_sum+=bessel_fun(a + h*i,m,x)
        i+=1
    integrand=sum + 4*o_sum + 2*e_sum
    total=integrand*(h/3)
    return total
    print(total)

y1data=[]     ##lists to store bessel functions 0,1,2
y2data=[]
y3data=[]
xdata=[]
for i in np.arange(0,20,.1):      ##loop through x=0->20 with a small step size
    data1=bessel_integrate(0,np.pi,m0,i,1000)   ##call the integrate functions from theta=0->pi
    data2=bessel_integrate(0,np.pi,m1,i,1000)   ## for the 3 separate bessel functions
    data3=bessel_integrate(0,np.pi,m2,i,1000)
    y1data.append(data1)       ##add the data the lists
    y2data.append(data2)
    y3data.append(data3)
    xdata.append(i)
#print(ydata)    ##print statement for debugging

plt.plot(xdata,y1data)        ##plot x,y
plt.plot(xdata,y2data)
plt.plot(xdata,y3data)

plt.title("J_0,J_1,J_2 Bessel Functions")
plt.show()
