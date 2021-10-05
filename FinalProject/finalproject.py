"""
Blake Cole
Large Brownian Motion Simulation:

The program creates random x,y coordinates between -20 and 20 for N particles.
Then begins a loop of adding -1 or 1 to the coordinates and animates the steps.
There is boundary for the particles defined near the borders.


Output: saves an mp4 file named animation using ffmpeg as the writer

"""


import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation
"""
particle in (x,y) can move either
up(0,1) down(0,-1)
left(0,-1) right(0,1)
"""

L=101
grid=np.zeros((L,L))    ##define working grid
min=-1   ##values for step size
max=1
fig,ax=plt.subplots()  ##initialize figure window

N=100    ##number of particles to create, can be set arbitrarily

randomlistx=[]  ##lists to store coordinates
randomlisty=[]
bc=45  ##boundary location
u=20  ##limits for initial particle locations

for i in range(0,N):  ##creates starting x coordinates for N particles
    n=random.randint(-u,u)
    randomlistx.append(n)

for i in range(0,N): ##creates starting y coordinates for N particles
    n=random.randint(-u,u)
    randomlisty.append(n)

def animate(l):  ##main function
    a=0  ##initialize counter
    """
    the while loop is unecessary since the animate function
    already performs a loop, but increasing a allows multiple steps
    per animatation loop
    """
    while a<1:
        for i in range(0,N):
            stepxx=random.randint(min,max)  ##either -1 or 1
            stepyy=random.randint(min,max)  ##either -1 or 1
            randomlistx[i]+=stepxx   ##perform random step
            randomlisty[i]+=stepyy

            if randomlistx[i]==bc:  ##creates boundary conditions, must be larger than
                randomlistx[i]-=stepxx  ##initial starting points
            if randomlistx[i]==-bc:
                randomlistx[i]-=stepxx
            if randomlisty[i]==bc:    ##if particle hits boundary it reverses step
                randomlisty[i]-=stepyy
            if randomlisty[i]==-bc:
                randomlisty[i]-=stepyy

            """
            I attemped to make the particles collide if their coordinates
            were equal but I couldn't get it to work
            """
            """
            for j in range(0,N):
                if randomlistx[i]==randomlistx[j]:
                    randomlistx[i]-=stepxx
                if randomlisty[i]==randomlisty[j]:
                    randomlisty[i]-=stepyy
            """
        a+=1

    """
    I decided to hold to the axis size constant so the particles
    look like they're moving around in a box.

    the previous positions can be maintained on screen by
    commenting out plt.cla() which clears the screen

    the window can dynamically change size by commenting out the axis limits

    if '.' linestyle is removed from the plot statement it creates a mesh
    of lines that grows, no longer models particles, but looks cool
    """

    plt.cla()   ##clears previous points on the screen
    ax.plot(randomlistx,randomlisty,'-')

    plt.xlim(-50,50)    ##sets constant window size
    plt.ylim(-50,50)
    #meanx=np.mean(randomlistx)
    #print(meanx)
Writer=animation.writers['ffmpeg']     ### writer to save animation
writer=Writer(fps=15,metadata=dict(artist='BlakeC',bitrate=1800))


ani=FuncAnimation(plt.gcf(),animate,interval=90,save_count=200)  ##calls function
ani.save('animation3.mp4',writer=writer)   ##saves animation
plt.show()
