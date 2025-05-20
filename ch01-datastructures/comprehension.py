# %% [markdown]
# # 01_04: Comprehensions

# %%
import math
import collections
import dataclasses
import datetime

import numpy as np
import pandas as pd
import matplotlib.pyplot as pp

# %%
squares = []
for i in range(1, 11):
    squares.append(i**2)

# %%
squares

# %%
squares = [i**2 for i in range(1, 11)]

# %%
squares

# %%
squares_by_four = [i**2 for i in range(1, 11) if i**2 % 4 == 0]

# %%
squares_by_four

# %%
squares_dict = {i: i**2 for i in range(1, 11)}

# %%
squares_dict

# %%
capitals_by_country = {'United States': 'Washington, DC', 'France': 'Paris', 'Italy': 'Rome'}

# %%
countries_by_capital = {capital: country for country, capital in capitals_by_country.items()}

# %%
countries_by_capital

# %%
sum(i**2 for i in range(1, 11))

# %%
matrix = [[i*j for i in range(1,4)] for j in range(1,4)]

# %%
matrix

# %%
[element for row in matrix for element in row]



# %%
