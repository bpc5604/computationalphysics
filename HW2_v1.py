"""
HW 2
Blake Cole
1-16-20
"""

"""
Problem 1: Quadratic Equation
Method: 
*note the different versions of the equation end up reversing the negative and positive solutions, 
I think this is because of the way python is calculating square roots, in one case the numerator includes a square root,
in the other the denominator includes a square root
"""
import numpy as np
import matplotlib.pyplot as plt

print("==============")
print("Problem 1:")

a=.001    
b=1000
c=.001

def quadratic(a,b,c):       ##version 1 of the quadratic equation
	
	pos_solution=(-b + np.sqrt(b**2 - 4*a*c))/(2*a)       
	neg_solution=(-b - np.sqrt(b**2 - 4*a*c))/(2*a)
	print("Positive Solution:",pos_solution) 
	print("Negative Solution:",neg_solution)

def quadraticv2(a,b,c):    ##version 2 of the quadratic equation
	pos1_solution=(2*c)/(-b + np.sqrt(b**2-4*a*c))
	neg1_solution=(2*c)/(-b - np.sqrt(b**2-4*a*c))
	print("Positive Solution:",pos1_solution)
	print("Negative Solution:",neg1_solution)
	
quadratic(a,b,c)
quadraticv2(a,b,c)

"""
Problem 2:Calculating Derivatives
Method: define several loops which calculate derivative with increasing precision
Python begins to round at large decimal values which causes it to become inaccurate

*note this method takes a WHILE to run when delta gets small since it's calculating millions of values,
so I wrote a second function deriv_v2 which calculates at the given delta value instead of looping down to it
"""
print("==============")
print("Problem 2:")

delta=1  			##define delta variable which results in precision of derivation calculation
x=1

def derivative1(x,delta):
	def function(x):
		return x*(x-1)
	while delta>=10**-4:        ##stop the loop once delta reaches the nominal value
		answer=(function(x + delta) - function(x))/delta
		delta -= 10**-5     ##incrimenting value should be less than the delta function
	print(answer)
def derivative2(x,delta):
	def function(x):
		return x*(x-1)
	while delta>=10**-6:        ##stop the loop once delta reaches the nominal value
		answer=(function(x + delta) - function(x))/delta
		delta -= 10**-7     ##incrimenting value should be less than the delta function
	print(answer)


def f(x):
	return x**2-x
def deriv_v2(x,delta):      ##defining 'version 2' of the derivative which calculates a single value 
	deriv=(f(x + delta) - f(x))/delta
	print(deriv)
deriv_v2(1,10**-6)     ##calling v2 of the deriv function given values of delta
deriv_v2(1,10**-8)
deriv_v2(1,10**-10)
deriv_v2(1,10**-12)
deriv_v2(1,10**-14)



derivative1(x,delta)    ##calling version 1 of the deriv function which loops through values of delta
derivative2(x,delta)



"""
Problem 3: Wave Interference
Method: create a meshgrid, calculate sin waves and sum them, plot using contour plot for visual density
"""
print("==============")
print("Problem 3:")



lam=5        ##wavelength of 5cm
amp=1  		##amplitude of 1cm
k=2*np.pi/lam       ##wave vector 


x1=-10    ##define the centers at 10,-10 so they are 20cm apart
x2=10

y1=0     ##along the x-axis
y2=0

x=np.linspace(-50,50,num=500)    ##define 500 points ranging from -50cm to 50cm for a total of 1m 
X,Y=np.meshgrid(x,x)             ##create an x,y grid out of these points 

r1=np.sqrt((X-x1)**2 + (Y-y1)**2)       ##calculate r1 and r2 using the grid values and defined centers
r2=np.sqrt((X-x2)**2 + (Y-y2)**2)

wave1= amp*np.sin(k*r1)         ##create the sin waves
wave2= amp*np.sin(k*r2)
wavetotal=wave1 + wave2        ##sum the sin waves for a total

plt.contourf(X,Y,wavetotal)
plt.title("Sin Wave Summation for Water Droplets")       
plt.show()









