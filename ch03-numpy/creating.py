# %% [markdown]
# # 03_02: Creating NumPy arrays

# %%
import math
import collections
import dataclasses
import datetime

import numpy as np
import pandas as pd

import matplotlib.pyplot as pp

# %%
lines = open('monalisa.txt', 'r').readlines()

# %%
lines[0]

# %%
len(lines)

# %%
monalisa_bw = np.loadtxt('monalisa.txt')

# %%
monalisa_bw

# %%
monalisa_bw.ndim

# %%
monalisa_bw.shape

# %%
monalisa_bw.size

# %%
monalisa_bw.nbytes

# %%
monalisa_bw.dtype

# %%
pp.imshow(monalisa_bw)

# %%
pp.imshow(monalisa_bw, cmap='gray')

# %%
monalisa = np.load('monalisa.npy')

# %%
monalisa.shape

# %%
pp.figure(figsize=(5,8))
pp.imshow(monalisa)

# %%
fromlist = np.array([[1,2,3],[4,5,6],[7,8,9]])

# %%
fromlist

# %%
fromlist.shape

# %%
fromlist.dtype

# %%
zero_1d = np.zeros(8, 'd') # or np.float64

# %%
zero_2d = np.zeros((8,8), np.float64)

# %%
zero_1d, zero_1d.ndim, zero_1d.shape, zero_1d.size, zero_1d.nbytes

# %%
zero_2d, zero_2d.ndim, zero_2d.shape, zero_2d.size, zero_2d.nbytes

# %%
np.zeros_like(monalisa_bw)

# %%
np.empty(24, 'd')

# %%
linear = np.linspace(0, 1, 16)

# %%
linear

# %%
pp.plot(linear, 'o')

# %%
np.arange(0, 1.5, 0.1)

# %%
random_2d = np.random.random((8,8))

# %%
random_2d

# %%
pp.matshow(random_2d)

# %%
np.random.randint(0, 10, (8,8))

# %%
pp.hist(np.random.standard_normal(100000), bins=40);

# %%
np.save('random.npy', random_2d)

# %%
np.savetxt('random.txt', random_2d)

# %%
open('random.txt', 'r').readlines()


