import numpy as np

class NeuralNetwork ():
    def __init__(self):
        np.random.seed(1)

        self.synaptic_weights = 2 * np.random.random((3,1)) - 1 #3 by 1 matrix between -1 and 1

    def sigmoid(self, x):
        return 1/ (1 + np.exp(-x))

    def sigmoid_deriv (self, x):
        return x * (1 -x)

    def train(self, train_input, train_output, train_iteration):

        for D in range (train_iteration):
            output = self.think(train_input)
            error = train_output - output #back propgation
        adjustment = np.dot(train_input.T, error * self.sigmoid(output)) #matrix multiplication of train inputs
        self.synaptic_weights += adjustment

    def think(self,inputs):
        inputs = inputs.astype(float) #int & float can't be used in an operation
        output = self.sigmoid(np.dot(inputs, self.synaptic_weights))

        return output

if __import__ == "__main__":
    neural_network = NeuralNetwork()

    print("random weights")
    print(neural_network.synaptic_weights)

training_input = np.array([[0,0,1], [1,1,1], [1,0,1], [0,1,1]])

training_outputs = np.array ([[0,1,1,0]]).T #transpose to make it a four by four

neural_network.train(training_input, training_outputs. train_iteration)

print("synaptic weights after training: " )
print(neural_network.synaptic_weights)
