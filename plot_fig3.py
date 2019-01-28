import matplotlib.pyplot as plt
import numpy as np

# データ生成
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# プロット領域(Figure, Axes)の初期化
plt.figure(figsize=(12, 8))
fig1=plt.subplot(131)
fig2=plt.subplot(132)
fig3=plt.subplot(133)

# 棒グラフの作成
fig1.bar([1,2,3],[3,4,5])
fig1.set_xlabel("x")
fig1.set_ylabel("y")
fig2.barh([0.5,1.5,2.5],[0.5,1,2])
fig2.set_xlabel("xbar")
fig2.set_ylabel("ybar")
fig2.set_xlim(0,3)
fig2.set_ylim(0,3)
fig3.scatter(y1, y2)
plt.xlabel("sin(x)")
plt.ylabel("cos(x)")
plt.xlim(-1.2,1.2)
plt.ylim(-1.5,1.5)
#fig3.set_xlabel("sin(x)")
#fig3.set_ylabel("cos(x)")

plt.show()