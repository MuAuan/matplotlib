import matplotlib.pyplot as plt
import numpy as np
import matplotlib

fig, axes = plt.subplots(2, 3, figsize=(12, 8))
x = np.linspace(0, 5, 10)

axes[0,0].plot(x, x**2, x, x**3)
axes[0,0].set_title("default axes ranges")

axes[0,1].plot(x, x**2, x, x**3)
axes[0,1].axis('tight')
axes[0,1].set_title("tight axes")

axes[0,2].plot(x, x**2, x, x**3)
axes[0,2].set_ylim([0, 60])
axes[0,2].set_xlim([2, 5])
axes[0,2].set_title("custom axes range")

axes[1,0].plot(x, x**2, x, x**3)
axes[1,0].set_title("default axes ranges2")

axes[1,1].plot(x, x**2, x, x**3)
axes[1,1].axis('tight')
axes[1,1].set_title("tight axes2")

axes[1,2].plot(x, x**2, x, x**3)
axes[1,2].set_ylim([0, 60])
axes[1,2].set_xlim([2, 5])
axes[1,2].set_title("custom axes range2")
fig.savefig("./moving_fig/ordinary_fig.png", dpi=200)
plt.show()
plt.close()

x = np.linspace(0, 5, 10)
y = x ** 2

matplotlib.rcParams.update({'font.size': 18, 'font.family': 'sans', 'text.usetex': False}) 
fig = plt.figure(figsize=(8,6))  #(width,height)
for i in range(10):
    x_offset=np.round(0.05*4,decimals=2)
    y_offset=np.round(0.05*i,decimals=2)
    width=0.3
    height=0.3
    axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8]) # main axes
    axes2 = fig.add_axes([x_offset, y_offset, width, height]) # insert axes
    
    # main figure
    # possible marker symbols: marker = '+', 'o', '*', 's', ',', '.', '1', '2', '3', '4', ...
    # possible linestype options ‘-‘, ‘--’, ‘-.’, ‘:’, ‘steps’
    
    axes1.plot(x, y, color='r', lw=3, linestyle='--',marker='o' , label=r"$y = x^2$")
    axes1.legend(loc=1) # upper left corner
    axes1.grid(True)
    axes1.set_xlabel('x')
    axes1.set_ylabel('y')
    axes1.set_title('title')

    # insert
    axes2.plot(y, x, 'g', label=r"$x = y^2$")
    axes2.legend(loc=2) # upper left corner
    axes2.set_xlabel('y')
    axes2.set_ylabel('x')
    axes2.set_title('insert title;'+str(x_offset)+"_"+str(y_offset))
    plt.pause(1)
    fig.savefig("./moving_fig/moving_fig"+str(i)+".png", dpi=200)
    plt.clf()