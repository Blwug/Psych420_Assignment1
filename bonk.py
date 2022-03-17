import numpy as np
import random as rd
import matplotlib.pyplot as plt

x_values = np.array([rd.random() * 30 - 15 for i in range(30)])
y_values = np.array([rd.random() * 30 - 15 for i in range(30)])

y_values[:15] += 50

# plt.scatter(x_values, y_values)
# plt.show()

training_set = list(zip(x_values, y_values, [1] * 15 + [-1] * 15))
training_set = rd.sample(training_set, k=len(training_set))


def activation(step, weight):
    bias = 1
    threshold = 0

    sum = step[0] * weight[0] + step[1] * weight[1] + bias * weight[2]
    return 1 if sum >= threshold else -1

def delta_rule(ipt, weight, obs, des):
    lr = 0.1
    for i  in range(len(weight)):
        weight[i] = weight[i] + ((des - obs) * lr * ipt[i])
    return weight

weight = [rd.random() for i in range(3)]

correct = 0
while correct < len(training_set):
    correct = 0
    for step in training_set:
        obs = activation(step, weight)
        if obs == step[2]:
            correct += 1
        else:
            ipt = [step[0], step[1], 1]
            weight = delta_rule(ipt, weight, obs, step[2])

print("Final weights: " + str(weight))

evaluation = []
for step in training_set:
    output = activation(step, weight)
    evaluation.append([step[0], step[1], output])

def plot(data):
    for x in data:
        plt.scatter(x[0], x[1], color="red" if x[2] == 1 else "green")
    plt.show()

plot(training_set)
plot(evaluation)

