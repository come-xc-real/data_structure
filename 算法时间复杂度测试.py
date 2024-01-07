import time

import matplotlib.pyplot as plt
import numpy as np


# def fun(n):
#     i = 1
#     t = time.time()
#     while i <= n:
#         i *= 2
#     t = time.time() - t
#     return t

def fun(n):
    i, k = 1, 100
    t = time.time()
    while i <= n:
        k += 1
        i += 2
    t = time.time() - t
    return t


x = np.linspace(0, 6000, 600)

list = []
for i in x:
    list.append(fun(i))

y3 = np.array(list)

plt.plot(x, y3)
plt.show()





