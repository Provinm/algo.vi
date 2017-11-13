#coding=utf-8
# =================
# author: zhouxin
# start_date： 171112
# description: this file will be deleted after i have clear thinking about 
#              this projects know how to convert data to animation pic 
#              using matplotlib
# =================

from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np
import random
from collections import OrderedDict

# bubble sort code

def bubble(lst):
    
    length = len(lst)
    r = []
    for i in range(length):
        
        for j in range(i+1, length):
            dct = OrderedDict([(k, False) for k in lst])
            dct[lst[i]] = True
            dct[lst[j]] = True
            r.append(dct)
            print(dct)
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]

            dct = OrderedDict([(k, False) for k in lst])
            dct[lst[i]] = True
            dct[lst[j]] = True
            r.append(dct)
            print(dct)
            
    return r

r = bubble([5,3,1,4,7,9])


frames = len(r)


fig = plt.figure()
# ax = plt.axes(xlim=(0,2), ylim=(-2, 2))
# line, = ax.plot([], [], lw=2)

def animate(i):
    data = r[i]
    height = data.keys()
    left = list(range(len(height)))
    width = 0.8
    base_color = []
    for i in data.values():
        if i:
            base_color.append('green')
        else:
           
            base_color.append('red')
    return plt.bar(left, height, width=0.8, color=base_color)

anim = animation.FuncAnimation(fig, animate, frames=frames, interval=1000, blit=True)


plt.show()