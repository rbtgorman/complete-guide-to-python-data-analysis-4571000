# %% [markdown]
# # 01_03: Dictionaries and sets

# %%
import math
import collections
import dataclasses
import datetime

import numpy as np
import pandas as pd
import matplotlib.pyplot as pp  

# %%
capitals = {'United States': 'Washington, DC', 'France': 'Paris', 'Italy': 'Rome'}

# %%
capitals

# %%
len(capitals), len({})

# %%
capitals['Italy']

# %%
capitals['Spain'] = 'Madrid'

# %%
capitals

# %%
capitals['Germany']

# %%
'Germany' in capitals, 'Italy' in capitals

# %%
morecapitals = {'Germany': 'Berlin', 'United Kingdom': 'London'}

# %%
{**capitals, **morecapitals}

# %%
capitals.update(morecapitals)

# %%
capitals

# %%
del capitals['United Kingdom']

# %%
capitals

# %%
birthdays = {(7,15): 'Michele', (3,14): 'Albert'}

# %%
birthdays[(7,15)]

# %%
hash('Italy'), hash((7,15))

# %%
for country in capitals:
    print(country)

# %%
for country in capitals.keys():
    print(country)

# %%
capitals.keys()

# %%
list(capitals.keys())

# %%
for capital in capitals.values():
    print(capital)

# %%
for country, capital in capitals.items():
    print(country, capital)

# %%
capitals.keys()

# %%
list(capitals.keys())

# %%
capitals_default = collections.defaultdict(lambda: "I don't know!")

# %%
capitals_default.update(capitals)

# %%
capitals_default['Canada']

# %%
continents = {'America', 'Europe', 'Asia', 'Oceania', 'Africa', 'Africa'}

# %%
continents

# %%
'Africa' in continents

# %%
continents.add('Antarctica')

# %%
continents.remove('Antarctica')

# %%
for c in continents:
    print(c)



# %%
