import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt


def cal_imaginary(c, max_limit):
    j = c
    for i in range(max_limit):
        if abs(j) > 2:
            return i
        j = j * j + c
    return max_limit


def make_mandelbrot(area_split, max_limit):
    x_list = np.linspace(-2, 1, area_split)
    y_list = np.linspace(-1.5, 1.5, area_split)
    coordinate_list = np.zeros((area_split, area_split))

    for i, y in enumerate(y_list):
        for j, x in enumerate(x_list):
            print(str(i) + ", " + str(j))
            coordinate_list[i, j] = cal_imaginary(complex(x, y), max_limit)

    plt.imshow(coordinate_list, cmap=cm.inferno)
    plt.colorbar()
    plt.show()


make_mandelbrot(5000, 100)
