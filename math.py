from matplotlib import pyplot as plt, patches
import numpy as np
from fractions import Fraction as fr

import matplotlib as mpl

pii=np.pi

#fig = plt.figure(None, (10,10))
fig = plt.figure()
fig.set_size_inches((6.4*3, 4.8*3))
fig.set_facecolor((0.8,0.8,1))
ax = fig.subplots()

ymp = patches.Circle((0, 0), radius=pii, fill=0)
ax.add_patch(ymp)

# Move left y-axis and bottom x-axis to centre, passing through (0,0)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')

# Eliminate upper and right axes
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# Show ticks in the left and lower axes only
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

ax.axis('equal')

plt.xticks([-pii, 0, pii])
plt.yticks([-pii, 0, pii])


"""
pist_xy=np.array([pii, pii, 3*pii, pii])
nim=np.array([1, 2, 4, 6])
varit=np.array(['red', 'green', 'blue', 'orange'])
"""

"""
pist_xy=np.array([2*pii, pii, pii, pii, pii, pii, pii, pii])
nim=np.array([5, 2, 4, 6, 7, 2, 3, 5])
varit=np.array(['red', 'green', 'blue', 'orange', 'blue', 'pink' , 'pink' , 'pink'])

text=[r'$\pi$', r'$\frac{\pi}{2}$', r'$\frac{3\pi}{4}$', r'$\frac{\pi}{6}$', r'$3\pi$' , r'$3\pi$' , r'$3\pi$' , r'$3\pi$']
"""

pist_xy=np.array([30*pii, 45*pii, 60*pii, 90*pii, 120*pii, 150*pii, 180*pii, 270*pii])
nim=np.array([180, 180, 180, 180, 180, 180, 180, 180])
varit=np.array(['red', 'orange', 'yellow', 'green', 'cyan', 'blue', 'purple', 'red'])

text=[r'$\frac{30\pi}{180}$', r'$\frac{45\pi}{180}$', r'$\frac{60\pi}{180}$', r'$\frac{90\pi}{180}$',r'$\frac{120\pi}{180}$', r'$\frac{150\pi}{180}$',r'$\frac{180\pi}{180}$', r'$\frac{270\pi}{180}$',]

x = np.cos(pist_xy/nim)
y = np.sin(pist_xy/nim)

plt.scatter(x*pii, y*pii, color=varit, marker='X')

for i in range(len(pist_xy)):
    plt.annotate(text[i],
             xy=(np.cos(pist_xy[i]/nim[i])*pii, np.sin(pist_xy[i]/nim[i])*pii), xycoords='data',
             xytext=(+10, +40), textcoords='offset points', fontsize=12,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=0"))


plt.show()