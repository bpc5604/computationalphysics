"""
Problem 1: Low pass filter
Method:
1. integrate over t
2. plug in rc
3.

"""

def vin(t):
    if:  even return 1
    else: its odd return -1

def function_to_int(RC,vout):  ###(a,b,h)
    return (1/RC)*(vin(t)-vout)



integrate function(a,b,RC, )
    def RKfour(a,b,RC,y,n,vin,vout):
        x_n=[0]   ### creates list to populate with initial value=0
        t_n=[a]  ##first value in t list is initial value to start from (independent variable)
        h=(b-a)/n    ##evenly spaced step size
        while t_n[-1] < b:   ##iterates from initial_t a->b
            k_1= h*function(RC,x_n[-1],t_n[-1])
            k_2= h*function(RC,x_n[-1] + k_1/2, t_n[-1] + h/2)
            k_3= h*function(RC,x_n[-1] + k_2/2, t_n[-1] + h/2)
            k_4= h*function(RC,x_n[-1] + k_3, t_n[-1] +h)
            #y=x_n[0] + h*function(x_n[-1],t_n[-1])     ##calculate the next approximate value in the function (then append to list in a later line)
            t_n.append(t_n[-1]+h)    ##add a value to the t list with the latest value plus the slice width, stepping
            x_n.append(x_n[-1] + (k_1 + 2*k_2 + 2*k_3 + k_4)/6)        ##append the list with the calculated value
        plt.plot(t_n,x_n)
        plt.title("R-K 4th order")
        plt.show()
    RKfour(0,10,0.01,function,50)
    plt.show()
