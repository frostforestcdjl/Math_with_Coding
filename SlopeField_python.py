import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

diff = 0.1
nx, ny = diff*5, diff
x = np.arange(-1, 5, nx)
y = np.arange(-1, 5, ny)
X, Y = np.meshgrid(x, y)


dyGP = [-2 + X - Y, X * np.exp(-2 * X) - 2 * Y, np.exp(-X) + Y, X + 2*Y, 3*np.sin(X) + 1 + Y, 2*X - 1 - Y**2, -(2*X+Y)/(2*Y), Y**3/6 - Y - X**2/3]
title = ['-2 + X - Y', 'X * exp(-2X) - 2Y', 'exp(-X) + Y', 'X + 2Y', '3sin(X) + 1 + Y', '2X - 1 - Y**2', '-(2X+Y)/(2Y)', 'Y**3/6 - Y - X**2/3']

c_n = 3
fig = plt.figure(figsize=(c_n*4, len(dyGP)//2*2))
gs = gridspec.GridSpec(nrows=len(dyGP)//c_n+1, ncols=c_n)

for i in range(len(dyGP)):
    dy = dyGP[i]
    dx = np.ones(dy.shape)

    color = dy
    ax = fig.add_subplot(gs[i//c_n, i%c_n])
    ax.streamplot(X, Y, dx, dy, color=color, density=1, cmap='jet', arrowsize=1)
    ax.set_title(title[i])
    
plt.tight_layout()
