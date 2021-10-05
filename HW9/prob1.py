"""
Blake Cole
HW 9
Ising Model
"""


import matplotlib.pyplot as plt
import numpy as np
import random


n=5  ##size of grid
J=2 ##positive interaction constant


grid=2*np.random.randint(0,2,size=(n+1,n+1))-1    ##creates random grid of -1,1 of shape nxn

print(grid)
sysenergy=[]
for i in range(n):
    for j in range(n):
        si=grid[i,j]
        adl=grid[i-1,j]  ##particle to the left
        adr=grid[i+1,j]  ##spin to the right
        adu=grid[i,j+1]  ##spin adjacent above
        add=grid[i,j-1]  ##spin adjacent below

        #sysenergy=-J*np.cumsum(si*adl*adr*adu*add)
        sysenergy.append(-J*(si*adl*adr*adu*add))

#print(np.sum(sysenergy))
Ei=np.sum(sysenergy)
rand=np.random.randint(0,n)
#print(rand)

for i in range(n):
    for j in range(n):
        gridj=grid
        gridj[i,j]=grid[rand,rand]*-1  ##randomly flip some spins
print(gridj)
#Edif=Ej-Ei
