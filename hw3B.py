"""
Problem 1: Low pass filter
Method:
1. integrate over t
2. plug in rc
3.

"""
import numpy as np
import matplotlib.pyplot as plt
import math


def vin(t):
    if (math.floor(2*t) % 2 ==0):  ## rounds down to nearest whole, if even
        return 1
    else:
        return -1     ##if odd

def function_to_int(RC,vout,t):  ###(a,b,h)
    return (1/RC)*(vin(t)-vout)



def filter_fun(a,b,RC,y,n ):   ##uses RK 4th order to integrate
    #def RKfour(a,b,RC,y,n,vin,vout):
        vout_n=[0]   ### creates list to populate with initial value=0
        t_n=[a]  ##first value in t list is initial value to start from (independent variable)
        h=(b-a)/n    ##evenly spaced step size
        while t_n[-1] < b:   ##iterates from initial_t a->b
            k_1= h*function_to_int(RC,vout_n[-1],t_n[-1])
            k_2= h*function_to_int(RC,vout_n[-1] + k_1/2, t_n[-1] + h/2)
            k_3= h*function_to_int(RC,vout_n[-1] + k_2/2, t_n[-1] + h/2)
            k_4= h*function_to_int(RC,vout_n[-1] + k_3, t_n[-1] + h)
            #y=x_n[0] + h*function(x_n[-1],t_n[-1])     ##calculate the next approximate value in the function (then append to list in a later line)
            t_n.append(t_n[-1]+h)    ##add a value to the t list with the latest value plus the slice width, stepping
            vout_n.append(vout_n[-1] + (k_1 + 2*k_2 + 2*k_3 + k_4)/6)        ##append the list with the calculated value
        plt.plot(t_n,vout_n)
        plt.title("R-K 4th order")
        plt.show()
filter_fun(0,10,.001,function_to_int,50000)
plt.show()
