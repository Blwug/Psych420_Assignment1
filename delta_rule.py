import numpy as np

a = np.random.rand(3)
weight = np.random.rand(3)
threshold = 0.5
bias = np.random.rand(1)


def product(a, weights):
    x1 = np.dot(a, weights) + bias

    if x1 < threshold:
        x1 = np.append(x1, -1)
        print(x1)
    else:
        if x1 > threshold:
            x1 = np.append(x1, 1)
            print(x1)


def check(active_results, one_or_negative_one):
    if active_results == one_or_negative_one:
        return True
    else:
        return False


