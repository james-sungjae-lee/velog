# import packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# generate data
data = {'A': [30, 0.97, 70],
        'B': [16, 0.95, 91],
        'C': [12, 0.96, 80], 
        'D': [11, 0.97, 66]}
df = pd.DataFrame(data)

# plot setting
value_y1 = df.iloc[0]
value_y2 = df.iloc[2]
value_star = df.iloc[1]

fs = 25 # font size
x_pos = np.arange(len(df.columns))
bar_width = 0.35

fig, ax1 = plt.subplots()
fig.set_figheight(10)
fig.set_figwidth(10)

# draw plot
rects1 = ax1.bar(x_pos - (bar_width*1.1/2), value_y1, width=bar_width, label='value_y1',
                 color='gray', edgecolor='black', alpha=0.65, linewidth=1.5)
ax1.set_ylabel('value_y1', fontsize=fs)
ax1.set_xticks(x_pos)
ax1_y_min = 0
ax1_y_max = 50
ax1.set_ylim((ax1_y_min, ax1_y_max))
ax1.yaxis.set_ticks(np.arange(ax1_y_min, ax1_y_max+1, 10))
ax1.set_yticklabels(np.arange(ax1_y_min, ax1_y_max+1, 10), fontsize=fs*0.8)
ax1.set_xticklabels(df.columns, fontsize=fs)

ax2 = ax1.twinx()
rects2 = ax2.bar(x_pos + (bar_width*1.1/2), value_y2, width=bar_width, label='value_y2',
                 color='white', edgecolor='black', hatch='/', alpha=0.65, linewidth=1.5)
ax2.set_ylabel('value_y2', fontsize=fs)
ax2.set_xticks(x_pos)
ax2_y_min = 50
ax2_y_max = 130
ax2.set_ylim((ax2_y_min, ax2_y_max))
ax2.yaxis.set_ticks(np.arange(ax2_y_min, ax2_y_max+1, 10))
ax2.set_yticklabels(np.arange(ax2_y_min, ax2_y_max+1, 10), fontsize=fs*0.8)
ax2.set_xticklabels(df.columns, fontsize=fs)

ax3 = ax1.twinx()
rects3 = ax3.scatter(x_pos, value_star, label='value_star', marker='*', color='black', s=200)
for i in range(len(x_pos)):
    ax3.text(x_pos[i]-0.25, value_star[i]+0.005, round(value_star[i], 2), fontsize=fs)

ax3_y_min = 0.88
ax3_y_max = 0.983
ax3.set_ylim((ax3_y_min, ax3_y_max))
ax3.set_yticks([])
ax3.set_yticks([], minor=True)

lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
lines3, labels3 = ax3.get_legend_handles_labels()
ax3.legend(lines + lines2 + lines3, labels + labels2 + labels3,fontsize=fs-3, loc=5)

fig.tight_layout()
plt.savefig('test.pdf')
plt.show()
