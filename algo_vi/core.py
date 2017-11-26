#coding=utf-8
# =================
# author: zhouxin
# start_date： 171120
# description: objs in this file performs like a hub, input a concret algorithm
#              dispatch it to corresponding visualization method 
# after deep consideration, i decide to delete engine.py, co's it makes my project 
# hard to understand, it's not my purpose.
# =================


import matplotlib.pyplot as plt
from matplotlib import animation
import random

def barlist(n): 
    return [1/float(n*k) for k in range(1,6)]

fig=plt.figure()
n=100 #Number of frames
x=range(1,6)
barcollection = plt.bar(x,barlist(1))

def animate(i):
    y=barlist(i+1)
    for i, b in enumerate(barcollection):
        # print(b.color)
        b.set_height(y[i])
        b.set_color(random.choice(['red', 'green', 'grey']))

anim=animation.FuncAnimation(fig,animate,repeat=False,blit=False,frames=n,
                             interval=100)

# anim.save('mymovie.mp4',writer=animation.FFMpegWriter(fps=10))
plt.show()