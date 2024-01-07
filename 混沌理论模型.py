import numpy as np
import matplotlib.pyplot as plt


def main(k, y=0.6):
    x = np.linspace(1, 40, 40)
    plt.title(f"y = {y}, k = {k}")
    list_y = [y]
    for i in range(39):
        y = k * y * (1 - y)
        list_y.append(y)
    y_real = np.array(list_y)
    plt.plot(x, y_real)

    plt.show()


if __name__ == '__main__':
    main(0.8)
    main(2.2)
    main(3.2)
    main(3.5)
    main(3.9)











