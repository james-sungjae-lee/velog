# import packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# generate data
# three types of value in each case (val1, val2, and val3)
# two different section (X and Y)
# four different case (a, b, c, d is order of list)
val1_X = [12, 13, 15, 14]
val1_Y = [6, 5, 7, 6.5]

val2_X = [30, 45, 33, 48]
val2_Y = [15, 20, 19, 22]

val3_X = [0.98, 0.975, 0.96, 0.97]
val3_Y = [0.99, 0.99, 0.985, 0.99]

# plot setting
fs = 25 # font size
small_fs = 25*0.8
bw = 0.4 # bar width

solid_style = {'color': 'gray', 'edgecolor': 'black', 'alpha': 0.65, 'linewidth': 1.5}
hatch_style = {'color': 'white', 'edgecolor': 'black', 'hatch': '//', 'alpha': 0.65, 'linewidth': 1.5}
marker_style = {'color': 'black', 'marker': '*', 's': 200}

x_pos_1 = np.array([1, 2, 3, 4]) # x position for type X
x_pos_2 = np.array([6, 7, 8, 9]) # x position for type Y
x_pos_all = np.concatenate((x_pos_1, x_pos_2))
x_tick_list = ['a', 'b', 'c', 'd']

fig, ax1 = plt.subplots()
fig.set_figheight(10)
fig.set_figwidth(10)

# draw figure
# axes 1
rects1 = ax1.bar(x_pos_1-(bw * 1.15/2), val1_X, bw, label='A', **solid_style)
rects2 = ax1.bar(x_pos_2-(bw * 1.15/2), val1_Y, bw, **solid_style)

ax1_y_min = 0
ax1_y_max = 20

ax1.plot([5, 5], [0, 20], color='grey')
ax1.set_ylim((ax1_y_min, ax1_y_max))
ax1.set_yticks(np.arange(ax1_y_min, ax1_y_max+1, 5))
ax1.set_yticklabels(np.arange(ax1_y_min, ax1_y_max+1, 5), fontsize=small_fs)
ax1.set_xticks(x_pos_all)
ax1.set_xticklabels(x_tick_list * 2, fontsize=small_fs)
ax1.set_ylabel('Value Type 1', fontsize=fs)

# axes 2
ax2 = ax1.twinx()
rects3 = ax2.bar(x_pos_1+(bw*1.15/2), val2_X, bw, label='B', **hatch_style)
rects4 = ax2.bar(x_pos_2+(bw*1.15/2), val2_Y, bw, **hatch_style)

ax2_y_min = 0
ax2_y_max = 60

ax2.set_ylim((ax2_y_min, ax2_y_max))
ax2.set_yticks(np.arange(ax2_y_min, ax2_y_max+1, 10))
ax2.set_yticklabels(np.arange(ax2_y_min, ax2_y_max+1, 10), fontsize=small_fs)
ax2.set_ylabel('Value Type 2', fontsize=fs)

# axes 3
ax3 = ax1.twinx()
rects5 = ax3.scatter(x_pos_1, val3_X, label=r'$C^2$', **marker_style)
for i in range(len(x_pos_1)):
    ax3.text(x_pos_1[i]-0.3, val3_X[i]+0.005, round(val3_X[i], 4), fontsize=small_fs)
    
rects6 = ax3.scatter(x_pos_2, val3_Y, **marker_style)
for i in range(len(x_pos_2)):
    ax3.text(x_pos_2[i]-0.3, val3_Y[i]-0.01, round(val3_Y[i], 4), fontsize=small_fs)

ax3_y_min = 0.82
ax3_y_max = 1.0
ax3.set_ylim((ax3_y_min, ax3_y_max))
ax3.set_yticks([], minor=True)

# legend setting
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
lines3, labels3 = ax3.get_legend_handles_labels()
ax3.legend(lines + lines2 + lines3, labels + labels2 + labels3,fontsize=fs-3, loc=5,
           bbox_to_anchor=(1.0, 0.6))

# additional x ticks (setting at axes 1)
ax1.text(2.5, -1.8, 'Type X Values', ha='center', va='center', fontsize=fs)
ax1.text(7.5, -1.8, 'Type Y Values', ha='center', va='center', fontsize=fs)

fig.tight_layout()
plt.savefig('test.pdf')  
plt.show()
