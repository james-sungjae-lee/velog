# import packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# generate data
value_1 = [10, 20, 30, 40]
value_2 = [5, 10, 15, 25]
value_3 = [3, 6, 9, 18]

# plot setting
fs = 30 # font size
small_fs = fs * 0.8
bw = 0.4 # bar width
x_pos = [1, 1.5, 2.2, 2.7]

style_1 = {'linewidth': 2, 'edgecolor': 'black', 'hatch': '/', 'color': 'white', 'capsize': 20}
style_2 = {'linewidth': 2, 'edgecolor': 'black', 'hatch': '.', 'color': 'white', 'capsize': 20}
style_3 = {'linewidth': 2, 'edgecolor': 'black', 'hatch': '\\', 'color': 'white', 'capsize': 20}

# draw plot
fig, ax1 = plt.subplots()
fig.set_figheight(10)
fig.set_figwidth(10)

ax1.bar(x_pos, value_1, bw, **style_1)
ax1.bar(x_pos, value_2, bw, **style_2)
ax1.bar(x_pos, value_3, bw, **style_3)

ax1.set_xticks(x_pos)
ax1.set_xticklabels(['A', 'B', 'A', 'B'], fontsize=small_fs)

y_min = 0
y_max = 50
ax1.set_ylim((y_min, y_max))
ax1.set_yticks(np.arange(y_min, y_max+1, 5))
ax1.set_yticklabels(np.arange(y_min, y_max+1, 5), fontsize=small_fs)

ax1.text(1.25, -4, 'Type X Values', ha='center', va='center', fontsize=fs)
ax1.text(2.5, -4, 'Type Y Values', ha='center', va='center', fontsize=fs)

ax1.legend(['Value First', 'Value Second', 'Value Third'], loc='upper left', fontsize=small_fs)

fig.tight_layout()
plt.savefig('test.pdf')  
plt.show()
