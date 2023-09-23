# Projectile Motion Plot
# => Project on GitHub (https://github.com/JelyFishhhhhh/projectile-motion-plot)

import numpy as np
import matplotlib.pylab as plt
from math import pi, degrees

# plot init
plt.title("Physics Bonus HomeWork")
plt.xlabel("x(m)")
plt.ylabel("y(m)")
# init constants
v = 50
g = 9.8
theta = np.arange(pi/ 12, (pi* 5) / 12, pi/ 12)

for rad in theta:
    
    # init x, y coordinates
    x_coordinate= []
    y_coordinate= []
    # timeline
    times = np.linspace(start=0, stop= 50, num= 5000)
    
    # calc x, y
    for c_times in times:
        
        x = ((v* c_times)* np.cos(rad))
        y = ((v* c_times)* np.sin(rad))- ((0.5* g)*(c_times** 2))
        x_coordinate.append(x)
        y_coordinate.append(y)
    
    # del below x-axis value
    p = [i for i, j in enumerate(y_coordinate) if j < 0]

    for index in sorted(p, reverse=True):
        
        del x_coordinate[index]
        del y_coordinate[index]

    # plot
    plt.plot(x_coordinate, y_coordinate, "#578891") # plt with same color (#578891)
    # plt.plot(x_coordinate, y_coordinate) # plt with different color
    plt.text(x= x_coordinate[int((len(x_coordinate)-1)/2)], y= y_coordinate[int((len(y_coordinate)-1)/2)], s= f"{int(round(degrees(rad), 0))}°")

# save-N-show
plt.savefig("result.png") # save plot
plt.show() # show plt