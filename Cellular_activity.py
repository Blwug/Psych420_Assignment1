import numpy as np


inner_layer = np.array(([0.5, 0.5, 0.2],
                     [0.2, 0.7, 0.4],
                     [0.7, 0.4, 0.2],
                    ))

targets = np.array([1, 1, 0]) #true true false

weights = np.array([0.4, 0.2, 0.6])

bias = 0.5
l_rate = 0.1 #learning rate

def sigmoid(w_sum):
    return 1 / (1 + np.exp(-w_sum)) #1/1 + e**-weighted sum


def get_prediction(inner_layer, weights, bias):

    return sigmoid(np.dot(inner_layer, weights) + bias)


def cross_entropy(target, pred):
    return -(target * np.log10(pred) + (1 - target) * (np.log10(1 - pred))) #difference of target and prediction


def hidden_layer(inner_layer, weights, target, prediction, l_rate, bias):
    if prediction > target:

        new_weights = []
        bias += l_rate * (target - prediction) #initial bias + learning rate * (difference of target and prediction)
        for x, w in zip(inner_layer, weights):
            new_w = w + l_rate * (target - prediction) * x #(target - prediction) is error
            new_weights.append(new_w)
        return new_weights, bias #returns a tuple

    else:
        if prediction < target:
            new_weights = []
            for x, w in zip(inner_layer, weights):
                new_w = w + l_rate * (target + prediction) * x  # (target - prediction) is error
                new_weights.append(new_w)
            return new_weights, bias  # returns a tuple

for epoch in range(200): #epoch is the number of iterations
    for x, y in zip(inner_layer, targets):
        pred = get_prediction(x, weights, bias)
        error = cross_entropy(y, pred)
        weights, bias = hidden_layer(x, weights, y, pred, l_rate, bias)

    predictions = get_prediction(inner_layer, weights, bias)
    updated_value = np.mean(cross_entropy(targets, predictions)) #


    print("epoch", str(epoch))
    print("updated product: ", updated_value)