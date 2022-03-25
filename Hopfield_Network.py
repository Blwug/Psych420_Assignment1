import numpy as np
input = [1,-1,1]
weights = [1, -1, 1]
expected_pattern = [1,-1,1]
check_input = [1, -1, 1]


def hopfield(inner_layer, weight):
    r1 = [i * weight[0] for i in (inner_layer)]
    r2 = [i * weight[1] for i in (inner_layer)]
    r3 = [i * weight[2] for i in (inner_layer)]
    r1[0] = 0
    r2[1] = 0
    r3[2] = 0
    output = [r1,r2,r3]
    return output

def threshold(result):
    threshold = 0
    for i in range(len(result)):
        if result[i] > threshold:
            result[i] = 1
        else:
            result[i] = -1


matrix = hopfield(input, weights)
print(matrix)

temp = np.array([matrix[0]])
print (temp)

te =[y * check_input for y in (temp)]
print (te)


