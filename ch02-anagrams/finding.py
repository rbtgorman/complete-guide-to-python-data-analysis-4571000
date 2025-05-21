# %% [markdown]
# # 02_03: Finding anagrams

# %%
import math
import collections
import dataclasses
import datetime

import numpy as np
import pandas as pd
import matplotlib.pyplot as pp

# %%
words = sorted({line.strip().lower() for line in open('words.txt', 'r')})

# %%
sorted("aaron")

# %%
sorted("elvis") == sorted("lives")

# %%
sorted("bowie") == sorted("lives")

# %%
'-'.join(sorted("aaron"))

# %%
''.join(sorted("aaron"))

# %%
def signature(word):
    return ''.join(sorted(word))

# %%
words_by_signature = {}

for word in words:
    if signature(word) not in words_by_signature:
        # if we haven't seen this signature, define the dictionary entry with this word
        words_by_signature[signature(word)] = {word}
    else:
        # otherwise add the word to the set for this signature
        words_by_signature[signature(word)].add(word)

# %%
words_by_signature

# %%
words_by_signature = collections.defaultdict(set)

for word in words:
    words_by_signature[signature(word)].add(word)

# %%
words_by_signature

# %%
anagrams_by_signature = {sig: wordset for sig, wordset in words_by_signature.items() if len(wordset) > 1}

# %%
signature('python')

# %%
anagrams_by_signature[signature('python')]

# %%
def find_anagram(word):    
    return anagrams_by_signature[signature(word)]

# %%
find_anagram('tops')

# %%
find_anagram('michele')

# %%
def find_anagram(myword):
    try:
        return anagrams_by_signature[signature(word)]
    except KeyError:
        return set()

# %%
find_anagram('Michele')

# %%
sorted(anagrams_by_signature.keys(), key=len, reverse=True)

# %%
[anagrams_by_signature[sig] for sig in sorted(anagrams_by_signature.keys(), key=len, reverse=True)]

# %%
sorted(anagrams_by_signature.values(), key=len, reverse=True)


