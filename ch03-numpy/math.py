# %% [markdown]
# # 03_04: Doing math with NumPy arrays

# %%
import math
import collections
import dataclasses
import datetime

import numpy as np
import pandas as pd
import matplotlib.pyplot as pp

# %%
x = np.linspace(0.0, 5.0*math.pi, 128)  # extrema are included!

# %%
x

# %%
math.sin(x)

# %%
sinx = np.sin(x)

# %%
sinx

# %%
pp.plot(x, sinx)

# %%
pp.plot(x, sinx)
pp.plot(x, np.cos(x))
pp.plot(x, np.log(1.0 + x))

# %%
pp.plot(x, sinx, label='sin(x)')
pp.plot(x, np.cos(x), label='cos(x)')
pp.plot(x, np.log(1 + x), label='log(1+x)')

pp.legend()

# %%
cosx = np.cos(x)

# %%
y = sinx * cosx
z = cosx**2 - sinx**2  # the power operator in Python is **, not ^  

pp.plot(x, y)
pp.plot(x, z)

# %%
x + y[16:32]

# %%
w = sinx + 1.5

# %%
pp.plot(x, sinx, label='sin(x)')
pp.plot(x, w, label='sin(x) + 1.5')
pp.legend()

# %%
monalisa_bw = np.loadtxt('monalisa.txt')

# %%
monalisa_bw.shape

# %%
xgrad = np.linspace(0.0, 1.0, 134)

# %%
monalisa_xgrad = monalisa_bw * xgrad

# %%
pp.subplot(1, 2, 1); pp.imshow(monalisa_bw, cmap='gray')
pp.subplot(1, 2, 2); pp.imshow(monalisa_xgrad, cmap='gray')

# %%
ygrad = np.linspace(0.0, 1.0, 200)

# %%
monalisa_ygrad = ygrad * monalisa_bw

# %%
ygrad_2d = ygrad[:, np.newaxis]

# %%
ygrad_2d.shape

# %%
monalisa_ygrad = monalisa_bw * ygrad_2d

# %%
pp.subplot(1, 2, 1); pp.imshow(monalisa_xgrad, cmap='gray')
pp.subplot(1, 2, 2); pp.imshow(monalisa_ygrad, cmap='gray')

# %%
np.array([0.0, 1.0, 2.0]) @ np.array([-1.0, -2.0, -3.0])  # same as np.dot()

# %%
np.array([0.0, 1.0, 2.0]) * np.array([-1.0, -2.0, -3.0])

# %%
np.array([[0.0, 1.0, 2.0], [3.0, 4.0, 5.0]]) @ np.array([10.0, 20.0, 30.0])
# shapes (2,3) and (3,)

# %%
np.array([100.0, 200.0]) @ np.array([[0.0, 1.0, 2.0], [3.0, 4.0, 5.0]])
# shapes (2,) and (2,3)

# %%
np.array([[0.0, 1.0, 2.0], [3.0, 4.0, 5.0]]) @ np.array([[10.0, 20.0], [30.0, 40.0], [50.0, 60.0]])
# shapes (2,3) and (3,2)


