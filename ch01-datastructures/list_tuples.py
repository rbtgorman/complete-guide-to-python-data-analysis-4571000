
# %%
import math
import collections
import dataclasses
import datetime

import numpy as np
import pandas as pd
import matplotlib.pyplot as pp  

# %%
nephews = ['Huey', 'Dewey', 'Louie']

# %%
nephews

# %%
len(nephews)

# %%
len([])

# %%
nephews[0]

# %%
nephews[2]

# %%
nephews[3]

# %%
nephews[-1]

# %%
nephews[-2]

# %%
for i in range(3):
    nephews[i] = nephews[i] + ' Duck'

# %%
nephews

# %%
mix_it_up = [1, [2, 3], 'alpha']

# %%
mix_it_up

# %%
'Huey' in nephews

# %%
'Huey Duck' in nephews

# %%
nephews.append('April Duck')

# %%
nephews

# %%
nephews.extend(['May Duck', 'June Duck'])

# %%
nephews

# %%
ducks = nephews + ['Donald Duck', 'Daisy Duck']

# %%
ducks

# %%
ducks.insert(0, 'Scrooge McDuck')

# %%
ducks

# %%
del ducks[0]

# %%
ducks

# %%
ducks.remove('Donald Duck')

# %%
ducks

# %%
ducks.sort()

# %%
ducks

# %%
reverse_ducks = sorted(ducks, reverse=True)

# %%
reverse_ducks

# %%
for duck in ducks:
    print(duck, "quacks!")

# %%
squares = [1, 4, 9, 16, 25, 36, 49]

# %%
squares[0:2]

# %%
squares[:4]

# %%
squares[3:]

# %%
squares[:]

# %%
squares[0:7:2]

# %%
squares[-3:-1]

# %%
# reverse the list!
squares[::-1]

# %%
squares[2:4] = ['four', 'nine']

# %%
squares

# %%
del squares[4:6]

# %%
squares

# %%
integers = ('one', 'two', 'three', 'four')

# %%
integers

# %%
integers[-1], integers[1:3]

# %%
integers[0] = 1

# %%
(a, b) = (1, 2)

# %%
c, d = 3, 4

# %%
for i, duck in enumerate(ducks):
    print(i, duck)

# %%
def print_three_args(a, b, c):
    print(a, b, c)

# %%
my_args = (1,2,3)

# %%
print_three_args(*my_args)

# %%
def any_args(*args):
    print(args)

# %%
any_args(1,2,3)


