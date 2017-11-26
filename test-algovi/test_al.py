	
# If you don't need blitting

import matplotlib.pylab as plt
import matplotlib.animation as animation
import numpy as np

#create image with format (time,x,y)
image = np.random.rand(100,10,10)

#setup figure
fig = plt.figure()
ax1 = fig.add_subplot(1,2,1)
ax2 = fig.add_subplot(1,2,2)
#set up viewing window (in this case the 25 most recent values)
repeat_length = (np.shape(image)[0]+1)/4
ax2.set_xlim([0,repeat_length])
#ax2.autoscale_view()
ax2.set_ylim([np.amin(image[:,5,5]),np.amax(image[:,5,5])])

#set up list of images for animation


im = ax1.imshow(image[0,:,:])
im2, = ax2.plot([], [], color=(0,0,1))

def func(n):
    im.set_data(image[n,:,:])

    im2.set_xdata(np.arange(n))
    im2.set_ydata(image[0:n, 5, 5])
    if n>repeat_length:
        lim = ax2.set_xlim(n-repeat_length, n)
    else:
        # makes it look ok when the animation loops
        lim = ax2.set_xlim(0, repeat_length)
    return im, im2

ani = animation.FuncAnimation(fig, func, frames=image.shape[0], interval=30, blit=False)

plt.show()