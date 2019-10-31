import numpy as np
import matplotlib.pyplot as plt
import math
np.random.seed(0)

M, N = 10, 5

def is_pareto_efficient(X):
    is_efficient = np.ones(len(X), dtype = bool)
    for i, c in enumerate(X):
        if is_efficient[i]:
            is_efficient[is_efficient] = np.any(X[is_efficient] > c, axis=1) 
            is_efficient[i] = True  
    return is_efficient

X = np.random.sample((M, N))

eff = is_pareto_efficient(X)
ax = plt.subplot(111, projection="polar")
plt.thetagrids(np.arange(0, 360, 360/N))

for i in range(len(eff)):
    if eff[i] == True:
        ax.plot(np.append(np.arange(0, N, 1), 0) * 2 * math.pi/N, np.append(X[i, :], X[i, 0]), color="r")
    else:
        ax.plot(np.append(np.arange(0, N, 1) * 2 * math.pi/N, 0), np.append(X[i, :], X[i, 0]), color="b")
