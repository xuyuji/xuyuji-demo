import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

heights = [[0, 0, 0],[3, 2, 1],[-3, 2, 1],[0, 4, 2],[0, -2, 2],[3, 0, 3],[-3, 0, 3],[0, 2, 4],[0, 2, -2],[3, 4, -1],[3,-2,-1],[6,0,0]]
fig, ax = plt.subplots()
bars = ax.bar(np.arange(len(heights[0])), heights[0], 0.35)
ax.set_ylim(-6,6)
ax.set_xticklabels(['', 'A(3)', '', 'B(2)', '', 'C(1)'])

def update(frame):
    height = heights[frame]
    needRed = frame % 2 == 1
    maxHeight = max(height)
    for i in range(0, len(height)): 
        bars[i].set_height(height[i])
        if needRed and height[i] == maxHeight:
            bars[i].set_facecolor('red') 
            needRed=False
        else:
            bars[i].set_facecolor('blue') 
    return bars,

anim = animation.FuncAnimation(fig, update, frames=range(len(heights)), interval=1000)
anim.save('GifGen/routing_algo.gif', writer='imagemagick')
# plt.show()
