# %% [markdown]
# # 02_02 Loading text files

# %%
import math
import collections
import dataclasses
import datetime

import numpy as np
import pandas as pd
import matplotlib.pyplot as pp

# %%
words = []
for line in open('words.txt'):
    words.append(line)

# %%
len(words)

# %%
words[:10]

# %%
'Aaron\n'.strip()

# %%
'Aaron\n'.strip().lower()

# %%
words = []
for line in open('words.txt'):
    words.append(line.strip().lower())

# %%
words[:10]

# %%
words = set()
for line in open('words.txt'):
    words.add(line.strip().lower())

# %%
words = {line.strip().lower() for line in open('words.txt')}

# %%
words

# %%
words = sorted({line.strip().lower() for line in open('words.txt')})

# %%
words

# %%
paroles = sorted({line.strip().lower()
                 for line in open('francais.txt', encoding='latin-1')})

# %%
paroles


