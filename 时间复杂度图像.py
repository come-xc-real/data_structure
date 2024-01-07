import numpy as np
import matplotlib.pyplot as plt
import time


def fuc1(n):
    x, y = n, 100
    count = 0
    t = time.time()
    while y > 0:
        if x > 100:
            x -= 10
            y -= 1
        else:
            x += 1
        count += 1
    t = time.time() - t
    return [count, t]


def fuc2(n):
    i, k = 1, 100
    count = 0
    t = time.time()
    while i <= n:
        k += 1
        i += 2
        count += 1
    t = time.time() - t
    return [count, t]


def fuc3(n):
    i = 1
    count = 0
    t = time.time()
    while i <= n:
        i *= 2
        count += 1
    t = time.time() - t
    return [count, t]


def fuc4(n):
    count = 0
    t = time.time()
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            k = 1
            while k <= n:
                k *= 5
                count += 1
    t = time.time() - t
    return [count, t]


def main(fuc, name, x=np.linspace(1, 5001, 5000), y_test=np.linspace(100, 100, 5000), count=5001, t_c=600000):
    fuc_list = []
    fuc_time_list = []
    for i in range(1, count):
        c, t = fuc(i)
        fuc_list.append(c)
        fuc_time_list.append(t * t_c)
    y_real = np.array(fuc_list)
    y_real_time = np.array(fuc_time_list)
    plt.plot(x, y_test, "r", label="test")
    plt.plot(x, y_real, "g", label="real")
    plt.plot(x, y_real_time, "y", label="real_time")
    plt.legend(loc="lower right")
    plt.title(name,
              fontdict={"fontsize": 20}, loc="center")
    plt.xlabel("Number of executions", fontdict={"fontsize": 10})
    plt.ylabel("Elapsed time and number of runs", fontdict={"fontsize": 10})
    plt.show()


if __name__ == '__main__':
    x = np.linspace(1, 5001, 5000)

    main(fuc1, "fuc1", y_test=np.linspace(100, 100, 5000))

    main(fuc2, "fuc2", y_test=x / 2)

    main(fuc3, "fuc3", y_test=np.log2(x), t_c=10000)

    fuc4_x = np.linspace(1, 201, 200)
    main(fuc4, "fuc4", x=fuc4_x, y_test=fuc4_x ** 2 * np.log(fuc4_x) / np.log(5), count=201, t_c=10000000)



