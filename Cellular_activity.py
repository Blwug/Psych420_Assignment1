import numpy as np

inner_layer = np.array(([0.5, 0.5, 0.2],
                        [0.2, 0.7, 0.4],
                        [0.7, 0.4, 0.2],
                        ))

targets = np.array([1, 1, 0])  #

weights = np.array([0.4, 0.2, 0.4])
new = [0]
runs = []
bias = 1
l_rate = 0.1  # learning rate

def sigmoid(w_sum):
    return 1 / (1 + np.exp(-w_sum))  # 1/1 + e**-weighted sum


def get_prediction(inner_layer, weights, bias):
    return sigmoid(np.dot(inner_layer, weights) + bias)


def cross_entropy(target, pred):
    return -(target * np.log10(pred) + (1 - target) * (np.log10(1 - pred)))  # difference of target and prediction

product = np.dot(weights, inner_layer)

a = sigmoid(product)
b = get_prediction(inner_layer, weights, bias)

c = cross_entropy(targets, b)


print (a)
print (b)
print(c)


