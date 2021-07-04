# -*- coding: utf-8 -*-
"""Assignment-7

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ydFJYCjNsmzBAxEGAbG5ZA1G_cm5vdFl
"""

import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as axes3d

theta, phi = np.linspace(0, 2 * np.pi, 40), np.linspace(0, np.pi, 40)
THETA, PHI = np.meshgrid(theta, phi)
k=161
R = np.sqrt(k**2-161/4)
X = R * np.sin(PHI) * np.cos(THETA)+1
Y = R * np.sin(PHI) * np.sin(THETA)+7/2
Z = R * np.cos(PHI)-1
fig = plt.figure()
ax = fig.add_subplot(1,1,1, projection='3d')
plot = ax.plot_surface(
    X, Y, Z, rstride=1, cstride=1, cmap=plt.get_cmap('jet'),
    linewidth=0, antialiased=False, alpha=0.5)

plt.show()