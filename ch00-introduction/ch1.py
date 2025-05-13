# %%


# %% [markdown]
# # 00_04: Using GitHub CodeSpaces with this course

# %%
print("Hello world!")

# %%
import numpy as np
import matplotlib.pyplot as pp  

# %%
pp.figure(figsize=(6, 4))

t = np.linspace(0, 30 * np.pi, 5000)
fs = [1, (1 + np.sqrt(5)) / 2, np.sqrt(2)]

x = np.sin(fs[0] * t) + np.sin(fs[1] * t)
y = np.sin(fs[1] * t) + np.sin(fs[2] * t)

pp.plot(x, y, color="k", alpha=0.7, linewidth=0.8)
pp.axis("off");


