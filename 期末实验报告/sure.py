import time

from matplotlib import pyplot as plt


def fuc_a():
    pass
def fuc_b():
    a = 1
    b = 1
x_list = []
t_list = []
for i in range(100):
    t = time.time()
    for j in range(100000):
        fuc_b()
    t = time.time() - t
    t_list.append(t)
    x_list.append(i)

plt.plot(x_list, t_list)
plt.show()

