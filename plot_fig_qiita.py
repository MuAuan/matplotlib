import matplotlib.pyplot as plt
import numpy as np

# プロット領域(Figure, Axes)の初期化
fig = plt.figure()
ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(224)
ax4 = fig.add_subplot(223) #追記
ax1.axis([-1.2, 1.2, -1.2, 1.2])

# 棒グラフの作成
s = 1
while True:
    # ax1-3を削除する
    #fig.delaxes(ax1)
    fig.delaxes(ax2)
    fig.delaxes(ax3)
    #plt.pause(0.01) #これ入れるとちかちかする
    #ax1 = fig.add_subplot(221)
    ax2 = fig.add_subplot(222)
    ax3 = fig.add_subplot(224)
    #ax1.axis([-1.2, 1.2, -1.2, 1.2]) 
    ax2.axis([-2.2, 2.2, -2.2, 2.2]) 
    ax3.axis([-1.2, 1.2, -1.2, 1.2]) 
    y1 = np.sin(s/10)*np.exp(-s/1000)
    y2 = np.cos(s/10)*np.exp(-s/1000)
    y3 = np.sin(s/10)
    y4 = np.cos(s/10)
    ax1.scatter(y1, y2)
    ax2.scatter(y1+y4, y2+y3)
    ax3.scatter(y4, y3)
    ax4.scatter(s,y1*y1+y2*y2) #追記
    ax4.set_yscale("log")#y軸のscale追記
    plt.pause(0.001)
    s += 1