# %% [markdown]
# # 01_01: Warmup with Python loops

# %%
import math
import collections
import dataclasses
import datetime

# We load often-used modules using shorter aliases. np and pd are standard from numpy and pandas
import numpy as np
import pandas as pd

# We also import the simpler command-oriented interface to matplotlib, pyplot
import matplotlib.pyplot as pp  

# %%
for i in range(0, 10):
    print(i)

# %%
for i in range(5):
    print(i)

# %%
for i in range(0, 10, 2):
    print(i)

# %%
for count_100 in range(1+1):
    for count_50 in range(2+1):
        for count_25 in range(5+1):
            for count_10 in range(10+1):
                for count_5 in range(20+1):
                    for count_1 in range(100+1):
                        pass # do nothing for the moment

# %%
combinations = []

for count_100 in range(1+1):
    for count_50 in range(2+1):
        for count_25 in range(4+1):
            for count_10 in range(10+1):
                for count_5 in range(20+1):
                    for count_1 in range(100+1):
                        if 100*count_100 + 50*count_50 + 25*count_25 + 10*count_10 + 5*count_5 + count_1 == 100:
                            combinations.append([count_100, count_50, count_25, count_10, count_5, count_1])

# %%
combinations

# %%
len(combinations)

# %%
for count_25 in range(4+1):
    print(count_25)

# %%
for amount_25 in range(0, 100+1, 25):
    print(amount_25)

# %%
combinations_amounts = []

for amount_100 in range(0, 100+1, 100):
    for amount_50 in range(0, 100+1, 50):
        for amount_25 in range(0, 100+1, 25):
            for amount_10 in range(0, 100+1, 10):
                for amount_5 in range(0, 100+1, 5):
                    total_so_far = amount_100 + amount_50 + amount_25 + amount_10 + amount_5
                    
                    if total_so_far <= 100:
                        combinations_amounts.append([amount_100, amount_50, amount_25, amount_10, amount_5,
                                                     100 - total_so_far])

# %%
combinations_amounts

# %%
len(combinations_amounts) 

# %%
# [copy code from above]

def find_combinations(total):
    combinations_amounts = []

    for amount_100 in range(0, total+1, 100):
        for amount_50 in range(0, total+1, 50):
            for amount_25 in range(0, total+1, 25):
                for amount_10 in range(0, total+1, 10):
                    for amount_5 in range(0, total+1, 5):
                        total_so_far = amount_100 + amount_50 + amount_25 + amount_10 + amount_5

                        if total_so_far <= total:
                            combinations_amounts.append([amount_100, amount_50, amount_25, amount_10, amount_5,
                                                         total - total_so_far])
    
    return combinations_amounts

# %%
len(find_combinations(200))

# %%
len(find_combinations(300))

# %%
totals = range(100, 600, 100)
lengths = [len(find_combinations(total)) for total in totals]

# %%
pp.plot(totals, lengths)


