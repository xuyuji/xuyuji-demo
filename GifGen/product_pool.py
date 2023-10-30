import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import random

# 用折线图表示商品池变化，无代价区用虚线表示
# A、B累计单量趋势图、预期进度
# A、B当前单量趋势图

productPool = [[10,12,0],[10,11,0],[21,20,1],[5,3,2],[30,25,5]]
curor = 1
preDayTarget = 950
aCogs,targetCogs = 0,0

fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(12,8))
fig.subplots_adjust(hspace=0.8)

def extendLim(maxValue,nowLim):
    while maxValue > 0.8 * nowLim:
        nowLim = nowLim * 1.5
    return nowLim

ax1.set_title('Daily product order num')
line1, = ax1.plot([], [], label='order num')
ax1.legend()
xlim1 = 50
ylim1 = 100
line1_x = []
line1_y = []
def draw1(i,order_num):
    if i == 0:
        global line1_x,line1_y
        line1_x,line1_y = [],[]
    line1_x.append(i)
    line1_y.append(order_num)
    line1.set_data(line1_x,line1_y)
    
    global xlim1,ylim1
    ax1.set_xlim(0, extendLim(i,xlim1))
    ax1.set_ylim(0, extendLim(order_num,ylim1))

ax2.set_title('Total cogs')
line2, = ax2.plot([], [], label="target actual total cogs")
xlim2 = 50
ylim2 = 100
line2_x = []
line2_y = []
line22, = ax2.plot([], [], label="target plan total cogs")
line22_x = []
line22_y = []
ax2.legend()
def draw2(i,order_num):
    if i == 0:
        global line2_x,line2_y,line22_x,line22_y
        line2_x,line2_y,line22_x,line22_y = [],[],[],[]
    line2_x.append(i)
    line2_y.append(aCogs)
    line2.set_data(line2_x,line2_y)
    line22_x.append(i)
    line22_y.append(targetCogs)
    line22.set_data(line22_x,line22_y)
    
    global xlim2,ylim2
    ax2.set_xlim(0, extendLim(i,xlim2))
    ax2.set_ylim(0, extendLim(aCogs,ylim2))

ax3.set_title("Product pool")
line3, = ax3.plot([], [], label="cursor")
xlim3 = 50
ax3.set_ylim(0, 6)
ax3.set_yticks([0, 1, 2, 3, 4, 5], ['', 'A(10) B(12)', 'A(10) B(11)', 'A(21) B(20)', 'A(5) B(3)', 'A(30) B(25)'])
# ax3.set_yticklabels(['A(10) B(12)', 'A(10) B(11)', 'A(21) B(20)', 'A(5) B(3)', 'A(30) B(25)'])
line3_x = []
line3_y = []
line32, = ax3.plot(0, 0, color='green', linestyle='--', label="no cost zone")
line32_x = []
line32_y = []
ax3.legend()
def draw3(i):
    if i == 0:
        global line3_x,line3_y
        line3_x,line3_y = [],[]
    line3_x.append(i)
    global curor
    line3_y.append(curor)
    line3.set_data(line3_x,line3_y)

    line32_x.append(i)
    line32_y.append(1)
    line32.set_data(line32_x,line32_y)

    global xlim3
    ax3.set_xlim(0, extendLim(i,xlim3))

# line4a, = ax4.plot([], [])
# line4b, = ax4.plot([], [])
# xlim4 = 50
# ax4.set_ylim(0, len(productPool)+2)
# line4a_x,line4a_y,line4b_x,line4b_y = [],[],[],[]
# def draw4(i,a,b):
#     global aOrder,bOrder
#     if i == 0:
#         global line4a_x,line4a_y,line4b_x,line4b_y
#         line4a_x,line4a_y,line4b_x,line4b_y = [],[],[],[]
#     line4a_x.append(i)
#     line4a_y.append(a)
#     line4a.set_data(line4a_x,line4a_y)
#     line4b_x.append(i)
#     line4b_y.append(b)
#     line4b.set_data(line4b_x,line4b_y)

#     global xlim4,ylim4
#     ax4.set_xlim(0, extendLim(i,xlim4))

def update(frame):
    global curor
    if frame == 0:
        global aCogs,targetCogs
        aCogs,targetCogs = 0,0
    order_num = int(20+20*np.sin(frame)+random.randint(1,20))
    if order_num < 0:
        order_num = 0

    if aCogs < targetCogs * 0.99:
        curor+=1
    if aCogs > targetCogs * 1.01:
        curor-=1
    if curor >= len(productPool):
        curor = len(productPool)-1
    if curor < 1:
        curor = 1
    
    aOrder,bOrder = 0,0
    cogs = 0
    for j in range(0,len(productPool)):
        if j <= curor:
            cogs += order_num*productPool[j][0]   # 使用A供应商
            aOrder+=order_num
        else:
            bOrder+=order_num
    print("a:{},b:{},cursor:{}",aOrder,bOrder,curor)
    aCogs += cogs
    targetCogs += preDayTarget
    
    draw1(frame, order_num)
    draw2(frame, order_num)
    draw3(frame)
    # draw4(frame,curor+1,len(productPool)-1-curor)
    
    return line1

ani = animation.FuncAnimation(fig, update, frames=range(80), interval=200)
ani.save('GifGen/product_pool.gif', writer='imagemagick')
plt.show()