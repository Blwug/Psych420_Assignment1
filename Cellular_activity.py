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
goal = [0.2590329139118882]
iteration = 0
instance = [iteration]

def sigmoid(w_sum):
    return 1 / (1 + np.exp(-w_sum))  # 1/1 + e**-weighted sum


def get_prediction(inner_layer, weights, bias):
    return sigmoid(np.dot(inner_layer, weights) + bias)


def cross_entropy(target, pred):
    return -(target * np.log10(pred) + (1 - target) * (np.log10(1 - pred)))  # difference of target and prediction

def hidden_layer(inner_layer, weights, target, prediction, l_rate, bias):
    new_weights = []
    bias += l_rate * (target - prediction)  # bias = initial bias + learning rate * (difference of target and prediction)
    for x, w in zip(inner_layer, weights): #inner_layer[2],weights[2] are paired together when passed for instance
        new_w = w + l_rate * (target - prediction) * x  # (target - prediction) is error
        new_weights.append(new_w)
    return new_weights, bias  # returns a tuple

while True:

    if new == goal:
        false = 1
        iteration += 1
        instance.append(iteration)

        break
    else:
        for x, y in zip(inner_layer,
                        targets):  # pairs the values being passed in every iteration so inner_layer[0],targets[0]
            pred = get_prediction(x, weights, bias)
            error = cross_entropy(y, pred)
            weights, bias = hidden_layer(x, weights, y, pred, l_rate, bias)

        predictions = get_prediction(inner_layer, weights, bias)
        updated_value = np.mean(cross_entropy(targets, predictions))

        new = updated_value
        false = 0
        iteration += 1

        print("dot product value" +str(new))
        print("number of " +str(false))
        print ("number of iterations " +str (iteration))

print(false)
