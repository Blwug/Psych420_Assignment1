import numpy as np  # scaler is one value

inputs = [1.0, 2.0, 3.0, 2.2]  # shapes is (1,4)

weights = [[0.2, 0.8, -0.3, 0.1],  # shapes is (3,4) & matrix has to have the same size
           [0.5, -0.9, -0.2, 0.5],  # 2D array && a matrix
           [0.2, -0.8, -0.3, 0.9]]

biases = [1.0, 2.0, 0.5]  # represents the b in ymx + b

output = np.dot(weights, inputs) + biases

threshold = [2, 2, 2]

for output_i, threshold_i in zip(output, threshold):
    difference = output_i - threshold_i
    break

print("difference of output - threshold prior to the gate " + str(difference))

if float(difference) > 0:
    difference = 1
else:
    if float(difference) < 0: difference = 0

print("converted value of difference " + str(difference))
print(output)

'''
every perceptron can have a different value for their threshold
output = np.dot(weights, inputs) + biases is the dot product of weight [0] * inputs[0] + weight [1] *inputs[1]...
    output is the hidden layer and we want the values index by the weight set
if we put in (input, weights) we will get an error shapes because of the difference in size 
more neurons = more area of effects which makes the neuron more representative

    
'''
