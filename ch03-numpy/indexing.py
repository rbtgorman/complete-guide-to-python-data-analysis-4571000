# %% [markdown]
# # 03_03: Indexing and slicing

# %%
import math
import collections
import dataclasses
import datetime

import numpy as np
import pandas as pd
import matplotlib.pyplot as pp

# %%
monalisa = np.load('monalisa.npy')

# %%
monalisa.shape

# %%
pp.imshow(monalisa)

# %%
monalisa[600, 400, 0]

# %%
int(monalisa[600, 400, 0]), float(monalisa[600, 400, 0])

# %%
monalisa[-50, -50, 1]

# %%
monalisa[1198 - 50, 804 - 50, 1], monalisa[1148, 754, 1]

# %%
monalisa[1000, 900, 2]

# %%
monalisa[600, 400, 0] = monalisa[600, 400, 1] = monalisa[600, 400, 2] = 0

# %%
just_a_list = [[1,2,3],[4,5,6],[7,8,9]]

# %%
just_a_list[1,2]

# %%
just_a_list[1]

# %%
just_a_list[1][2]

# %%
pp.imshow(monalisa[400:800, 200:600, 0:3])

# %%
pp.imshow(monalisa[800:, :, :])

# %%
pp.imshow(monalisa[100:400, ...])

# %%
pp.imshow(monalisa[::20, ::20, :])

# %%
pp.imshow(monalisa[::-1, :, :])

# %%
row = monalisa[20, ::20, 0]

# %%
row.shape

# %%
row

# %%
pp.plot(row)

# %%
rect = monalisa[20:21, ::20, 0]

# %%
rect

# %%
rect.shape

# %%
monalisa[20:300, 20:300, :] = 200

# %%
pp.imshow(monalisa)

# %%
monalisa[20:300, 20:300, :] = np.random.randint(100, 255, size=(280, 280, 3))

# %%
pp.imshow(monalisa)

# %%
monalisa_bw = np.loadtxt('monalisa.txt')

# %%
pp.imshow(monalisa_bw, cmap='gray')

# %%
monalisa_bw < 120

# %%
monalisa_bw[monalisa_bw < 120] = 0

# %%
pp.imshow(monalisa_bw, cmap='gray')

# %%
mylist = [0,1,2,3,4,5]

# %%
myslice = mylist[0:4]

# %%
myslice[2] = myslice[3] = 100

# %%
myslice

# %%
mylist

# %%
monaslice = monalisa[:, 300:500, :]

# %%
pp.imshow(monaslice)

# %%
monaslice[:,:,:] //= 3 # integer-divide by three in place

# %%
pp.imshow(monalisa)

# %%
monacopy = monalisa_bw.copy()


