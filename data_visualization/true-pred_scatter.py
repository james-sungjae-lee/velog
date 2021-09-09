# import packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import ticker

def set_max(true, pred, ratio):
    return max(list(true) + list(pred)) * ratio

# generate data
num_data = 200
true = np.random.rand(num_data,) * 10000
pred = true + np.random.rand(num_data,) * 1000 - np.random.rand(num_data,) * 1000

# plot setting
fs = 15 # font size
small_fs = 15 * 0.8
ds = 5 # dot size
dc = 'black' # dot color
ms = 'o' # marker shape
xy_linewidth = 1
x_tick_level = 1e4/4
y_tick_level = 1e3

# plot size setting
fig, ax = plt.subplots(1, 1)
fig.set_figheight(4)
fig.set_figwidth(4)

# formatting for scientific notation
formatter = ticker.ScalarFormatter(useMathText=True)
formatter.set_scientific(True) 
formatter.set_powerlimits((-1,1))

# x and y axis range setting
x_min = 0
y_min = 0
xy_max = set_max(true, pred, 1.1)

# draw figure
ax.scatter(true, pred, s=ds, color=dc, marker=ms, linewidth=0)
ax.plot([0, xy_max], [0, xy_max], color=dc, linewidth=xy_linewidth)
ax.set_aspect('equal')
ax.set_ylim((y_min, xy_max))
ax.set_xlim((x_min, xy_max))
ax.yaxis.set_ticks(np.arange(y_min, xy_max, y_tick_level))
ax.set_yticklabels(np.arange(y_min, xy_max, y_tick_level), fontsize=small_fs)
ax.xaxis.set_ticks(np.arange(x_min, xy_max, x_tick_level))
ax.set_xticklabels(np.arange(x_min, xy_max, x_tick_level), fontsize=small_fs)
ax.yaxis.set_major_formatter(formatter) 
ax.xaxis.set_major_formatter(formatter) 
ax.set_ylabel('Predicted Values', fontsize=fs)
ax.set_xlabel('True Values', fontsize=fs)

fig.tight_layout()
plt.savefig('test.pdf')
plt.show()
